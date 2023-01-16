FROM python:3-alpine

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# RUN pip install Flask

EXPOSE 80

CMD ["python",  "simpleapp.py"]
