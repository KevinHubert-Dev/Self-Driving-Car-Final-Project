# Self driving Car - Nanodegree Final

Capstone Project for Udacity Self-Driving Car Nanodegree

## Introducing

The goal of the project is to capsulate the whole gained knowledge of the "Self driving car"-Nanodegree course and use it to control a real-driving-car on a test-track.
The project uses the so called [Roboter-Operating-System](https://en.wikipedia.org/wiki/Robot_Operating_System) (short: ROS) which is a framework mostly used in the fields of robotics and autonomous systems.


## Team
The project was proudly developed by the following contributors (in alphabetical order).

| Adam Gyarmati | Gaurav A. | Kevin Hubert | Lukas Leonard Köning |
|:---:|:---:|:---:|:---:|
| [![Adam_GitHubImage](https://avatars1.githubusercontent.com/u/40522904?v=4&s=400)](https://github.com/gyadam)    | [![Gaurav_GitHubImage](https://avatars0.githubusercontent.com/u/33591870?s=400&v=4)](https://github.com/gasatig) | [![Kevin_GitHubImage](https://avatars3.githubusercontent.com/u/34512569?s=400&v=4)](https://github.com/KevinHubert-Dev)  | [![LukasLeonard_GitHubImage](https://avatars2.githubusercontent.com/u/6058766?s=400&v=4)](https://github.com/LukasLeonardKoening)  |

** Click on the picture of the respective person to view GitHub-Profile.

---

## Setup

We recommend to use the Docker container provided by Udacity. To do so first build the docker container and then run the docker file:

```sh
# Build
docker build . -t capstone

# Run
docker run -p 4567:4567 -v $PWD:/capstone -v /tmp/log:/root/.ros/ --rm -it capstone
```

To run the server-program on your local enviroment:

``` sh
# Clone this repository
git clone <Repository>
cd <Repository-Folder>

# Install requirements
pip install -r requirements.txt

# Build project and source ros-enviroment-variables
cd ros
catkin_make
source ./devel/setup.bash

# Launch
roslaunch ./launch/styx.launch
```

To see the result you need to download the [simulator](https://github.com/udacity/CarND-Capstone/releases) (we have tested it using version 1.3) and run it. Ensure that port 4567 is free to used.

---

## Referencens and additional reading material
The following references/links/papers gave us inspiration and helped us to solve the project.
- [Short description 1](https://udacity.com)
- [Short description 2](https://udacity.com)
- [Short description 3](https://udacity.com)

More about Nanodegree-Program at Udacity can be found here:
[Become a Self-Driving Car Engineer](https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013)


---

## License

Copyright (c) 2020 Adam Gyarmati, Gaurav A., Kevin Hubert, Lukas Leonard Köning

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