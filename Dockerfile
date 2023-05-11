FROM ubuntu:latest

#developper userを追加
RUN useradd -m -s /bin/bash developper
RUN apt-get update
RUN apt-get install python3 python3-pip -y


RUN pip3 install flask pipenv
#developperに変更
USER developper
WORKDIR /home/developper/code

RUN echo "if [[ -z \"\${VIRTUAL_ENV}\" ]]; then" >> ~/.bashrc && \
    echo "source \$(pipenv --venv)/bin/activate" >> ~/.bashrc && \
    echo "fi"                                    >> ~/.bashrc
# COPY Pipfile ~/code/Pipfile
COPY Pipfile Pipfile.lock ./
COPY requirements.txt ~/code/requirements.txt

RUN pipenv install --skip-lock --dev --ignore-pipfile 
RUN pipenv install --system --deploy
# --system 依存関係をシステムのPython環境にインストール
# --deploy Pipfile.lockに記述されたバージョンのパッケージが正確にインストールされることを保証
# CMD /bin/bash
CMD ["python3", "app.py"]
