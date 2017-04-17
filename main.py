#!/usr/bin/python

import sys
import getopt

#HELP_ARGS = ("-h", "--help")

MODULES = {"square": lambda x: print(x)}

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:m:f:a:", ["help","input=","module=","frequency=","amplitude="])
    except:
        print("usage: python3 8bitify.py -i <wavfile> -m <module> <moduleopts>")
        sys.exit(2)

    # Init Defaults
    inputfile = "def"
    module = "def"
    is_module = False
    frequency = 100
    amplitude = 1

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(HELP)
            sys.exit()
        elif opt in ("-i", "--input"):
            if arg == "":
                print("No input file provided.")
                sys.exit(2)
            inputfile = arg
        elif opt in ("-m", "--module") and arg in MODULES:
            module = MODULES[arg]
            is_module = True
        elif opt in ("-f", "--frequency"):
            if is_module:
                frequency = arg
            else:
                print("Frequency provided with no module to use.")
        elif opt in ("-a", "--frequency"):
            if is_module:
                amplitude = arg
            else:
                print("Amplitude provided with no module to use.")
        else:
            print("Unrecognized input:", opt, "with argument", arg)

""" Some baseline for an eventual interactive console
def interactive():
    while True:
        line = input(">>> ")
        exp = parse(line)
"""

HELP = """
8Bitify: A sound file experimentation program
This package will take a .WAV file, modify it using any provided modules,
and play it back to the user.
This is intended to provide a method of experimenting with digital music.

Usage:
------
python3 8bitify.py -i <wavfile> -m <module> <moduleopts>

  WAV File*:                 The path to the sound file, saved in .WAV format
  Module:                    The alteration function to run on the .WAV file, e.g. Square

    Square:                 Superimpose a square wave across the entire .WAV
         Frequency (-f)      The frequency, in Hz, of the square wave.
         Amplitude (-a)      The amplitude of the square wave.
"""

if __name__ == "__main__":
    main(sys.argv[1:])
