---
title: "NASA Lunar Autonomy Challenge"
date: 2025-01-12T00:23:20-08:00
draft: false
image: '../images/lac.webp'
description: "I founded Purdue's NASA Lunar Autonomy Challenge team, and we were one of 20 or so teams selected to compete. More..."
---
I founded Purdue's NASA Lunar Autonomy Challenge team, and we were one of 20 or so teams selected to compete. The goal of the competition was to map a selected area of lunar topography as efficiently as possible using a pre-existing rover type. 

Our approach was to generate a point cloud and then use RANSAC to identify the ground plane, and use the point cloud as well as a Yolov11 detector to match rocks. 

{{< video
  src="/videos/lac.mp4"
>}}

We then used odometry data from ORB_SLAM3 to localize our mapping, providing high-quality location data through both stereo and monocular cameras. We use this location and visual data on start to implement MPPI path rollouts to simulate the most productive way to map the lunar surface.

![LAC1](/images/lac_slam.webp)

Unfortunately, all of our workstations encountered a catastrophic hardware bug in the form of the Intel 14900K failures. You can't make this shit up. Anyways, we intend to do better next year and hopefully be more organized!