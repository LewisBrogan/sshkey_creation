# SSH Key Creation

## Description

This project provides a Python script for checking the existence of a directory and generating an RSA key pair within that directory if it doesn't already exist. It consists of two classes: `CheckDirectory` and `CheckPubKey`.

The `CheckDirectory` class checks if a directory exists and creates it if it doesn't. It handles potential errors such as an invalid directory path or permission denied.

The `CheckPubKey` class verifies the presence of a specific file inside the SSH directory. If the file is not found, it generates an RSA key pair using the `ssh-keygen` command. It also handles errors that may occur during the key pair generation process.

## Prerequisites

- Python 3.x: Install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Installation

1. Clone the repository: 
        
        git clone https://github.com/LewisBrogan/ssh-key-creation.git

2. Navigate to the project directory:
        
        cd ssh-key-creation

3. Create and activate a virtual environment (optional but recommended):

        python3 -m venv venv
        source venv/bin/activate


4. Install project dependencies:

        pip install -r requirements.txt


## Usage

`python3 ./main.py` if you want to keep the default directory as `$HOME/./ssh` else:

1. Open the `main.py` file in a text editor.

2. Modify the `directory` variable to specify the desired SSH directory. By default, it is set to `$HOME/./ssh`, expanding the `$HOME` environment variable.

3. Save the changes.

4. Run the `main.py` script:

        python main.py


The script will check if the directory exists and create it if necessary. It will then verify the presence of the RSA key file inside the SSH directory and generate one if needed.

## Unit Tests

1. Ensure that the project dependencies are installed (refer to the Installation section).

2. Run the unit tests:

        python -m unittest discover -s testing


The unit tests cover the functionality of the `CheckDirectory` and `CheckPubKey` classes, including various scenarios such as directory creation, file existence, and key pair generation. The test results will be displayed in the console.
