#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    get_full_name = s.split(" ")
    return(" ".join(i.capitalize() for i in get_full_name))

if __name__ == '__main__':
