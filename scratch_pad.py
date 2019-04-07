import os, json, sys, mutagen

this_dir = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(this_dir)
import mut_keys 

MUSIC_BASE = os.path.join('D:\\', 'Shaun', 'Music', 'iTunes', 'iTunes Media', 'Music')

file_extensions = ['.m4a', '.m4p', '.m4v', '.mp3', '.mpg', '.wav']

file_list = []
file_json = []

with open(os.path.join(this_dir, 'file_error_list.txt'), 'r') as f:
	file_list = f.readlines()

def scanFiles(filepath):
	artists_set = set()
	no_artist = []
	for roots, dirs, filenames in os.walk(filepath):
		for filename in filenames:
			if os.path.splitext(filename)[1] in file_extensions:
				file_path = os.path.join(roots, filename)
				try:
					tag = mutagen.File(file_path, easy=True)
					for artist in tag['artist']:
						artists_set.add(artist)
				except:
					no_artist.append(file_path)
	return artists_set, no_artist
	
def scan_err_files(filepath):
	name = os.path.split(filepath)[1]
	file_dict = {}
	file_dict['name'] = name.strip()
	file_dict['path'] = filepath.strip()
	try:
		tags = mutagen.File(filepath.strip(), easy=True)
		file_dict['field_count'] = len(tags)
	except:
		file_dict['field_count'] = 0
	return file_dict

def out_to_json(filelist=file_list):
	filejson = []
	for i, line in enumerate(filelist):
		filejson.append(scan_err_files(line))
	return filejson

