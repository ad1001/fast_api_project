FROM python:latest
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt 
COPY . /code
CMD ["flask", "run", "--host", "0.0.0.0"]