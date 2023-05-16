import os

class CheckDirectory:
    def __init__(self, directory):
        try:
            if not os.path.exists(directory):
                print('Directory doesn\'t exist. Creating directory...')
                os.makedirs(directory)
                print('Directory created successfully.')
            else:
                print('Directory already exists.')
        except FileNotFoundError:
            print('Error: Directory path is invalid.')
        except PermissionError:
            print('Error: Permission denied.')
