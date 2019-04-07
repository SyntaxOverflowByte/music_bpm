import os, argparse

parser = argparse.ArgumentParser(description='Program to get song metadata')
#parser.add_argument('directory', action='store', default='D:\\Shaun\\Music\\iTunes\\iTunes Media\\Music')
parser.add_argument('--outfile', '-o', action='store', required=False)
args = parser.parse_args()