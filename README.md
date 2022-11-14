# orochi

This repository contains two folders, one of which is a 6-axis manipulator in the orochi series, and the other is a 7-axis manipulator.
You can build it with the following commands:

```sh
$ cd ~/catkin_ws/src
$ git clone https://github.com/GradyM2M/orochi.git
$ cd .. && catkin_make && source devel/setup.bash
```

### 功能包使用方法

```sh
$ roslaunch orochi7_gripper_gazebo orochi_control_bringup_moveit.launch
$ roslaunch orochi7 ar_track_alvar.launch
$ rosrun orochi7_planning ar_track_follower.py
```

## Prototype Design
<img src="https://github.com/GradyM2M/linear_stepper_motor_controller/blob/main/img/%E6%A0%B7%E6%9C%BA%E5%9B%BE.jpg" width="1000">
