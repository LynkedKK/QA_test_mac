#!/usr/bin/env python3
import os,sys
from appium import webdriver
import base64
from time import sleep
import json
import unittest
from appium import webdriver

from lib.assert_check_point import assertCheckPoint
from lib.assert_check_point import assertHelloworld

CURR_DIR=os.path.abspath(os.path.dirname(__file__))
SCREEN_CAPTURE_DIR='{}/screens'.format(CURR_DIR)

desired_caps = dict(
    platformName='iOS',
    platformVersion='12.4',
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

def writeLog(filename, content):
  fo=open(filename,'w')
  fo.writelines(content)

def test_IOS14():
  ERROR_MESSAGE='The device should auto redirect to line up page'

  driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
  driver.implicitly_wait(30)

  try:
    driver.start_recording_screen()

    driver.get("https://aboutme.louislabs.com/")
    sleep(15)
    driver.switch_to.context(driver.contexts[1])
    writeLog('safariConsole_louislabs.log', json.dumps(driver.get_log('safariConsole')))
    assertCheckPoint(driver, 'TID_001_1_IOS12', ERROR_MESSAGE)

    # https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending
    driver.get('https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending');
    getScreenShot(driver, '{}/check_browser.png'.format(SCREEN_CAPTURE_DIR))
    assertCheckPoint(driver, 'TID_001_2_IOS12', ERROR_MESSAGE)


    driver.get('http://menymeny.com/manage/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/')
    sleep(5)
    getScreenShot(driver, '{}/menymeny_manage_screenshot.png'.format(SCREEN_CAPTURE_DIR))
    writeLog('safariConsole_manage.log', json.dumps(driver.get_log('safariConsole')))
    assertCheckPoint(driver, 'TID_001_3_IOS12', ERROR_MESSAGE)

    driver.get('http://menymeny.com/admin/')
    sleep(5)
    getScreenShot(driver, '{}/menymeny_admin_screenshot.png'.format(SCREEN_CAPTURE_DIR))
    writeLog('safariConsole_admin.log', json.dumps(driver.get_log('safariConsole')))
    assertCheckPoint(driver, 'TID_001_4_IOS12', ERROR_MESSAGE)

    driver.get('http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/')
    sleep(5)
    getScreenShot(driver, '{}/menymeny_food_screenshot.png'.format(SCREEN_CAPTURE_DIR))
    writeLog('safariConsole_food.log', json.dumps(driver.get_log('safariConsole')))
    assertCheckPoint(driver, 'TID_001_5_IOS12', ERROR_MESSAGE)

    # # el = driver.find_element_by_accessibility_id('item')
    # # el.click()



    browser=''
    # assertCheckPoint(browser, 'TID_001_1', ERROR_MESSAGE)


  finally:
    print('done')
