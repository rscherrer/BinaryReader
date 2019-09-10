#!/usr/bin/python3

import struct
import numpy as np

print(struct.pack('4f', 1.0, 2.0, 3.0, 4.0))
print(np.frombuffer(b'\x00\x00\x80?\x00\x00\x00@\x00\x00@@\x00\x00\x80@', np.float32))

with open("record.dat", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(data)

print(np.frombuffer(data, np.float64))
