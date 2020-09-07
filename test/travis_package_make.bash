#!/bin/bash -xve

# Copy repository to workspace
rsync -av ./ ~/catkin_ws/src/pimouse_run_corridor/

# Bring pimouse_ros to your workspace with git clone
cd ~/catkin_ws/src/
git clone --depth=1 https://github.com/Lybfip/pimouse_ros.git
        # If depth=1 is specified, only the latest one can be cloned.

cd ~/catkin_ws
catkin_make