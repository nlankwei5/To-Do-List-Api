FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8000

CMD ["python", "TDL/manage.py", "runserver", "0.0.0.0:8000"]


