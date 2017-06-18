# motivebatch

## Description

A simpler OOP IronPython wrapper interface for converting Optitrack Motive Take files to other formats.
Works using IronPython and Optitrack's NMotive SDK.

I found the Motive Batch Processor to be a bit clunky for my purposes, and in
the process of exploring the library made a more Pythonic interface for the part I needed
at the time--Exporting to CSV and AVI files.

## Installation

Currently, requires IronPython 64-bit and NMotive 64-bit and Windows, with the NMotive.dll
file stored at:

 **C:\Program Files\OptiTrack\Motive\assemblies\x64\NMotive.dll**

 *Note*: If anyone can show me how to do auto-dll detection during the setup process so this tool
 and others like it can find the dll automatically, I please message me or send a pull request--I'd be
 grateful to learn how to do that!

```
  git clone https://www.github.com/neuroneuro15/motivebatch
  cd motivebatch
  ipy64 setup.py install --user
```


 ## Examples

### Converting a Motive Take File's Tracking Data to CSV

```python
  from motivebatch import Take
  take = Take('myfile.tak')
  take.to_csv('myfile.csv', header=True)
```

Changing default rotation type and units:
```python
  from motivebatch import Take, Centimeters, XYZ
  take = Take('myfile.tak')
  take.to_csv(rotation=XYZ, units=Centimeters)
```

### Converting a Motive Take File's Video Data to AVI

```python
  from motivebatch import Take
  take = Take('myfile.tak')
  take.to_avi('myfile.avi')
```

