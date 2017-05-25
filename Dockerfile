FROM python:2.7
RUN mkdir /code
WORKDIR /code
ADD ./code/requirements.txt /code/
RUN pip install -r requirements.txt
