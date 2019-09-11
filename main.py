#!/usr/bin/python3

import numpy as np

with open("../build-EGS_test-kit-Debug/resource11.dat", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()

print(np.frombuffer(data, np.float64))
