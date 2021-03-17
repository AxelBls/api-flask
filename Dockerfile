FROM python:3

COPY . /api

ADD run.py /
ADD wrapper.py /

RUN pip3 install flask SQLAlchemy pymysql

RUN pip freeze > requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
