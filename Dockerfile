FROM python:2.7
ADD . /ridho
WORKDIR /ridho
RUN pip install -r requirements.txt
EXPOSE 5000