import sys
if not '64-bit' in sys.version:
    raise SystemError("motivebatch requires IronPython 64-bit.  Try running with 'ipy64' instead.")

import clr
from os import path
dll_path = r'C:\Program Files\OptiTrack\Motive\assemblies\x64\NMotive.dll'
if not path.exists(dll_path):
    raise SystemError("Cannot find required dll file: {}".format(dll_path))
clr.AddReferenceToFileAndPath(dll_path)
import NMotive

import itertools


Meters = NMotive.LengthUnits.Units_Meters
Centimeters = NMotive.LengthUnits.Units_Centimeters
Millimeters = NMotive.LengthUnits.Units_Millimeters

Quaternions = NMotive.Rotation.QuaternionFormat
for order in itertools.permutations('XYZ'):
    globals()[''.join(order)] = getattr(NMotive.Rotation, ''.join(order))


class Take(object):

    def __init__(self, fname):
        takename = fname
        if not path.split(takename)[0]:
            takename = path.join('.', takename)
        if not path.exists(takename):
            raise IOError("FileNotFound: {}".format(takename))
        self._take = NMotive.Take(takename)


    @property
    def fname(self):
        return self._take.FileName

    @property
    def frame_rate(self):
        return self._take.FrameRate

    def save(self, fname=None):
        self._take.Save() if fname else self._take.Save(fname)

    def to_csv(self, fname=None, markers=False, header=True, rotation=Quaternions, units=Meters):
        """Export Take's tracking data to CSV File."""
        if not fname:
            fname = path.splitext(self.fname)[0] + '.csv'
        exporter = NMotive.CSVExporter()
        exporter.RotationType = rotation
        exporter.WriteMarkers = markers
        exporter.WriteHeader = header
        exporter.Units = units
        exporter.Export(self._take, fname, True)

    def to_avi(self, fname=None):
        """Export Take's Video content to AVI file."""
        if not fname:
                fname = path.splitext(self.fname)[0] + '.avi'
        vid_exporter = NMotive.VideoExporter()
        vid_exporter.Export(self._take, fname, True)
