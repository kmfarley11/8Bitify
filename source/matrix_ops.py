#!/usr/bin/python3
### matrix_ops.py
#
#   Description: functions included allow for various audio file operations
#       (i.e. eight_bitify, superimpose_square)
#
#   Requires: numpy
#       (sudo apt-get install python3-numpy)
#
#   Tests available: python3 -m doctest matrix_ops.py
#
###

import numpy as np      # matrix ops via numpy: audio data of shape (num_data, num_channels)
from scipy import signal

# global vars for convenience / testing
audioFileDir = "../Test Files/"
testOrchFile = "383929__oymaldonado__uplifting-orchestra.wav"
testGuitarFile = "ThuMar2302_40_45UTC2017.wav"
testWavFileOut = "testWavOut.wav"


def eight_bitify(data):
    """ 
    takes numpy matrix of audio data, returns modded numpy data

    >>> t = np.array([1, 2, -5, 4, 5, 6, 120, 355, -500])
    >>> t
    array([   1,    2,   -5,    4,    5,    6,  120,  355, -500])
    >>> t.shape
    (9,)
    >>> result = eight_bitify(t)
    >>> result.shape
    (9,)
    >>> result
    array([  -1.81102362,    1.55511811,   -5.17716535,    1.55511811,
              4.92125984,    4.92125984,  119.37007874,  355.        , -500.        ])

    """
    # get max / min, then set discrete points for resolution depicted
    moddedData = np.array(data)
    hi = np.max(data)
    lo = np.min(data)
    bins = np.linspace(lo, hi, num=255)

    # discretize the data into our new resolution set of points (less noticeable for small data...)
    bidxs = np.digitize(moddedData, bins, right=False)
    moddedData = bins[bidxs-1]

    # return discretized data
    return moddedData


def create_square(rate, sampleLength, frequency=100, amplitude=0.05):
    """
    Create and return a NumPy square wave with the given parameters.

    Rate is the sample rate, in samples per second. sampleLength is num samples in data
    Therefore, create (rate/frequency) samples of amplitude before switching polarity.

    >>> create_square(500, 10, frequency=500, amplitude=1)
    array([ 1., -1., -1.,  1.,  1., -1., -1.,  1.,  1., -1.])
    
    """
    totalTime = sampleLength * rate

    t = np.linspace(0, totalTime, sampleLength) # this creates t indicating seconds with the same dimensions as incoming data

    square = signal.square(2 * np.pi * frequency * t) * amplitude

    return square


def superimpose(wave1, wave2):
    """
    Superimpose two numpy arrays.

    >>> a = np.array([1,1,1])
    >>> b = np.array([2,2,2])
    >>> superimpose(a,b)
    array([ 3.,  3.,  3.])

    >>> c = np.array([1])
    >>> d = np.array([2,2,2])
    >>> superimpose(d,c)
    array([ 3.,  2.,  2.])
    """
    assert type(wave1) == np.ndarray
    assert type(wave2) == np.ndarray

    if len(wave1) > len(wave2):
        zeros = np.zeros(len(wave1) - len(wave2))
        wave2 = np.concatenate((wave2, zeros))
    elif len(wave2) > len(wave1):
        zeros = np.zeros(len(wave2) - len(wave1))
        wave1 = np.concatenate((wave1, zeros))

    return wave1.astype(np.float64) + wave2.astype(np.float64)


def convolve(wave1, wave2, mode='full', method='auto'):
    """
    convolute one wave on top of another
    
    needs doctests and verification for what we are trying to do with it
    """
    
    return signal.convolve(wave1, wave2, mode, method)


def split_channel(data):
    rows, cols = data.shape
    return data[:,0], data[:,1]


def make_mono(data):
    return (data.sum(axis=1)/2).astype('int16')


def plot(t, array):
    import matplotlib.pyplot as plt
    plt.plot(t, array)
    plt.show()
