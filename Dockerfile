FROM ubuntu:latest

#developper userを追加
RUN useradd -m -s /bin/bash developper
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip3 install flask
#developperに変更
USER developper
CMD /bin/bash
