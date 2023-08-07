FROM python

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT flask run -h 0.0.0.0 -p 5000