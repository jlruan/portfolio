---
title: "CoMMA Lab (Zachary Kingston)"
date: 2025-01-24T00:23:20-08:00
draft: false
image: '../images/comma.jpeg'
description: "I worked on the bring-up and lab infrastructure for two new Franka Research 3 7-DOF robotic arms, and am currently developing a real-time obstacle avoidance demo. More..."
---
I was part of the lab bring-up of Franka Research 3 arms, and implemented containerization for multiple control methods with and without ROS as well as designed network and infrastructure.

I wrote a custom containerization solution as part of high performance computing infrastructure used lab-wide by using Docker and bash to streamline the bring-up process for new projects involving our Franka arms.

I'm currently working on a real-time obstacle avoidance algorithim with SIMD-generated point clouds using [VAMP](https://github.com/KavrakiLab/vamp), [OMPL](https://github.com/ompl/ompl), and [Realsense](https://github.com/IntelRealSense/librealsense/) cameras to demo at Purdue Research Expo. I'm also in the middle of writing control library binds for the arms in Python to sacrifice thread safety for accessibility.

{{< video
  src="/videos/comma.mp4"
>}}
