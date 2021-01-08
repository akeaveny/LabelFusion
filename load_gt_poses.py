import cv2
import glob
import numpy as np

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import argparse

import skimage.io

import yaml

from scipy.spatial.transform import Rotation as R

from skimage.color import gray2rgb

############################################################
############################################################

class_file = open('/home/akeaveny/arl_labelfusion_dataset/object-meshes/arl_scans/DenseFusion/classes_train.txt')
class_id_file = open('/home/akeaveny/arl_labelfusion_dataset/object-meshes/arl_scans/DenseFusion/classes_ids_train.txt')
class_IDs = np.loadtxt(class_id_file, dtype=np.int32)

cld = {}
for class_id in class_IDs:
    print("class_id: ", class_id)
    class_input = class_file.readline()
    print("class_input: ", class_input)
    if not class_input:
        break
    input_file = open('/home/akeaveny/arl_labelfusion_dataset/object-meshes/arl_scans/DenseFusion/{}.xyz'.format(class_input[:-1]))
    cld[class_id] = []
    while 1:
        input_line = input_file.readline()
        if not input_line:
            break
        input_line = input_line[:-1].split(' ')
        cld[class_id].append([float(input_line[0]), float(input_line[1]), float(input_line[2])])
    cld[class_id] = np.array(cld[class_id])
    input_file.close()

############################################################
#  argparse
############################################################
parser = argparse.ArgumentParser(description='Load YCB Images')

parser.add_argument(
                    '--labelfusion_labels', required=False,
                    ### tools
                    # default='/home/akeaveny/arl_labelfusion_dataset/logs/arl_single_mallet_1/images/',
                    # default='/home/akeaveny/arl_labelfusion_dataset/logs/arl_single_spatula_6/images/',
                    # default='/home/akeaveny/arl_labelfusion_dataset/logs/arl_single_wooden_spoon_8/images/',
                    # default='/home/akeaveny/arl_labelfusion_dataset/logs/arl_single_screwdriver_8/images/',
                    # default='/home/akeaveny/arl_labelfusion_dataset/logs/arl_single_garden_shovel_1/images/',
                    ### clutter
                    # default='/home/akeaveny/arl_labelfusion_dataset/logs/test_clutter_scene_1/images/',
                    ### dataset
                    default='/home/akeaveny/arl_labelfusion_dataset/arl_test_clutter_1/test_clutter_scene_1/images/',
                    type=str,
                    metavar="/path/to/Affordance/dataset/")

args = parser.parse_args()

#########################
# load images
#########################
rgb_image_ext = "_depth.png"

labelfusion_path_ = args.labelfusion_labels + "*" + rgb_image_ext
labelfusion_files = sorted(glob.glob(labelfusion_path_))
print('Loaded {} Images'.format(len(labelfusion_files)))

output = {}
output['cls_indexes'] = []

for image_idx, image_addr in enumerate(labelfusion_files):

    str_num = image_addr.split('/')[-1].split(rgb_image_ext)[0]

    rgb_addr = args.labelfusion_labels + str_num + "_rgb.png"
    depth_addr = args.labelfusion_labels + str_num + "_depth.png"
    gt_addr = args.labelfusion_labels + str_num + "_labels.png"
    pose_addr = args.labelfusion_labels + str_num + "_poses.yaml"

    rgb = np.array(Image.open(rgb_addr))
    depth = np.array(Image.open(depth_addr))
    gt_label = np.array(Image.open(gt_addr))

    #####################
    #####################
    yaml_file = open(pose_addr, 'r')
    parsed = yaml.load(yaml_file, Loader=yaml.FullLoader)

    labels = []
    poses = []
    for idx, obj in enumerate(parsed.keys()):
        label = np.asarray(parsed[obj]['label'], dtype=np.uint8)
        labels.append(label)
        # translation
        trans = parsed[obj]['pose'][0]
        # rotation
        quart = parsed[obj]['pose'][1] # x y z w
        quart.append(quart[0])
        quart.pop(0)
        rot = R.from_quat(quart)  # x y z w
        pose = rot.as_matrix().tolist()

        for i in range(0, 3):
            pose[i].append(trans[i])

        if idx == 0:
            for i in range(0, 3):
                row = []
                for k in range(0, 4):
                    ele = []
                    ele.append(pose[i][k])
                    row.append(ele)
                poses.append(row)
        else:
            for i in range(0, 3):
                for k in range(0, 4):
                    poses[i][k].append(pose[i][k])

    poses = np.asarray(poses)
    poses = np.reshape(poses, (3, 4, len(parsed)))
    output['poses'] = poses

    labels_array = np.asarray(labels, dtype=np.uint8)
    output['cls_indexes'] = np.reshape(labels_array, (len(labels), -1))

    factor_depth = np.asarray([1000], dtype=np.uint16)
    output['factor_depth'] = [factor_depth]

    ####################
    # project points
    ####################
    rgb1 = rgb.copy()
    for idx, affordance_id in enumerate(labels_array):
        if affordance_id in class_IDs:
            cam_rotation4 = poses[0:3, 0:3, idx]
            cam_translation = poses[0:3, -1, idx]

            cam_cx = 341.276
            cam_cy = 175.296
            cam_fx = 338.546630859375
            cam_fy = 338.546630859375

            cam_mat = np.array([[cam_fx, 0, cam_cx], [0, cam_fy, cam_cy], [0, 0, 1]])
            dist = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
            # print("cam_mat: \n", cam_mat)

            imgpts, jac = cv2.projectPoints(cld[affordance_id] * 1e3,
                                            cam_rotation4,
                                            cam_translation * 1e3,
                                            cam_mat, dist)

            cv2_img = cv2.polylines(rgb1, np.int32([np.squeeze(imgpts)]), True, (0, 255, 255))
            cv2_label = cv2.polylines(gray2rgb(gt_label)*55, np.int32([np.squeeze(imgpts)]), True, (0, 255, 255))

    ####################
    # plot
    ####################
    # plt.figure(0)
    # plt.subplot(2, 2, 1)
    # plt.title("rgb")
    # plt.imshow(rgb)
    # plt.subplot(2, 2, 2)
    # plt.title("depth")
    # plt.imshow(depth)
    # print("Depth Img dtype:\t{}, Min Depth:\t{}, Max Depth:\t{}".format(depth.dtype, np.min(depth), np.max(depth)))
    # plt.subplot(2, 2, 3)
    # plt.title("gt_label")
    # plt.imshow(gt_label)
    # print("Label Img:\t{}".format(np.unique(gt_label)))
    # plt.subplot(2, 2, 4)
    # plt.title("gt_pose")
    # plt.imshow(cv2_img)
    # plt.show()

    print("\tImage Idx: {}".format(str_num))
    cv2.imshow('gt_pose', cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))
    cv2.waitKey(10)
