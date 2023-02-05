FROM python:3.9

RUN apt-get update && apt-get install masscan

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "scanner.py" ]