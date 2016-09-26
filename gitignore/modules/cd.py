import os
import sys

path = os.path.join(os.pardir)
from constants import *

print("import cd");
def cd(args):
	
    os.chdir(args[0])

    return SHELL_STATUS_RUN