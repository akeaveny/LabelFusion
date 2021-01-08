# CMake generated Testfile for 
# Source directory: /home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/cpp
# Build directory: /home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/cpp
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(CPP::memq_test "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/cpp/test-cpp-memq_test")
add_test(CPP::client_server "/usr/bin/python" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/cpp/../run_client_server_test.py" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/c/test-c-server" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/cpp/test-cpp-client")
