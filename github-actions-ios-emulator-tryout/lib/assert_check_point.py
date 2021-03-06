import os,sys

from time import sleep
from random import randrange

from lib.assert_image import assertSameImage
from lib.add_debug_message import addDebugMessage

LIB_DIR=os.path.dirname(__file__)
TEST_HOME=os.path.abspath(LIB_DIR+'/..')
ACTUAL_SC_DIR=os.path.abspath(TEST_HOME+'/actual')
EXPECTED_SC_DIR=os.path.abspath(TEST_HOME+'/expected')

def takeScreenshot(driver, sc_filename):
    driver.save_screenshot(sc_filename)

def getRandomString():
  return randrange(1,100)

def getActualScreenshotPath(test_number):
  random_string = getRandomString()
  # return 'tests/UI_test/functional/smoke_test_remote_parallel/actual/{}_sc.png'.format(test_number)
  return ACTUAL_SC_DIR+'/{}_sc_{}.png'.format(test_number, random_string)

def getExpectedScreenshotPath(test_number):
  return EXPECTED_SC_DIR+'/{}_sc.png'.format(test_number)

def assertCheckPoint(json_metadata, driver ,check_point_name, error_message, fail_threshold=0.039, sleep_s=0.5, make_asserts=True):
  sleep(sleep_s)
  actual_screenshot_path=getActualScreenshotPath(check_point_name)
  expected_screenshot_path=getExpectedScreenshotPath(check_point_name)


  takeScreenshot(driver, actual_screenshot_path)

  assertSameImage(json_metadata, expected_screenshot_path, actual_screenshot_path,fail_threshold,  error_message, make_asserts)

  # os.remove(actual_screenshot_path)


def assertHelloworld(check_point_name):
  # assert False, getActualScreenshotPath(check_point_name)
  # assert False,"hello fail"
  pass
