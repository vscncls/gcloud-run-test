from python:3.8.5-alpine

RUN apk add gcc musl-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "api.py"]
