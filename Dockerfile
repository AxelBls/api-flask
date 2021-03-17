FROM python:3

COPY . /api

ADD run.py /
ADD wrapper.py /

RUN pip3 install flask SQLAlchemy

RUN pip freeze > requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "./run.py"]
