FROM python:3.10
LABEL maintainer="hlystovea@gmail.com"
WORKDIR /sr_bot
RUN apt update
RUN apt install -y git
RUN git clone https://github.com/tensorlayer/srgan.git
RUN apt install -y wget
RUN mkdir ./srgan/models && \
    wget -O ./srgan/models/g.npz "https://drive.google.com/uc?export=download&id=1GlU9At-5XEDilgnt326fyClvZB_fsaFZ" && \
    wget -O ./srgan/models/d.npz "https://drive.google.com/uc?export=download&id=1RpOtVcVK-yxnVhNH4KSjnXHDvuU_pq3j"
RUN apt install -y ffmpeg libsm6 libxext6
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN wget "https://drive.google.com/file/d/12nQ9F9hFddU_z8l2Qzkbjkv9E7-VoIVA/view?usp=sharing"
RUN pip3 install --ignore-installed --upgrade tensorflow-2.7.0-cp38-cp38-linux_x86_64.whl
COPY . .