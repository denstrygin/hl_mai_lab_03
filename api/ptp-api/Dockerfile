FROM python:3.10-slim

RUN apt-get update && apt-get install -y libmariadb-dev gcc

WORKDIR /usr/src/app
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8002
CMD ["uvicorn", "ptp:app", "--host", "0.0.0.0", "--port", "8002"]