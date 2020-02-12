#!/bin/bash

# copy all files in src/
for file in src/*; do
    sudo ampy -p /dev/ttyUSB0 put "$file"
    echo "copied $file"
done