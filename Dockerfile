FROM python:3

COPY . /api

RUN pip freeze > requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "/root/Documents/api-flask/run.py"]
