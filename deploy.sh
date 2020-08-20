#!/bin/bash

# copy all files in src/
(
  cd src
  for file in ./*; do
    sudo ampy -p /dev/ttyUSB0 put "$file" "$file"
    echo "copied $file"
  done
)
