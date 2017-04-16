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

import wave
import numpy as np
import scipy.io.wavfile
import math
import struct

audioFileDir = "../Test Files/"
testOrchFile = "383929__oymaldonado__uplifting-orchestra.wav"
testGuitarFile = "ThuMar2302_40_45UTC2017.wav"
testWavFileOut = "testWavOut.wav"


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

        # get raw audio data list of ints from bytes
        b = f.readframes(params.nframes)
		
        # then group indices according to sample size
        g = list(range(0, len(b), params.sampwidth))
        g.append(None) # ensure last element is included
        gg = [tuple((g[i], g[i+1])) for i in range(0, len(g)-1)]

        # execute summation according to idx groupings
        groupedAudioBytes = [struct.unpack('h', b[i[0]:i[1]])[0] for i in gg] 
        dataToUse = np.array(groupedAudioBytes)
        f.close()
        return params, dataToUse

    except Exception as e:
        if f is not "":
            f.close()
        print('There was an error in handling the inputted WAV file')
        return None, None


def pack_wav(params, dataBySample, wavFile=""):
    """Takes a params tuple + numpy array of audio content grouped by sample width + new file path and writes to new wav, returns success status

    """
    # default wavFile to globally defined test file
    f = ""
    if wavFile is "":
        wavFile = audioFileDir + testWavFileOut

    try: 
        #f = wave.open(wavFile, 'w')		
        #f.setparams(params)
        #d = [struct.pack('h', n) for n in dataBySample]
        scipy.io.wavfile.write(wavFile, params.framerate, dataBySample.astype('>i2'))
        #f.close()
        return True

    except Exception as e:
        if f is not "":
            f.close()
        print('There was an error in writing to the desired WAV file')
        return False

params, data = unpack_wav()
success = pack_wav(params, data, "")