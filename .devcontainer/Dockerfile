# Reference: https://www.allisonthackston.com/articles/vscode-docker-ros2.html
FROM althack/ros2:foxy-gazebo 

# ** [Optional] Uncomment this section to install additional packages. **
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
&& apt-get -y install --no-install-recommends ros-foxy-robot-localization ros-foxy-slam-toolbox ros-foxy-navigation2 ros-foxy-nav2-bringup\
#    #
#    # Clean up
&& apt-get autoremove -y \
&& apt-get clean -y \
&& rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

# Set up auto-source of workspace for ros user
ARG WORKSPACE
RUN echo "if [ -f ${WORKSPACE}/install/setup.bash ]; then source ${WORKSPACE}/install/setup.bash; fi" >> /home/ros/.bashrc