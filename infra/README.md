
# AWS CDK Infrastructure for Vibe Selector

## Setup

1. Create a virtual env.

    ```bash
    python3 -m venv .venv
    ```

2. Activate virtual env.

    For MacOS and Linux:

    ```bash
    source .venv/bin/activate
    ```

    For Windows:

    ```cmd
    .venv\Scripts\activate.bat
    ```

3. Install the required dependencies.

    ```bash
    pip install -r requirements/all.txt
    ```

4. Synthesize CloudFormation template for this code.

    ```bash
    cdk synth
    ```

## Useful commands

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk docs`        open CDK documentation

## Other info

* `cdk.json` file tells the CDK Toolkit how to execute your app.
* To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements/all.txt`
command.
