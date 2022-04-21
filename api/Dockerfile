FROM python:3.10

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

EXPOSE 80

COPY ./backend /backend

WORKDIR /backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]