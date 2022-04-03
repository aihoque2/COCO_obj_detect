"""
pull_data.py

get our coco dataset
"""

import os

os.system("cd coco")
os.system("make")
os.system("python3 ./setup.py install")
    