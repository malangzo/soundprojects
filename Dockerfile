# step 1 : 이미지로 쓸 python 버전 명을 입력합니다.
FROM python:3.11.2-slim as build

# 필요한 기본 파일들을 설치합니다
RUN apt-get -y update \
    && apt-get -y install python3-launchpadlib \
    && apt-get -y install tzdata software-properties-common git net-tools vim curl ffmpeg

# 작업 폴더의 위치를 docker container 안의 /docker 위치로 합니다.
WORKDIR /docker

RUN git clone https://github.com/malangzo/soundprojects.git

WORKDIR /docker/soundprojects/python
# pip3 install -r 을 이용하여 requirements.txt 파일들에 있는 라이브러리들을 설치합니다.
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# docker container에게 5000번 포트를 쓸것이라고 언급해줍니다.
EXPOSE 5200

# 이제 위의 일련의 과정들로 build된 image 에서 하단의 명령어를 실행합니다.
CMD python3 -m uvicorn app:app --host 0.0.0.0 --port 5200 --reload