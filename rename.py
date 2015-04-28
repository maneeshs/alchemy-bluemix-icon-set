import os
import re

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

for filename in os.listdir("./svg/"):
	oldNamePath = "./svg/" + filename
	newNamePath = "./svg/" + filename.replace("_", "-")
	os.rename(oldNamePath, newNamePath)

