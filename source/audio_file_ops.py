#!/usr/bin/python3
### audio_file_ops.py
#
#   Description: functions included allow for various audio file operations 
#       (i.e. unpack_wav, pack_wav) 
#
#   Requires: numpy cffi pysoundfile
#       (sudo apt-get install python3-numpy python3-cffi libsndfile1)
#       (sudo python3 -m pip install pysoundfile)
#
#   Tests available: python3 -m doctest audio_file_ops.py
#
#   Note useful link on WAV files: 
#       (https://web.archive.org/web/20140221054954/http://home.roadrunner.com/~jgglatt/tech/wave.htm)
#
#   Note 2 old implementations available in old folder
#       (as a first attempt, python's built in wave modules were used as well as scipy and numpy)
###

import numpy as np      # return wav contents for later modifications
import soundfile as sf  # to read and write soundfiles easily

# global vars for convenience / testing
audioFileDir = "../Test Files/"
testOrchFile = "383929__oymaldonado__uplifting-orchestra.wav"
testGuitarFile = "ThuMar2302_40_45UTC2017.wav"
testWavFileOut = "testWavOut.wav"


def unpack_wav(wavFile=""):
    """Takes a file path and returns params tuple + numpy array of audio content grouped by sample width

    >>> wavFile = audioFileDir + testGuitarFile
    >>> rate, data = unpack_wav(wavFile)
    >>> rate, data.shape
    (44100, (1321976,))
    >>> wavFile = audioFileDir + testOrchFile
    >>> rate, data = unpack_wav(wavFile)
    >>> rate, data.shape
    (44100, (3361977, 2))
    >>> rate, data = unpack_wav("./audio_file_ops.py")
    There was an error in handling the inputted WAV file:
    Error opening './audio_file_ops.py': File contains data in an unknown format.
    >>> rate, data
    (None, None)
    """
    # default wavFile to globally defined test file
    if wavFile is "":
        wavFile = audioFileDir + testGuitarFile

    try: 
        data, rate = sf.read(wavFile)
        return rate, data

    except Exception as e:
        print('There was an error in handling the inputted WAV file:')
        print(e)
        return None, None


def pack_wav(rate, data, wavFile=""):
    """Takes sample rate + audio content + new file path and writes to new wav, returns success status

    >>> wavFile = audioFileDir + testGuitarFile
    >>> rate, data = unpack_wav(wavFile)
    >>> rate, data.shape
    (44100, (1321976,))
    >>> wavFile = audioFileDir + testWavFileOut
    >>> success = pack_wav(rate, data, wavFile)
    >>> success
    True
    >>> success = pack_wav(rate, data, "fakenews.py")
    There was an error in writing to the desired WAV file:
    No format specified and unable to get format from file extension: 'fakenews.py'
    >>> success
    False
    """
    # default wavFile to globally defined test file
    f = ""
    if wavFile is "":
        wavFile = audioFileDir + testWavFileOut

    try: 
        sf.write(wavFile, data, rate)
        return True

    except Exception as e:
        print('There was an error in writing to the desired WAV file:')
        print(e)
        return False

# example usage / testing:
#rate, data = unpack_wav()           # defaults to "../Test Files/ThuMar2302_40_45UTC2017.wav"
#success = pack_wav(rate, data, "")  # defaults to "../Test Files/testWavOut.wav"