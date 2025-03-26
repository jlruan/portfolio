---
title: "CoMMA Lab (Zachary Kingston)"
date: 2025-01-24T00:23:20-08:00
draft: false
image: '../images/comma.webp'
description: "I worked on the bring-up and lab infrastructure for two new Franka Research 3 7-DOF robotic arms, and am currently developing a real-time obstacle avoidance demo. More..."
---

I headed the lab bring-up of Franka Research 3 arms, and implemented containerization for multiple control methods with and without ROS as well as designed network and infrastructure. I also wrote custom containerization solutions as part of high performance computing infrastructure used lab-wide by using Docker and bash to streamline the bring-up process for new projects involving our Franka arms.

Additionally, I worked on writing a real-time point cloud aggregation and transformation server for use in the lab which uses multiple Intel Realsense D435i cameras to generate a hi-res point cloud of the target area.

{{< rerun version="0.22.1" url="https://jlruan.me/rerun/comma.rrd" >}}

I'm currently working on a real-time obstacle avoidance algorithim with SIMD-generated point clouds using [VAMP](https://github.com/KavrakiLab/vamp), [OMPL](https://github.com/ompl/ompl), and [Realsense](https://github.com/IntelRealSense/librealsense/) cameras to demo at Purdue Research Expo. I'm also in the middle of writing control library binds for the arms in Python to sacrifice thread safety for accessibility.

{{< video
  src="/videos/comma.mp4"
>}}
