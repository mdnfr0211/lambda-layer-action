# lambda-layer-action

GitHub Action for deploying Lambda Layer code

## Usage

```bash
{
    "functions": [],
    "layers": [
        {
            "layer_name": "test-layer",
            "runtime": [
                "nodejs18.x"
            ],
            "zip_file_name": "layer.zip",
            "layer_arch": [
              "x86_64"
            ]
        }
    ]
}
```

```bash
name: Deploy

on:
  push:
    branches:
      - main

jobs:
  Deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Assume IAM role
        uses: aws-actions/configure-aws-credentials@v3
        with:
          role-to-assume: <ROLE-TO-ASSUME>
          aws-region: <AWS-REGION>
        
      - name: deploy lambda layer
        uses: mdnfr0211/lambda-layer-action@v1
        env:
          RUNNER_ID: 1
          ARTIFACT_BUCKET: <ARTIFACT-BUCKET>
          LAMBDA_CONFIG_FILE: <PATH-OF-JSON-FILE>

```

The Lambda layer code(zip) should be structured under the artifact bucket in the format: `layer/<runner-id>/function.zip`.

## License

[MIT](https://choosealicense.com/licenses/mit/)
