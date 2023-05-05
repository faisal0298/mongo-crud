FROM python:3.10.2

WORKDIR /home/diycam/Desktop/mongocrud

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

# COPY . .

CMD ["uvicorn", "routes:app", "--host", "0.0.0.0", "--port", "8000"]
