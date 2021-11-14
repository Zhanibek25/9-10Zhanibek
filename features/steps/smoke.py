from behave import *
import time
from selenium.common.exceptions import NoSuchElementException

@given('teststep')
def login(context):
    context.driver.implicitly_wait(20)
    #сли выходит: We are for safety!
    try:
        context.driver.find_element_by_android_uiautomator('new UiSelector().text("We are for safety!")')
        context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/button2").click()
    except NoSuchElementException:
        print('OK: Safety popup not found')

    # Если выходит: system ui isn't responding
    try:
        context.driver.find_element_by_id("android:id/aerr_wait").click()
    except NoSuchElementException:
        print('OK: no problem with system ui is not responding')

    context.driver.implicitly_wait(20)

    #изменение языка
    context.driver.find_element_by_id('kz.homecredit.ibank.debug:id/llChangeLang').click()
    context.driver.find_element_by_id('kz.homecredit.ibank.debug:id/tvLangTwo').click()

    context.driver.find_element_by_android_uiautomator('new UiSelector().text("Вход")').click()

    context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/cvUsernameInput").send_keys("7087341574")
    custom_button = context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/customButton")
    custom_button.click()

    context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/etInputText").send_keys("12345678")
    custom_button.click()

    time.sleep(2)
    try:
        context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/ovOtpCode").send_keys('0000')
    except NoSuchElementException:
        print('OK: Otp not called')

    context.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]').click()

    time.sleep(3)
    #context.driver.find_element_by_android_uiautomator('new UiSelector().text("Открыть дебетную карту")').click()
    context.driver.find_element_by_id('kz.homecredit.ibank.debug:id/customButton').click()
    time.sleep(2)

    context.driver.find_element_by_id('kz.homecredit.ibank.debug:id/relativeLayout').send_keys("йцукен")
    time.sleep(2)
    try:
        context.driver.find_element_by_android_uiautomator('new UiSelector().text("Алматы")').click()
    except NoSuchElementException:
        print('OK: region selection did not come out, do not have to select the region')

    context.driver.find_element_by_android_uiautomator('new UiSelector().text("Улица")').send_keys("Al-Farabi")
    time.sleep(2)
    context.driver.find_element_by_android_uiautomator('new UiSelector().text("№ дома")').send_keys("71")
    time.sleep(2)
    context.driver.find_element_by_android_uiautomator('new UiSelector().text("Квартира")').send_keys("12")
    time.sleep(2)
    context.driver.find_element_by_id('kz.homecredit.ibank.debug:id/customButton').click()


    print('test ok')
