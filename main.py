#!/usr/bin/python

import sys
import argparse
import numpy as np
from source.audio_file_ops import *
from source.matrix_ops import *

# Map functions to input arguments
MODULES = {'square':create_square}

OPERATIONS = {'superimpose':superimpose,
              'convolve':convolve,
              'play':play,
              'save':pack_wav}

# Argument Parsing setup
parser = argparse.ArgumentParser(description="Audio manipulation and experimentation.")
parser.add_argument('-w', '--wav',
                    help="A list of .WAV files to experiment with. Provide the path to the file.",
                    nargs='+',
                    metavar='filename')
parser.add_argument('-m', '--module',
                    help="The module and parameters to be used in generating audio waveforms, in the form of [module name, frequency, amplitude]",
                    nargs=3,
                    metavar='param')
parser.add_argument('-o', '--ops',
                    help="List of operations to perform on the waveforms",
                    nargs='+',
                    metavar='op',
                    choices=list(OPERATIONS.keys()))

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

args = parser.parse_args()


# Load and generate the data
rates,datas = [],[]
if args.wav:
    for filename in args.wav:
        try:
            rate, data = unpack_wav(filename)
            #rates += [rate]
            #datas += [data]
        except:
            print("Could not load file", filename)

generated = None
if args.module:
    module, frequency, amplitude = args.module[0], args.module[1], args.module[2]
    generationFunc = MODULES[module]
    generated = generationFunc(frequency, amplitude)

# Perform operations
finalRate = rate
print(finalRate)
if args.ops:
    if data.any():
        finalWAV = data
    elif generated:
        finalWAV = generated
    else:
        print('No audio files provided/generated. Exiting.')
        sys.exit()

    for operation in args.ops:
        operationFunc = OPERATIONS[operation]
        if operation in ('superimpose', 'convolve'):
            for data in datas[1:]:
                finalWAV = operationFunc(finalWAV, data)

            if generated:
                finalWAV = operationFunc(finalWAV, generated)

            #finalRate = max(rates)
        else:
            print(operationFunc)
            operationFunc(rate, data)
