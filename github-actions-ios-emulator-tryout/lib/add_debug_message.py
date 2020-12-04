import os,sys
from pprint import pprint

def addDebugMessage(json_metadata, key, value):
  if not ('debug' in json_metadata.keys()):
    json_metadata['debug'] = {}

  json_metadata['debug'][key]=value
