from invoke import task
import os
import json
from copy import deepcopy
import ast


BUCKET = ""
CODE_DIRS = ["scripts", "notebooks", "tests", "table_extract"]


@task
def sync_to_s3(c, folder: str="data"):
    """
    Sync a folder to s3
    """
    os.system(f"aws s3 sync {folder}/ s3://{BUCKET}/{folder}/")


@task
def sync_from_s3(c, folder: str="data"):
    """
    Sync a folder from s3
    """
    os.system(f"aws s3 sync s3://{BUCKET}/{folder}/ {folder}/")


def convert_files_to_launch_json(
    directory: str,
    endswith: str = ".yaml",
    more_args: list = [],
    config_add: bool = False
):
    launch_options = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(file)
            if file.endswith(endswith):
                filepath = os.path.join(root, file)
                option = {
                    "name": filepath,
                    "type": "python",
                    "request": "launch",
                    "program": filepath,
                    "console": "integratedTerminal",
                    "justMyCode": True,
                    "args": more_args,
                }
                if config_add:
                    for file in files:
                        if file.endswith(".yaml"):
                            new_option = deepcopy(option)
                            fn = file[:-5]
                            new_option["args"] += ["--config-name", fn]
                            new_option["name"] += f" {fn}"
                            launch_options.append(new_option)
                else:
                    launch_options.append(option)
    return launch_options

@task
def debug(c):
    """
    Update the launch.json with your executable scripts and configs
    """
    output_directory = r".vscode"
    launch_options = []
    launch_options += convert_files_to_launch_json(
        "scripts/", endswith=".py"
    )
    launch_options += convert_files_to_launch_json(
        "config/", endswith=".py", config_add=True
    )
    current_file = {
        "name": "Python: Current File",
        "type": "python",
        "request": "launch",
        "program": "${file}",
        "console": "integratedTerminal",
        "justMyCode": True,
    }
    launch_options.append(current_file)
    launch_json = {"version": "0.2.0", "configurations": launch_options}
    os.makedirs(output_directory, exist_ok=True)
    with open(os.path.join(output_directory, "launch.json"), "w") as outfile:
        json.dump(launch_json, outfile, indent=2)
    print("successfully updated launch.json")


@task(debug)
def format(c):
    """
    Run code autoformatting with black, isort, and flake8
    """
    for dir in CODE_DIRS:
        os.system(f"isort {dir}")
        os.system(f"black {dir}")
        os.system(f"flake8 {dir} --ignore=E501")

@task(format)
def docs(c):
    """
    Update the documentation directory and update gh-pages from master
    """
    os.system("pdoc table_extract -o docs")
    os.system("ghp-import -p -o docs")
