#!/bin/env python3
import os
import re
import tempfile
import urllib.request

root = 'https://www.intriguing.com/mp/'
index = root + 'scripts.php'
file_pattern = re.compile(r'_scripts/(\w+)\.php')
exclusions = ['epguide', 'livecrdt', 'albums', 'mpfaq']
encoding = 'iso-8859-1'
data_directory = 'input'
data_file = 'input.txt'
line_pattern = re.compile(r'[^<>]+')

# Ensure data directory exists
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

# Find all script links on index page
with urllib.request.urlopen(index) as indexfile:
    for line in indexfile.readlines():
        match = file_pattern.search(line.decode(encoding))
        if match and match.group(1) not in exclusions:
            # Download file
            source = root + match.group(0)
            file_name = os.path.join(data_directory, match.group(1))
            print(f'Downloading {source} to {file_name}')
            urllib.request.urlretrieve(source, file_name)

# Strip blank lines and html tags from input data, aggregating into one file
files = map(lambda name: os.path.join(data_directory, name), os.listdir(data_directory))
with open(data_file, 'w') as aggregate:
    for file_name in files:
        print(f'Appending {file_name}')
        with open(file_name, 'rb') as f:
            aggregate.writelines(line.decode(encoding).strip() + '\n' \
                for line in f if line_pattern.match(line.decode(encoding).strip()))
