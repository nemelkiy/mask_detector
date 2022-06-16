FROM --platform=linux/amd64 python:3.8

RUN apt-get update \
            && apt-get upgrade -y \
            && apt-get autoremove \
            && apt-get autoclean \
            && mkdir app \
            && apt-get install -y python3-opencv \
            && apt install -y netcat

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --upgrade pip \
            && pip install --no-cache-dir -r requirements.txt
COPY /model/retinaface_resnet50_2020-07-20-f168fae3c.zip /root/.cache/torch/hub/checkpoints/
COPY . /app/

CMD ["python", "app.py"]