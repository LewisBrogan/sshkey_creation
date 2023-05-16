from check_directory import CheckDirectory
from check_pub_key import CheckPubKey 

import os

if __name__ == "__main__":
    directory = os.path.expandvars("$HOME/./ssh")
    
    check_dir = CheckDirectory(directory)
    check_pub_key = CheckPubKey(directory)
