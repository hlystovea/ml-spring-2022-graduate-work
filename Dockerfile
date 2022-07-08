FROM ubuntu
LABEL maintainer="hlystovea@gmail.com"
WORKDIR /sr_bot
RUN apt update
RUN apt install python3.10
RUN apt install -y git
RUN git clone https://github.com/tensorlayer/srgan.git
RUN apt install -y wget
RUN mkdir ./srgan/models && \
    wget -O ./srgan/models/g.npz "https://drive.google.com/uc?export=download&id=1GlU9At-5XEDilgnt326fyClvZB_fsaFZ" && \
    wget -O ./srgan/models/d.npz "https://drive.google.com/uc?export=download&id=1RpOtVcVK-yxnVhNH4KSjnXHDvuU_pq3j"
RUN apt install -y ffmpeg libsm6 libxext6
RUN mkdir ./local_wheels && \
    wget -O ./local_wheels/tensorflow-2.7.0-cp38-cp38-linux_x86_64.whl "https://github.com/lakshayg/tensorflow-build/releases/download/tf2.7.0-ubuntu20.04-py3.8.10/tensorflow-2.7.0-cp38-cp38-linux_x86_64.whl"
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .