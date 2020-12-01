FROM python:3.6

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /work

CMD ["python", "main.py"]