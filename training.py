#!/bin/env python3
from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('input.txt')
textgen.save('montypython.hdf5')
