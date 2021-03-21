# orochi
├── orochi
│   ├── CMakeLists.txt
│   ├── config
│   │   ├── joint_names_orochi.yaml
│   │   └── orochi.yaml
│   ├── export.log
│   ├── launch
│   │   ├── camera_image.launch
│   │   ├── display.launch
│   │   ├── display_orochi_camera.launch
│   │   ├── fake_orochi.launch
│   │   └── gazebo_test.launch
│   ├── meshes
│   │   ├── base_link.STL
│   │   ├── kinect.dae
│   │   ├── Link_0.STL
│   │   ├── Link_1.STL
│   │   ├── Link_2.STL
│   │   ├── Link_3.STL
│   │   ├── Link_4.STL
│   │   ├── Link_5.STL
│   │   ├── Link_6.STL
│   │   └── simple_box.dae
│   ├── package.xml
│   ├── textures
│   ├── urdf
│   │   ├── camera.xacro
│   │   ├── orochi.csv
│   │   ├── orochi.urdf
│   │   ├── orochi_with_camera.xacro
│   │   └── orochi.xacro
│   └── urdf.rviz
├── orochi_gazebo
│   ├── CMakeLists.txt
│   ├── config
│   │   ├── orochi_gazebo_control1.yaml
│   │   ├── orochi_gazebo_control.yaml
│   │   ├── orochi_gazebo_joint_states.yaml
│   │   └── trajectory_control.yaml
│   ├── launch
│   │   ├── orochi_bringup_moveit.launch
│   │   ├── orochi_gazebo_control.launch
│   │   ├── orochi_gazebo_controller.launch
│   │   ├── orochi_gazebo_states.launch
│   │   ├── orochi_trajectory_controller.launch
│   │   └── orochi_world.launch
│   ├── package.xml
│   └── set.bash
├── orochi_moveit_config
│   ├── CMakeLists.txt
│   ├── config
│   │   ├── chomp_planning.yaml
│   │   ├── controllers_gazebo.yaml
│   │   ├── controllers.yaml
│   │   ├── fake_controllers.yaml
│   │   ├── joint_limits.yaml
│   │   ├── kinematics.yaml
│   │   ├── ompl_planning.yaml
│   │   ├── orochi.srdf
│   │   ├── ros_controllers.yaml
│   │   └── sensors_3d.yaml
│   ├── launch
│   │   ├── chomp_planning_pipeline.launch.xml
│   │   ├── default_warehouse_db.launch
│   │   ├── demo_gazebo.launch
│   │   ├── demo.launch
│   │   ├── fake_moveit_controller_manager.launch.xml
│   │   ├── gazebo.launch
│   │   ├── joystick_control.launch
│   │   ├── move_group.launch
│   │   ├── moveit_planning_execution.launch
│   │   ├── moveit.rviz
│   │   ├── moveit_rviz.launch
│   │   ├── ompl_planning_pipeline.launch.xml
│   │   ├── orochi_moveit_controller_manager.launch.xml
│   │   ├── orochi_moveit_sensor_manager.launch.xml
│   │   ├── planning_context.launch
│   │   ├── planning_pipeline.launch.xml
│   │   ├── ros_controllers.launch
│   │   ├── run_benchmark_ompl.launch
│   │   ├── sensor_manager.launch.xml
│   │   ├── setup_assistant.launch
│   │   ├── trajectory_execution.launch.xml
│   │   ├── warehouse.launch
│   │   └── warehouse_settings.launch.xml
│   ├── package.xml
│   └── scripts
│       ├── camera_demo.py
│       └── moveit_obstacles_demo.py
└── orochi_planning
    ├── 2020-05-27-19-58-57.bag
    ├── CMakeLists.txt
    ├── config
    │   ├── arm_paths.rviz
    │   └── pick_and_place.rviz
    ├── launch
    │   ├── arm_planning_with_trail.launch
    │   └── orochi_planning.launch
    ├── moveit_bag.rviz
    ├── package.xml
    └── scripts
        ├── moveit_cartesian_demo.py
        ├── moveit_cartesian_line_demo.py
        ├── moveit_cartesian_test.py
        ├── moveit_circle_demo.py
        ├── moveit_circle.py
        ├── moveit_circle_test.py
        ├── moveit_fk_demo.py
        ├── moveit_ik_demo.py
        ├── moveit_ik_test.py
        ├── moveit_obstacles_demo.py
        ├── moveit_pick_and_place_demo.py
        ├── moveit_star.py
        └── trajectory_demo.py

