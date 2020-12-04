import os,sys
from pprint import pprint
from diffimg import diff

from lib.add_debug_message import addDebugMessage

def assertSameImage(json_metadata, img_expected, img_actual,image_test_threshold=0.05, error_msg='same image is expected but diff image found', make_asserts=True):
  ''' exception if different image '''
  img_diff_result = diff(img_expected, img_actual)
  verdict = img_diff_result < image_test_threshold
  check_point_name = os.path.basename(img_actual).replace('.png','')
  DEBUG_MSG = "debug: file: {}, threshold {}, diff result {}, verdict {}".format(img_actual, image_test_threshold, img_diff_result, verdict)
  print(DEBUG_MSG)

  addDebugMessage(json_metadata,'img_actual', img_actual)
  addDebugMessage(json_metadata,'image_test_threshold', image_test_threshold)
  addDebugMessage(json_metadata,'img_diff_result', img_diff_result)
  addDebugMessage(json_metadata,'verdict', verdict)

  if make_asserts:
    assert verdict, check_point_name+' : ' +error_msg
