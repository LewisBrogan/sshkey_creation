import os

class CheckPubKey:
    def __init__(self, directory):
        pub_key_path = os.path.join(directory, 'id_rsa')
        if os.path.exists(pub_key_path):
            print('File exists inside ssh directory.')
        else:
            print('File does not exist inside ssh directory.')
            print('Generating RSA key pair...')
            command = f'ssh-keygen -t rsa -f {pub_key_path}'
            exit_code = os.system(command)
            if exit_code != 0:
                print('Error occurred during RSA key pair generation.')
            else:
                print('RSA key pair generated successfully.')
