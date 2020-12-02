
FROM python:3.6-slim
WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD pytest
ENTRYPOINT python app.py


