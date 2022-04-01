## Robotics Engineer Internship role Task
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
---

## Contributor

[Aditya Jadhav](https://github.com/iamjadhav)
Graduate Student of M.Eng Robotics at University of Maryland.

## Overview of Instructions

This workspace contains two packages namely "sensors" and "data_processor" which have modules that generate random data from "temp", "speed", and "laser" sensors and display the average of the latest 20 
data entries. The file structure, building and executing instructions are given below. There are three python packages which contribute in this task. The sensors and data_processor packages are used for generating random sensor data, averaging the latest 20 entries and displaying them on console with the help of several publisher and subscriber nodes. The average_bringup package has the launch files that 
are used to launch the necessary nodes to achieve the task. To view the average runtime, the visualization instructions are also given.

## Technology Used

* Ubuntu 20.04 LTS
* Python Programming Language
* ROS2 Foxy
* Colcon Build System
* CMake Build System
* Sphinx documentation system


## License 

```
MIT License

Copyright (c) 2022 Aditya Jadhav

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
```


## How to build

Before building the workspace, add following lines to your bashrc,

```
source /opt/ros/foxy/setup.bash
source ~/ros2_ws/install/setup.bash
```

Execute the following commands after unzipping the workspace in your home directory,
```
cd ros2_ws
colcon build
. install/setup.bash
```

1) To view Temperature Sensor Average, open a separate terminal and execute,

```
ros2 launch average_bringup temp_average_launch.launch.py 
```

And to visualize runtime Temperature Average, open a separate terminal and execute,

```
ros2 run rqt_plot rqt_plot /average_temp/data
```

2) To view Speed Sensor Average, open a separate terminal and execute,
```
ros2 launch average_bringup speed_average_launch.launch.py 
```

And to visualize runtime Speed Average, open a separate terminal and execute,

```
ros2 run rqt_plot rqt_plot /average_speed/data
```

3) To view Laser Sensor Average, open a separate terminal and execute,
```
ros2 launch average_bringup laser_average_launch.launch.py
```

And to visualize runtime Distance Average, open a separate terminal and execute,

```
ros2 run rqt_plot rqt_plot /average_distance/data
```


## Documentation

1) To view Sensors package documentation, Open the index.html from the following directory,
```
cd ~/ros2_ws/src/sensors/sensors/docs/_build/html/
```

2) To view Data_processor package documentation, Open the index.html from the following directory,
```
cd ~/ros2_ws/src/data_processor/data_processor/docs/_build/html
```

3) To view Average_bringup package documentation, Open the index.html from the following directory,
```
cd ~/ros2_ws/src/average_bringup/launch/docs/_build/html
```


