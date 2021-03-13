#!/bin/env python3
from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.load('montypython.hdf5')
textgen.generate_to_file('output.txt', n=100)
