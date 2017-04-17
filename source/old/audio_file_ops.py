#!/usr/bin/python3

### DISCLAIMER
#
# this code was prototyped before finding the pysoundfile package, to make it easier, just use that...
#
###


### audio_file_ops.py
#
#   Description: functions included allow for various audio file operations 
#       (i.e. unpack_wav, pack_wav) 
#
#   Requires: numpy
#       (pip install numpy)
#
#   Tests available: python3 -m doctest audio_file_ops.py
#
#   Note useful link on WAV files: 
#       (https://web.archive.org/web/20140221054954/http://home.roadrunner.com/~jgglatt/tech/wave.htm)
###

# tmp install instructions for pending libs
# soundfile
#    sudo apt-get install python3-numpy python3-cffi libsndfile1
#    python3 -m pip install pysoundfile

import wave             # read wav file contents
import numpy as np      # return wav contents for later modifications
import scipy.io.wavfile # write wav modifications to new file
import struct           # unpack byte stream contents from wav files etc.

# global vars for convenience / testing
audioFileDir = "../Test Files/"
testOrchFile = "383929__oymaldonado__uplifting-orchestra.wav"
testGuitarFile = "ThuMar2302_40_45UTC2017.wav"
testWavFileOut = "testWavOut.wav"

# global static vars for config
# basically taken from http://www.bravegnu.org/blog/python-wave.html 
formats = [None, "B", "h", None, "l"]
offsets = [None, 128, 0, None, 0]


def unpack_wav(wavFile=""):
    """Takes a file path and returns params tuple + numpy array of audio content grouped by sample width

    >>> wavFile = audioFileDir + testGuitarFile
    >>> params, data = unpack_wav(wavFile)
    >>> f = wave.open(wavFile, 'r')
    >>> b = list(f.readframes(params.nframes))
    >>> b[-1 * params.sampwidth * params.sampwidth:]
    [112, 0, 115, 0]
    >>> data[-1 * params.sampwidth:]
    array([ 112.,  115.])
    >>> wavFile = audioFileDir + testOrchFile
    >>> params, data = unpack_wav(wavFile)
    >>> f = wave.open(wavFile, 'r')
    >>> b = list(f.readframes(params.nframes))
    >>> b[-1 * params.sampwidth * params.sampwidth:]
    [188, 255, 255, 193, 4, 0, 156, 255, 255]
    >>> data[-1 * params.sampwidth:]
    array([ 698.,  197.,  666.])
    >>> params, data = unpack_wav("./audio_file_ops.py")
    There was an error in handling the inputted WAV file
    >>> params, data
    (None, None)
    """
    # default wavFile to globally defined test file
    f = ""
    if wavFile is "":
        wavFile = audioFileDir + testGuitarFile

    try: 
        f = wave.open(wavFile, 'r')		
        params = f.getparams()
        fmat = formats[params.sampwidth]
        decr = offsets[params.sampwidth]

        # get raw audio data list of ints from bytes
        b = f.readframes(params.nframes)
		
        # then group indices according to sample size
        g = list(range(0, len(b), params.sampwidth))
        g.append(None) # ensure last element is included
        gg = [tuple((g[i], g[i+1])) for i in range(0, len(g)-1)]

        # execute summation according to idx groupings
        groupedAudioBytes = [struct.unpack(fmat, b[i[0]:i[1]])[0] for i in gg] 
        dataToUse = np.array(groupedAudioBytes) - decr
        f.close()
        return params, dataToUse

    except Exception as e:
        if f is not "":
            f.close()
        print('There was an error in handling the inputted WAV file')
        print(e)
        return None, None


def pack_wav(params, dataBySample, wavFile=""):
    """Takes a params tuple + audio content + new file path and writes to new wav, returns success status

    """
    # default wavFile to globally defined test file
    f = ""
    if wavFile is "":
        wavFile = audioFileDir + testWavFileOut

    try: 
        fmat = formats[params.sampwidth]
        incr = offsets[params.sampwidth]
        f = wave.open(wavFile, 'w')
        f.setparams(params)
        #d = [struct.pack(fmt, n) for n in dataBySample + incr]
        d = list(dataBySample + incr)
        out = struct.pack(fmat*len(d), *d)
        f.writeframes(out)
        #scipy.io.wavfile.write(wavFile, params.framerate, dataBySample.astype('>i2'))
        f.close()
        return True

    except Exception as e:
        if f is not "":
            f.close()
        print('There was an error in writing to the desired WAV file')
        print(e)
        return False

# example usage / testing:
params, data = unpack_wav(audioFileDir + testOrchFile)             # defaults to "../Test Files/ThuMar2302_40_45UTC2017.wav"
success = pack_wav(params, data, "")    # defaults to "../Test Files/testWavOut.wav"