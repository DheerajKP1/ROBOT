source /opt/ros/jazzy/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard



cd /mnt/9E0C3C590C3C2EA1/mtp/gazebo_env
colcon build 
source install/setup.bash 
ros2 launch mtp_robot robot.launch.py
ros2 launch mtp_robot slam.launch.py
ros2 run rviz2 rviz2

for custom world file
ros2 launch mtp_robot robot.launch.py world:=src/mtp_robot/worlds/room.world

ros2 topic list
gz topic -l


