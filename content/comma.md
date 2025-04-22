---
title: "CoMMA Lab (Zachary Kingston)"
date: 2025-01-24T00:23:20-08:00
draft: false
image: '../images/comma.webp'
description: "I worked on the bring-up and lab infrastructure for two new Franka Research 3 7-DOF robotic arms, and am currently developing a real-time obstacle avoidance demo. More..."
---

I headed the lab bring-up of Franka Research 3 arms, and wrote a library used lab-wide to improve functionality of depth cameras, robotic arms, motion capture systems, and other lab equipment. I implemented real-time velocity and position trajectory with online minimum-jerk trajectory generation and am currently working on implementing a torque controller. I also designed the lab intranet and infrastructure to securely allow lab access remotely and wrote custom containerization solutions as part of high performance computing infrastructure used lab-wide by using Docker and bash to streamline the bring-up process for new projects involving our Franka arms.

Additionally, I worked on writing a real-time point cloud aggregation and transformation library for use in the lab which uses multiple Intel Realsense D435i cameras to generate a hi-res point cloud of the target area. I used this in a real-time obstacle avoidance algorithim with SIMD-generated point clouds using [VAMP](https://github.com/KavrakiLab/vamp), [Ruckig](https://github.com/pantor/ruckig), and [Realsense](https://github.com/IntelRealSense/librealsense/) cameras to demo at Purdue Research Expo.

{{< rerun version="0.22.1" url="https://jlruan.me/rerun/collision.rrd" >}}

{{< video src="/videos/comma.mp4">}}
