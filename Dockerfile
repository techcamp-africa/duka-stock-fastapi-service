FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt .

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r requirements.txt
# RUN pip install argon2_cffi
COPY  . /app

# CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000", "--reload"]