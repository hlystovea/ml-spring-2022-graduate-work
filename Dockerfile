FROM tensorflow/tensorflow
LABEL maintainer="hlystovea@gmail.com"
WORKDIR /sr_bot
RUN apt update
RUN apt install -y git
RUN git clone https://github.com/tensorlayer/srgan.git
RUN apt install -y wget
RUN mkdir ./srgan/models && \
    wget -O ./srgan/models/g.npz "https://drive.google.com/uc?export=download&id=1GlU9At-5XEDilgnt326fyClvZB_fsaFZ" && \
    wget -O ./srgan/models/d.npz "https://drive.google.com/uc?export=download&id=1RpOtVcVK-yxnVhNH4KSjnXHDvuU_pq3j"
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .