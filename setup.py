import os
import re
from glob import glob

from setuptools import find_packages, setup

data_files = []
for root, dirs, files in os.walk("configuration"):
    data_files.append(
        (os.path.relpath(root, "configuration"), [os.path.join(root, f) for f in files])
    )

# declare your scripts:
# scripts in bin/ with a shebang containing python will be
# recognized automatically
scripts = []
for fname in glob("bin/*"):
    with open(fname, "r") as fh:
        if re.search(r"^#!.*python", fh.readline()):
            scripts.append(fname)

with open("requirements.txt") as f:
    dependencies = [line for line in f]

