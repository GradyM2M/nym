#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
import actionlib

from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class TrajectoryDemo():
    def __init__(self):
        rospy.init_node('trajectory_demo')
        
        # 是否需要回到初始化的位置
        reset = rospy.get_param('~reset', False)
        
        # 机械臂中joint的命名
        orochi_joints = ['joint_1',
                         'joint_2',
                         'joint_3', 
                         'joint_4',
                         'joint_5',
                         'joint_6',
                         'joint_7']
        
        if reset:
            # 如果需要回到初始化位置，需要将目标位置设置为初始化位置的七轴角度
            orochi_goal  = [0, 0, 0, 0, 0, 0, 0]

        else:
            # 如果不需要回初始化位置，则设置目标位置的七轴角度
            orochi_goal  = [-0.5, -1.0, 0.4, 0.8, 0.7, 1.0, 0]
    
        # 连接机械臂轨迹规划的trajectory action server
        rospy.loginfo('Waiting for orochi trajectory controller...')       
        arm_client = actionlib.SimpleActionClient('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
        arm_client.wait_for_server()        
        rospy.loginfo('...connected.')  
    
        # 使用设置的目标位置创建一条轨迹数据
        arm_trajectory = JointTrajectory()
        arm_trajectory.joint_names = orochi_joints
        arm_trajectory.points.append(JointTrajectoryPoint())
        arm_trajectory.points[0].positions = orochi_goal
        arm_trajectory.points[0].velocities = [0.0 for i in orochi_joints]
        arm_trajectory.points[0].accelerations = [0.0 for i in orochi_joints]
        arm_trajectory.points[0].time_from_start = rospy.Duration(3.0)
    
        rospy.loginfo('Moving the arm to goal position...')
        
        # 创建一个轨迹目标的空对象
        orochi_goal = FollowJointTrajectoryGoal()
        
        # 将之前创建好的轨迹数据加入轨迹目标对象中
        orochi_goal.trajectory = arm_trajectory
        
        # 设置执行时间的允许误差值
        orochi_goal.goal_time_tolerance = rospy.Duration(0.0)
    
        # 将轨迹目标发送到action server进行处理，实现机械臂的运动控制
        arm_client.send_goal(orochi_goal)

        # 等待机械臂运动结束
        arm_client.wait_for_result(rospy.Duration(5.0))
        
        rospy.loginfo('...done')
        
if __name__ == '__main__':
    try:
        TrajectoryDemo()
    except rospy.ROSInterruptException:
        pass
    
