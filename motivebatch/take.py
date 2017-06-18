import clr
dll_path = r'C:\Program Files\OptiTrack\Motive\assemblies\x64\NMotive.dll'
clr.AddReferenceToFileAndPath(dll_path)
import NMotive

import itertools
from os import path

Meters = NMotive.LengthUnits.Units_Meters
Centimeters = NMotive.LengthUnits.Units_Centimeters
Millimeters = NMotive.LengthUnits.Units_Millimeters

Quaternions = NMotive.Rotation.QuaternionFormat
for order in itertools.permutations('XYZ'):
    globals()[''.join(order)] = getattr(NMotive.Rotation, ''.join(order))


class Take(object):

    def __init__(self, fname):
        self._take = NMotive.Take(fname)

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
