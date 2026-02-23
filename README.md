# Autonomous Circular Navigation with Obstacle Avoidance using Nav2 and DWB

## Overview

This project demonstrates autonomous mobile robot navigation using the ROS 2 Navigation Stack. The robot follows a predefined circular trajectory stored in a YAML configuration file while performing real-time obstacle avoidance using the DWB local planner.

The system is implemented using:

- ROS 2 Galactic
- TurtleBot3 Simulation in Gazebo
- Navigation2 Stack
- DWB Local Planner
- AMCL Localization

---

## Features

- Infinite circular path traversal
- Path definition using YAML waypoint configuration
- Real-time obstacle avoidance
- Rejoining original trajectory after deviation
- Localization using AMCL
- Costmap-based navigation planning
- Simulation-based validation

---

## System Architecture

The navigation framework is built on the ROS 2 Navigation2 stack:

- Global Planner → Generates waypoint sequence
- Local Planner (DWB) → Performs dynamic obstacle avoidance
- Localization Module → AMCL-based pose estimation
- Controller Server → Executes trajectory tracking

---

## Requirements

### Software

- Ubuntu 20.04
- ROS 2 Galactic
- Gazebo 11
- TurtleBot3 Simulation Packages

---

## ROS Package Installation

```bash
sudo apt install ros-galactic-navigation2
sudo apt install ros-galactic-nav2-bringup
sudo apt install ros-galactic-turtlebot3*
sudo apt install ros-galactic-gazebo-ros-pkgs
