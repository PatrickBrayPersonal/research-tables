import os

PROJECT = "your_project"
PACKAGE = "your_package"
DESCRIPTION = "__description__"
AUTHORS = "__authors__"
BUCKET = "ml-template"
FILE_TYPES = [".toml", ".lock", ".md", ".txt", ".py"]


def replace_string_in_files(directory, old_string, new_string):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            # Get the file extension
            _, file_extension = os.path.splitext(filename)
            if file_extension.lower() in FILE_TYPES:
                filepath = os.path.join(dirpath, filename)
                with open(filepath, "r") as file:
                    filedata = file.read()
                # Replace the target string
                filedata = filedata.replace(old_string, new_string)
                # Write the file out again
                with open(filepath, "w") as file:
                    file.write(filedata)
    print(
        f"All instances of '{old_string}' have been successfully replaced with '{new_string}' in {directory}."
    )


def rename_directory(old_name, new_name):
    # check if the directory exists
    if os.path.isdir(old_name):
        try:
            # rename the directory
            os.rename(old_name, new_name)
            print(f"Directory {old_name} has been successfully renamed to {new_name}.")
        except OSError as e:
            print(f"Error: {e.strerror}")
    else:
        print(f"The directory {old_name} does not exist.")


new_project = input("Enter your project name: ")
rename_directory(PROJECT, new_project)
replace_string_in_files(new_project, PROJECT, new_project)
new_package = input("Enter your package name: ")
rename_directory(f"{new_project}/{PACKAGE}", f"{new_project}/{new_package}")
replace_string_in_files(new_project, PACKAGE, new_package)
new_description = input("Enter your package description: ")
replace_string_in_files(new_project, DESCRIPTION, new_description)
new_author = input("Enter your author name(s): ")
replace_string_in_files(new_project, AUTHORS, new_author)
new_bucket = input("Enter your s3 bucket name: ")
replace_string_in_files(new_project, BUCKET, new_bucket)
