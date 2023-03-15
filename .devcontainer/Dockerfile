# Ubuntuの公式コンテナを軸に環境構築
# 22.04ではaptからpython3.8が入っていなかったので20.04で固定する
FROM ubuntu:20.04

# インタラクティブモードにならないようにする
ARG DEBIAN_FRONTEND=noninteractive

# タイムゾーンを日本に設定
ENV TZ=Asia/Tokyo

# 起動シェルをshからbashに変更
SHELL ["/bin/bash", "-c"]

# 各種パッケージのインストール
RUN apt update && \
    apt -f install -y && \
    apt install -y \
    wget \
    bzip2 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgl1-mesa-dev \
    git \
    curl \
    unzip \
    file \
    xz-utils \
    python3 \
    python3-pip \
    time \
    tzdata \
    tree 

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb &&\
    rm google-chrome-stable_current_amd64.deb

RUN apt-get -y install fonts-ipafont-gothic

# ユーザー名を指定
ARG USERNAME=user
ARG GROUPNAME=user

# UID, GIDはidコマンドで確認し，ログインユーザーのUID, GIDを指定する
ARG UID=1000
ARG GID=1000

# ユーザーを作成
RUN groupadd -g $GID $GROUPNAME && \ 
    useradd -m -u $UID -g $GID -s /bin/bash $USERNAME

# 初期ユーザーの変更
USER $USERNAME

# workdirの指定
WORKDIR /work

# pathを通す
ENV PATH="$PATH:/home/user/.local/bin"

# requirements.txtをコピー
COPY requirements.txt ${PWD}

# pythonパッケージのインストール
RUN pip3 install --no-cache-dir -U pip setuptools wheel \
    && pip3 install --no-cache-dir -r /work/requirements.txt
