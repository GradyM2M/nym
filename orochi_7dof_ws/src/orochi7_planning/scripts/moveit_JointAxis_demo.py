#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
# from control_msgs.msg import GripperCommand

class MoveItJointAxisDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_JointAxis_demo', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        orochi_arm = moveit_commander.MoveGroupCommander('arm')
        
        # 初始化需要使用move group控制的机械臂中的gripper group
        orochi_gripper = moveit_commander.MoveGroupCommander('gripper')
        
        # 设置机械臂和夹爪的允许误差值
        orochi_arm.set_goal_joint_tolerance(0.001)
        orochi_gripper.set_goal_joint_tolerance(0.001)
        
        # 设置每次运动规划的时间限制：1s
        orochi_arm.set_planning_time(1)

        # 控制机械臂先回到初始化位置
        orochi_arm.set_named_target('home')
        orochi_arm.go()
        rospy.sleep(0.5)
         
        # 设置夹爪的目标位置，并控制夹爪运动
        # orochi_gripper.set_joint_value_target([0.01])
        # orochi_gripper.go()
        # rospy.sleep(0.1)
        
        # ---------------------  第一段轨迹生成，关节空间插值  ---------------------#
        
        # 设置机械臂的目标位置，使用七轴的位置数据进行描述（单位：弧度）
        joint_positions = [0, 0.785398, 0, 1.570796, 0, 0.785398, 0]
        orochi_arm.set_joint_value_target(joint_positions)
                 
        # 控制机械臂完成运动
        orochi_arm.go()
        rospy.sleep(0.5)

        # ---------------------  第二段轨迹生成，关节空间插值  ---------------------#

        # 设置机械臂的目标位置，使用七轴的位置数据进行描述（单位：弧度）
        joint_positions = [2.70994806605, -1.21800158073, 0.816776451192, -0.975483053825, 0.8559809165, 1.30229459067, -1.21311465215]
        orochi_arm.set_joint_value_target(joint_positions)
                 
        # 控制机械臂完成运动
        orochi_arm.go()
        rospy.sleep(0.5)       
        
        # ---------------------  第三段轨迹生成，关节空间插值  ---------------------#

        # 设置机械臂的目标位置，使用七轴的位置数据进行描述（单位：弧度）
        joint_positions = [0, 0, 0, 0, 0, 0, 0]
        orochi_arm.set_joint_value_target(joint_positions)
                 
        # 控制机械臂完成运动
        orochi_arm.go()
        rospy.sleep(1)

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItJointAxisDemo()
    except rospy.ROSInterruptException:
        pass
