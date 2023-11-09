FROM python:3.11

WORKDIR /final_project

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .