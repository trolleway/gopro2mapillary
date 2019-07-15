FROM partlab/ubuntu-golang
MAINTAINER Artem Svetlov <trolleway@yandex.ru>
RUN apt-get update
RUN apt-get install -y python \
python-pip \
git \
ffmpeg 

RUN git clone https://github.com/JuanIrache/gopro-utils.git
WORKDIR gopro-utils

RUN export GOPATH="/gopro-utils"
RUN go get github.com/JuanIrache/gopro-utils/telemetry
RUB go get github.com/paulmach/go.geo

