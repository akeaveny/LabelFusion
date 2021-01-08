# CMake generated Testfile for 
# Source directory: /home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/python
# Build directory: /home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(Python::bool_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/types:/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/python/bool_test.py")
add_test(Python::byte_array_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/types:/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/python/byte_array_test.py")
add_test(Python::lcm_file_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/types:/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/python/lcm_file_test.py")
add_test(Python::lcm_memq_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/types:/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/python/lcm_memq_test.py")
add_test(Python::lcm_thread_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/types:/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/python/lcm_thread_test.py")
add_test(Python::client_server "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/types:/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/run_client_server_test.py" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/c/test-c-server" "/usr/bin/python" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/python/client.py")
