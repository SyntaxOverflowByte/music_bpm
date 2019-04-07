"""
This script is intended to pull down tempo, bpm, of all iTunes songs
Each song will be the instance of a song class
It will use the mutagen library to pull the metadata
It will then use the getsongbpm API to try to pull down the tempo, BPM
"""

import os, sys, json, mutagen, argparse

# Import keys for mutable library
this_dir = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(this_dir)
import mut_keys 

MUSIC_BASE = os.path.join('D:\\', 'Shaun', 'Music', 'iTunes', 'iTunes Media', 'Music')
acdc_path = os.path.join(MUSIC_BASE, 'AC_DC', 'Warning! High Voltage')
song1_path = os.path.join(acdc_path, os.listdir(acdc_path)[0])
file_extensions = ['.m4a', '.m4p', '.m4v', '.mp3', '.mpg', '.wav']

# TODO import urllib3 and get API key
# TODO use urllib3 and API key to look up bpm

class Song(object):

	"""

	Song Class that manipulates the metadata of Song objects.
	Instantiate with the path to the song.

	"""

	num_of_songs = 0
	
	def __init__(self, path):
		self.path = path
		self.song = None
		self.tempo = None
		self.title = None
		self.album = None
		self.artist = None
		self.flag = False
		
		Song.num_of_songs += 1
	
	def load_song(self):
		try:
			self.song = mutagen.File(self.path, easy=True)
			return True
		except:
			self.flag = True
			return False
	
	def getSongAttribs_Title(self):
		if self.flag:
			return
		else:
			try:
				self.title = self.song['title']
			except:
				self.title = 'Unknown Title'

	def getSongAttribs_Album(self):
		if self.flag:
			return
		else:
			try:
				self.album = self.song['album']
			except:
				self.album = 'Unknown Album'
	
	def getSongAttribs_Artist(self):
		if self.flag:
			return
		else:
			try:
				self.artist = self.song['artist']
			except:
				self.artist = 'Unknown Artist'
	
	def get_dict(self):
		"""
		Return a dictionary of the Song object with:
		filepath, title, album, artist, year, genre, album_artist
		"""
		song_dict = {}
		song_dict['filepath'] = self.path
		song_dict['title'] = self.title
		song_dict['album'] = self.album
		song_dict['artist'] = self.artist
		return song_dict
	
	def song_info(self):
		return '{} by {}'.format(self.title, self.artist)

	def load_attributes(self):
		if self.flag:
			return
		self.getSongAttribs_Album()
		self.getSongAttribs_Artist()
		self.getSongAttribs_Title()
		return True


# def main(filepath):
	# all_songs = []
	# for roots, dirs, filenames in os.walk(filepath):
		# for filename in filenames:
			# if os.path.splitext(filename)[1] in file_extensions:
				# full_path = os.path.join(roots, filename)
				# song_dict = Song()
				# song_dict.load_song(full_path)
				# all_songs.append(song_dict)
	# return all_songs


if __name__ == '__main__':
#	file_path = args.directory
	songs = main(MUSIC_BASE)
	with open('D:\\Shaun\\Music\\iTunes\\iTunes Media\\Music\\outfile.json', 'w') as f:
		json.dump(f, songs)
	
#	if args.outfile is not None:
#		with open(args.outfile, 'w') as f:
#			json.dump(f, songs)
	