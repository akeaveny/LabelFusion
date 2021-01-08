# CMake generated Testfile for 
# Source directory: /home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/java
# Build directory: /home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/java
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(Java::client_server "/usr/bin/python" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/java/../run_client_server_test.py" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/c/test-c-server" "/usr/bin/java" "-cp" "/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/java/lcm-test.jar:/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/test/types/lcm-test-types.jar:/home/akeaveny/catkin_ws/src/LabelFusion/lcm/build/lcm-java/lcm.jar:/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/java/junit-4.11.jar:/home/akeaveny/catkin_ws/src/LabelFusion/lcm/test/java/hamcrest-core-1.3.jar" "LcmTestClient")
