FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install -r ci/requirements.txt

ENTRYPOINT ["python", "/app/ci/deploy_lambda_layer.py"]