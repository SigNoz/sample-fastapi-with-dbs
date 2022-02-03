FROM python:3.8

# open port
EXPOSE 5000

# add requirements
COPY . /

# install requirements
RUN pip install -r /requirements.txt
RUN opentelemetry-bootstrap --action=install

# Init command
CMD ["opentelemetry-instrument", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--host", "0.0.0.0"]
