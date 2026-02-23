# Autonomous Circular Navigation with Obstacle Avoidance using Nav2 and DWB

## Overview

This project demonstrates autonomous mobile robot navigation using the ROS 2 Navigation Stack. The robot follows a predefined circular trajectory stored in a YAML configuration file while performing real-time obstacle avoidance using the DWB local planner.

The system is implemented using:

- ROS 2 Galactic
- TurtleBot3 Simulation in Gazebo
- Navigation2 Stack
- DWB Local Planner
- AMCL Localization

## Features

- Infinite circular path traversal
- Path definition using YAML waypoint configuration
- Real-time obstacle avoidance
- Rejoining original trajectory after deviation
- Localization using AMCL
- Costmap-based navigation planning
- Simulation-based validation

## System Architecture

The navigation framework is built on the ROS 2 Navigation2 stack:

- Global Planner → Generates waypoint sequence
- Local Planner (DWB) → Performs dynamic obstacle avoidance
- Localization Module → AMCL-based pose estimation
- Controller Server → Executes trajectory tracking

## Requirements

### Software

- Ubuntu 20.04
- ROS 2 Galactic
- Gazebo 11
- TurtleBot3 Simulation Packages

### ROS Packages

Install required dependencies:


sudo apt install ros-galactic-navigation2
sudo apt install ros-galactic-nav2-bringup
sudo apt install ros-galactic-turtlebot3*
sudo apt install ros-galactic-gazebo-ros-pkgs
Workspace Setup
mkdir -p fixed_path_ws/src
cd fixed_path_ws
colcon build
source install/setup.bash
Execution Steps
Launch Simulation
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
Launch Navigation Stack
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True
Run Path Execution Node
ros2 run fixed_path_nav path_sender

### **Path Configuration**

The circular trajectory is defined inside:

path/circle_path.yaml

Users can modify waypoint coordinates to change robot motion patterns.

## **Obstacle Avoidance**

**Obstacle avoidance is handled by:

DWB local planner critics

Inflation costmap layers

Real-time LiDAR scan processing

Visualization

The system can be monitored using RViz2:

Map frame tracking

Robot pose estimation

Path execution monitoring

Obstacle costmap visualization

Future Improvements

Dynamic obstacle prediction

Multi-robot cooperative navigation

Learning-based path optimization

Real-world deployment validation**

**License

This project is intended for academic and research demonstration purposes.

Author

Vinayak N Nayak
**
