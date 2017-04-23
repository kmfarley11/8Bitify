#!/usr/bin/python

import sys
import argparse
from source.audio_file_ops import *
from source.matrix_ops import *
import sounddevice as sd

# Map functions to input arguments
MODULES = {'square':create_square}

OPERATIONS = {'superimpose':superimpose,
              'convolve':convolve,
              'play':sd.play,
              'save':pack_wav,
              'plot':plot,
              '8bitify':eight_bitify}

# Argument Parsing setup
parser = argparse.ArgumentParser(description="Audio manipulation and experimentation.")
parser.add_argument('-w', '--wav',
                    help="A list of .WAV files to experiment with. Provide the path to the file.",
                    #nargs='+',
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
parser.add_argument('-b', '--bits',
                    help="Number of bits to change the resolution to. Only used when the eight_bitify operation is provided.",
                    type=int)


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

args = parser.parse_args()


# Load and generate the data
rate, data = None, None
if args.wav:
    try:
        rate, data = unpack_wav(args.wav)
        if len(data.shape) > 1:
            data = make_mono(data) # we are only prepared for mono data...
    except:
        print("Could not load file", args.wav)

generated = None
if args.module and rate and data.any():
    module, frequency, amplitude = args.module[0], args.module[1], args.module[2]
    generationFunc = MODULES[module]
    generated = generationFunc(rate, len(data), int(frequency), float(amplitude))
elif not rate or not data.any():
    print('Cannot generate a wave without an audio file to compare to. Skipping.')


# Perform operations
finalWAV = data
finalRate = rate
print(args.ops)
if args.ops:
    if data != None:
        finalWAV = data
    elif generated != None:
        finalWAV = generated
    else:
        print('No audio files provided/generated. Exiting.')
        sys.exit()

    for operation in args.ops:
        print(operation)
        operationFunc = OPERATIONS[operation]
        if operation in ('superimpose', 'convolve'):
            if generated != None:
                finalWAV = operationFunc(finalWAV, generated)
        
        elif operation in ('play') and rate and data.any():
            print("Playing...")
            try:
                sd.play(finalWAV, rate, blocking=True)
            except KeyboardInterrupt:
                sd.stop()
                print("Playback ended by user.")
        
        elif operation in ('save'):
            operationFunc(rate, finalWAV)
            print('File written')
        
        elif operation in ('plot'):
            totalTime = len(data) * rate
            t = linspace(0, totalTime, len(data))
            operationFunc(t, data)
        
        elif operation in ('8bitify'):
            if args.bits:
                finalWAV = operationFunc(data, args.bits)
            else:
                finalWAV = operationFunc(data)
