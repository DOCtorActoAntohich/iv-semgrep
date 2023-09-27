import os
from pathlib import Path

# ruleid: os-path-is-forbidden
file_bad = os.path.join("folder", "file.txt")

# ruleid: os-path-is-forbidden
absolute_bad = os.path.abspath(".")

# ruleid: os-path-is-forbidden
os.path.exists("config/death.yaml")

# ruleid: os-path-is-forbidden
os.path.isdir("config")
