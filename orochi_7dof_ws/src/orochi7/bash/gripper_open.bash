#!/bin/bash


# rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory "header:
rostopic pub /orochi/gripper_controller/command trajectory_msgs/JointTrajectory "header:

  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
joint_names: ['left_gripper_finger_joint', 'right_gripper_finger_joint']
points:
- positions: [0.0,0.0]
  velocities: []
  accelerations: []
  effort: []
  time_from_start: {secs: 0.5, nsecs: 990099009}"

# - positions: [-1.94761217286908,-0.660726252078899,0.589841186608446,-1.42858440895602,-1.37640744799328,-1.26145694817514,0]
# - positions: [1.94761217286908,0.660726252078899,-0.589841186608446,1.42858440895602,1.37640744799328,1.26145694817514,0.2]
# - positions: [0,0,0,0,0,0,0]
