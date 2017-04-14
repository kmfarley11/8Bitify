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
            bitify_help()
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
    
    print(inputfile)
    print(module)
    print(is_module)
    print(frequency)
    print(amplitude)

def bitify_help():
    print("8Bitify: A sound file experimentation program")
    print("This package will take a .WAV file, modify it using any provided modules, and play it back to the user.")
    print("This is intended to provide a method of experimenting with digital music.")
    print()
    print("Usage: ")
    print("------")
    print("python3 8bitify.py -i <wavfile> -m <module> <moduleopts>")
    print()
    print("  WAV File*:                 The path to the sound file, saved in .WAV format")
    print("  Module:                    The alteration function to run on the .WAV file, e.g. Square")
    # TODO: build this from the module
    print("     Square:                 Superimpose a square wave across the entire .WAV")
    print("         Frequency (-f)      The frequency, in Hz, of the square wave.")
    print("         Amplitude (-a)      The amplitude of the square wave.")
    print()
    print("Supported Modules: ")
    for entry in MODULES:
        print(" ", entry)

if __name__ == "__main__":
    main(sys.argv[1:])
