import os,sys
from pprint import pprint

from lib.add_debug_message import addDebugMessage

def test_json_metadata(json_metadata):
  json_metadata['hello']='WORLD'
  # json_metadata['debug']['hello']='hellodebug'
  addDebugMessage(json_metadata,'hello', 'hellodebug')
  print(json_metadata)
