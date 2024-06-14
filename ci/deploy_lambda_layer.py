import boto3
import json
import os
import logging

from botocore.exceptions import ClientError

lambda_config_file = os.getenv("LAMBDA_CONFIG_FILE")
artifact_bucket = os.getenv("ARTIFACT_BUCKET")
runner_id = os.getenv("RUNNER_ID")

lambda_client = boto3.client('lambda')


def read_function_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def publish_layer(layer_data):
    try:
        for layer in layer_data:
            layer_name = layer["layer_name"]
            runtime = layer["runtime"]
            zip_file_name = layer["zip_file_name"]

            response = lambda_client.publish_layer_version(
                LayerName=layer_name,
                Content={
                    'S3Bucket': artifact_bucket,
                    'S3Key': f"layer/{runner_id}/{zip_file_name}",
                },
                CompatibleRuntimes=runtime,
                CompatibleArchitectures=layer.get("layer_arch", ["x86_64"])
            )
    except ClientError as e:
        logging.error(f"Error Publishing Layer Version: {e}")
        raise


if __name__ == "__main__":
    layer_data = read_function_data(lambda_config_file)["layers"]
    publish_layer(layer_data)
