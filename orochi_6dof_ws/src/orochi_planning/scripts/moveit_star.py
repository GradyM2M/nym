#!/usr/bin/env python
#encoding=utf-8

import sys
from copy import deepcopy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
# from lineConstraint import lineConstraint
from std_msgs.msg import String
from math import cos, sin, pi
import time

def move_group_python_interface_tutorial():
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('move_group_python_interface_tutorial',
                  anonymous=True)

  arm = moveit_commander.MoveGroupCommander("arm")
 
  arm.set_pose_reference_frame('base_link')
  ## We can get the name of the reference frame for this robot
  print "============ Reference frame: %s" % arm.get_planning_frame()

  ## We can also print the name of the end-effector link for this group
  end_effector_link = arm.get_end_effector_link()
  print "============ End effector: %s" % end_effector_link

  arm.set_goal_tolerance(0.01);
    
  arm.set_joint_value_target([0, 0, 0, 0, 0, 0])
  arm.go()
  rospy.sleep(1)
  waypoints = []

  delta = 0.6
  R = 0.1
  X = R * cos(18.0/180*pi)
  Y = delta + R * sin(18.0/180*pi)
  Z = R * cos(54.0/180*pi)
  W = delta -R * sin(54.0/180*pi)

  star = [[-X, Y], [X, Y], [-Z, W], [0, R+delta], [Z, W], [-X, Y]]
  # star = [[-0.2853, 0.3925], [0.2853, 0.3925], [-0.1763, 0.0573], [0, 0.6], [0.1763, 0.0573], [-0.2853, 0.3925]]
  '''
  L = [0.257, 0.255, 0.250, 0.150, 0, 0]
  for j in range(5):
    st_pos = deepcopy(star[j])
    st_pos.insert(0, 0.4)
    ed_pos = deepcopy(star[j+1])
    ed_pos.insert(0, 0.4)
  
    lc = lineConstraint(L, st_pos, ed_pos, 0, 10, 0.01, 1e-7)
  
    poses = lc.makePoses()
    for i in range(len(poses)):
      if not rospy.is_shutdown():
          arm.set_start_state_to_current_state()
          arm.set_pose_target(poses[i])
          arm.go()
  '''
  pose = geometry_msgs.msg.Pose()
  pose.orientation.x = 0
  pose.orientation.y = 1
  pose.orientation.z = 0
  # pose.orientation.w = 0.707106781186547
  pose.orientation.w = 0

  st_x = 0.4
  pose.position.x = st_x
  pose.position.y = star[0][0]
  pose.position.z = star[0][1]
  arm.set_pose_target(pose)
  arm.go()
  '''
    print pose
    print '*'*30
    arm.set_pose_target(pose)
    arm.go()
    rospy.sleep(1)
  '''
  
  for i in range(6):
      pose.position.x = st_x
      pose.position.y = star[i][0]
      pose.position.z = star[i][1]
      waypoints.append(deepcopy(pose))
  '''
  waypoints.append(deepcopy(pose))
  pose.position.x += 0.15
  waypoints.append(deepcopy(pose))
  print waypoints
  ''' 
  fraction = 0.0
  maxtries = 100
  attempts = 0

  # Set the internal state to the current state
  arm.set_start_state_to_current_state()
    
  start_time = time.time()
  # Plan the Cartesian path connecting the waypoints
  while fraction < 1.0 and attempts < maxtries:
      (plan, fraction) = arm.compute_cartesian_path (
                              waypoints,   # waypoint poses
                              0.01,        # eef_step
                              0.0,         # jump_threshold
                              True)        # avoid_collisions
      
      # Increment the number of attempts 
      attempts += 1
      
      # Print out a progress message
      if attempts % 10 == 0:
          rospy.loginfo("Still trying after " + str(attempts) + " attempts...")
               
  # If we have a complete plan, execute the trajectory
  if fraction == 1.0:
      rospy.loginfo("Path computed successfully. Moving the arm.")
      end_time = time.time()
      rospy.loginfo("Planning time: " + str(end_time - start_time))
      arm.execute(plan)
      rospy.loginfo("Path execution complete.")
  else:
      rospy.loginfo("Path planning failed with only " + str(fraction) + " success after " + str(maxtries) + " attempts.") 
  '''
  with open ("/home/jyk/Desktop/data.txt",'w') as f:
      for point in plan.joint_trajectory.points:
              f.write(str(point.positions).replace('(','').replace(')','').replace(',',' '))
              f.write('\n')
  '''
  

  arm.set_joint_value_target([0, 0, 0, 0, 0, 0])
  arm.go()
  rospy.sleep(1)
  
  ## When finished shut down moveit_commander.
  moveit_commander.roscpp_shutdown()

if __name__=='__main__':
  try:
    move_group_python_interface_tutorial()
  except rospy.ROSInterruptException:
    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)
