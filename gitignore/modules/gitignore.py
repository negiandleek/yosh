import os
import subprocess;

path = os.path.join(os.pardir)
from constants import *
print("import gitignore");

def gitignore(args):
	cmd = "find ./ -name __init__.py";
	result = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).stdout.readlines();

	result_list = [item.rstrip() for item in result]

	cmd = "find ./ -name __pycache__";
	result = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).stdout.readlines();

	result_list = [item.rstrip() for item in result]
	print(result_list);

	return SHELL_STATUS_RUN
