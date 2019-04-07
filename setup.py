import os, json, sys, mutagen

this_dir = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(this_dir)

from music_bpm import *

acdc_path = os.path.join(MUSIC_BASE, 'AC_DC', 'Warning! High Voltage')
gb_path = os.path.join(MUSIC_BASE, 'Garth Brooks', )
song1_path = os.path.join(acdc_path, os.listdir(acdc_path)[0])