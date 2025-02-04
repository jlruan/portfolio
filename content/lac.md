---
title: "NASA Lunar Autonomy Challenge"
date: 2025-01-12T00:23:20-08:00
draft: false
image: '../images/lac.jpg'
description: "I founded Purdue's NASA Lunar Autonomy Challenge team, and we were one of 20 or so teams selected to compete. More..."
---
I founded Purdue's NASA Lunar Autonomy Challenge team, and we were one of 20 or so teams selected to compete. The goal of the competition was to map a selected area of lunar topography as efficiently as possible using a pre-existing rover type. 

Our approach was to generate a point cloud and then use RANSAC to identify the ground plane, and use the point cloud as well as a Yolov11 detector to match rocks. 

{{< video
  src="/videos/lac.mp4"
>}}

We then used odometry data from ORB_SLAM3 to localize our mapping, providing high-quality location data through both stereo and monocular cameras.

![LAC1](/images/lac.png)

We're currently working on integrating image compression & ROS2. Check back soon for more updates!
