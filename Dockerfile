FROM python:3.6-slim

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt ./

RUN pip3.6 install -r requirements.txt

COPY app.py ./

EXPOSE 8001

CMD ["python3.6", "app.py"]
