WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PORT=8000

CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT} app:app"]
