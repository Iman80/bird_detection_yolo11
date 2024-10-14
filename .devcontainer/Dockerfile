FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04 AS build

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# setting timezone
RUN ln -fs /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

RUN apt-get update && \
    apt-get install -y build-essential \
    software-properties-common \
    curl \
    git \
    wget \
    python3.10 \
    python3.10-dev \
    python3.10-distutils \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3.10 get-pip.py && rm get-pip.py

# # Install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt


CMD ["/bin/bash"]