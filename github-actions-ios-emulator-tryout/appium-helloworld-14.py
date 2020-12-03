# iOS environment
import os,sys
from appium import webdriver
import base64
from time import sleep
import json
import unittest
from appium import webdriver


CURR_DIR=os.path.abspath(os.path.dirname(__file__))
SCREEN_CAPTURE_DIR='{}/screens'.format(CURR_DIR)

desired_caps = dict(
    platformName='iOS',
    platformVersion='14.1',
    automationName='xcuitest',
    deviceName='iPhone Simulator',
    # app=PATH('../../apps/UICatalog.app.zip')
    browserName='safari',
    loggingPrefs={"browser":"ALL"}
)
desired_caps["goog:loggingPrefs"]={"browser":"ALL"}

def getScreenShot(driver, sc_filename):
  img_data = driver.get_screenshot_as_base64()
  with open(sc_filename, "wb") as fh:
    fh.write(base64.urlsafe_b64decode(img_data))

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)

# class driver:
#   contexts='hello contexts'
#   def get_log(text):
#     return text

#   def get(text):
#     return ''

#   def quit():
#     return ''

#   class switch_to:
#     def context(text):
#       return text

def writeLog(filename, content):
  fo=open(filename,'w')
  fo.writelines(content)

def saveRecordingScreen(driver, video_name):
  video_rawdata = driver.stop_recording_screen()

  filepath = os.path.join(video_name)
  with open(filepath, "wb") as vd:
      vd.write(base64.b64decode(video_rawdata))

try:
  print('driver.contexts')
  print(json.dumps(driver.contexts))
  # driver.switch_to.context("WEBVIEW_chrome")

  driver.start_recording_screen()

  driver.get("https://aboutme.louislabs.com/")
  sleep(15)
  driver.switch_to.context(driver.contexts[1])
  writeLog('safariConsole_louislabs.log', json.dumps(driver.get_log('safariConsole')))

  # https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending
  driver.get('https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending');
  getScreenShot(driver, '{}/check_browser.png'.format(SCREEN_CAPTURE_DIR))



  driver.get('http://menymeny.com/manage/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/')
  sleep(30)
  getScreenShot(driver, '{}/menymeny_manage_screenshot.png'.format(SCREEN_CAPTURE_DIR))
  writeLog('safariConsole_manage.log', json.dumps(driver.get_log('safariConsole')))

  driver.get('http://menymeny.com/admin/')
  sleep(30)
  getScreenShot(driver, '{}/menymeny_admin_screenshot.png'.format(SCREEN_CAPTURE_DIR))
  writeLog('safariConsole_admin.log', json.dumps(driver.get_log('safariConsole')))

  driver.get('http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/')
  sleep(30)
  getScreenShot(driver, '{}/menymeny_food_screenshot.png'.format(SCREEN_CAPTURE_DIR))
  writeLog('safariConsole_food.log', json.dumps(driver.get_log('safariConsole')))

  # el = driver.find_element_by_accessibility_id('item')
  # el.click()


except Exception as e:
  raise e

finally:
  saveRecordingScreen(driver, './test.mp4')

  driver.quit()
  print('done')
