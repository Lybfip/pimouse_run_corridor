#!/bin/bash -xve

#sync add make
rsync -av ./ ~/catkin_ws/src/pimouse_run_corridor/
cd ~/catkin_ws
catkin_make