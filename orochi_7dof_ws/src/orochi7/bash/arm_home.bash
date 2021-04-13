#!/bin/bash


# rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory "header:
rostopic pub /panda/arm_controller/command trajectory_msgs/JointTrajectory "header:

  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
joint_names: ['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7']
points:
- positions: [0,0,0,-1.5708,0,0,0]
  velocities: []
  accelerations: []
  effort: []
  time_from_start: {secs: 2.0, nsecs: 990099009}"

# - positions: [-1.94761217286908,-0.660726252078899,0.589841186608446,-1.42858440895602,-1.37640744799328,-1.26145694817514,0]
# - positions: [1.94761217286908,0.660726252078899,-0.589841186608446,1.42858440895602,1.37640744799328,1.26145694817514,0.2]
# - positions: [0,0,0,0,0,0,0]
