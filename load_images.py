import cv2
import glob
import numpy as np

from PIL import Image
import matplotlib.pyplot as plt

import argparse

import skimage.io

############################################################
#  argparse
############################################################
parser = argparse.ArgumentParser(description='Load YCB Images')

parser.add_argument(
                    '--object_rpe_dataset', required=False, default='/home/akeaveny/catkin_ws/src/ElasticFusion/png_to_klg/object_rpe_data/depth/',
                    type=str,
                    metavar="/path/to/Affordance/dataset/")

parser.add_argument(
                    '--zed_dataset', required=False, default='/home/akeaveny/catkin_ws/src/ElasticFusion/png_to_klg/zed/depth/',
                    # '--zed_dataset', required=False, default='/home/akeaveny/catkin_ws/src/object-rpe-ak/densefusion_ros/images/zed/',
                    type=str,
                    metavar="/path/to/Affordance/dataset/")

parser.add_argument(
                    '--labelfusion_labels', required=False,
                    default='/home/akeaveny/Datasets/LabelFusion_Data/logs/006_mustard_bottle_01/images/',
                    type=str,
                    metavar="/path/to/Affordance/dataset/")

args = parser.parse_args()

#########################
# load images
#########################
# depth_image_ext = ".png"
depth_image_ext = "_depth.png"

labels_image_ext = "_labels.png"

arl_syn_path_ = args.labelfusion_labels + "*" + depth_image_ext
# arl_syn_path_ = args.labelfusion_labels + "*" + labels_image_ext
arl_syn_files = sorted(glob.glob(arl_syn_path_))
arl_syn_max_depth = -np.inf
arl_syn_min_depth = np.inf
NDDS_DEPTH_CONST = 10e3 / (2 ** 8 - 1)

print('Loaded {} Images'.format(len(arl_syn_files)))

for idx, image_addr in enumerate(arl_syn_files):

    #####################
    # MAX DEPTH
    #####################
    arl_syn_depth = np.array(Image.open(image_addr))

    img_max_depth = np.max(arl_syn_depth)
    img_min_depth = np.min(arl_syn_depth)

    # if img_max_depth == (2 ** 16 - 1):
    #     print(image_addr)
        # print("Img dtype:\t{}, Min Depth:\t{}, Max Depth:\t{}".format(arl_syn_depth.dtype, img_min_depth, img_max_depth))

    ### plot
    plt.figure(0)
    plt.title("Max Depth")
    plt.imshow(arl_syn_depth)
    print("Img dtype:\t{}, Min Depth:\t{}, Max Depth:\t{}".format(arl_syn_depth.dtype, img_min_depth, img_max_depth))
    plt.show()
    plt.ioff()


    arl_syn_max_depth = img_max_depth if img_max_depth > arl_syn_max_depth else arl_syn_max_depth
    arl_syn_min_depth = img_min_depth if img_min_depth < arl_syn_min_depth else arl_syn_min_depth
print("Min Depth:\t{}, Max Depth:\t{}".format(arl_syn_min_depth, arl_syn_max_depth))