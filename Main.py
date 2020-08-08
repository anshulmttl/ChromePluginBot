 # @author Anshul Mittal
 # @email anshulmttl@gmail.com
 # @create date 2020-08-04 22:34:33
 # @modify date 2020-08-04 22:34:33
 # @desc [description]
 
import tkinter
import GUI
import os
import subprocess
import pyautogui
import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

window = tkinter.Tk()
gui = GUI.GUI(window)
runSession = True

def OpenBrowser():
    subprocess.Popen("C:/Users/91702/Documents/Work/Fiverr/ChromePlugin/Chrome.bat")
    #os.system("C:/Users/91702/Documents/Work/Fiverr/ChromePlugin/Chrome.bat")

def CloseBrowser():
    runSession = False
    driver.quit()
    print(numberRetries)

def SetRefreshes():
    global numberRetries
    numberRetries = 1
    numberRetries = gui.GetNumberRetries()

def ThreadFunc():
    time.sleep(2)
    print("Thread start")
    while runSession:
        time.sleep(1)
        #try:
        #    frame = driver.switch_to.frame(driver.find_element_by_name('Post'))
        #    print(frame)
        #except:
        #    print("No frame")
        handles = driver.window_handles
        print(handles)
        lElement = driver.find_element_by_xpath("//a[@id = 'FBscriptCClose']")
        lElement.click()

        driver.implicitly_wait(60)

        im = pyautogui.locateOnScreen(r'C:/Users/91702/Documents/Work/Fiverr/SourceControl/ChromePlugin/ChromePluginBot/ExtensionIcon.PNG')
        pyautogui.click(x=im[0],y=im[1],clicks=1,interval=0.0,button="left")

        driver.implicitly_wait(30)

        lElementStart = driver.find_element_by_xpath("//div[@class = 'fbe-actions fbe-button1']")
        lElementStart.click()
        numberRetries -= 1
        attr = driver.switch_to.active_element
        print(attr)
        try:
            print("Alert")
            #print(alert)
        except TimeoutException:
            print("No alert")
        #except NoAlertPresentException:
        #    print("No Alert")
        except:
            print("No alert") 

        
        

def ConnectBrowser():
    global driver
    chromeOptions = ChromeOptions()
    chromeOptions.add_experimental_option("debuggerAddress","127.0.0.1:9222")
    driver = webdriver.Chrome("C:/Users/91702/Documents/Work/Fiverr/ChromePlugin/chromedriver.exe", options=chromeOptions)
    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(60)

    th = threading.Thread(target=ThreadFunc)
    th.start()
    #WebDriverWait(driver, 60).until(EC.alert_is_present(), 'Timed out', 'confirmation popup to appear')
    #alert = driver.switch_to.alert
    #alert.accept()
    #v = pyautogui.locateOnScreen()
gui.SetCallbacks(OpenBrowser, CloseBrowser, SetRefreshes, ConnectBrowser)
window.mainloop()

#Open chrome
#chromeOptions = ChromeOptions()
#chromeOptions.add_experimental_option("debuggerAddress","127.0.0.1:9222")
#driver = webdriver.Chrome("C:/Users/91702/Documents/Work/Fiverr/ChromePlugin/chromedriver.exe", options=chromeOptions)
#print(driver.title)

#driver.find_element_by_link_text("About").click()
#print(driver.title)

#driver.find_element_by_link_text("Support").click()
#print(driver.title)

#driver.find_element_by_link_text("Download").click()
#print(driver.title)

#driver.find_element_by_link_text("Projects").click()
#print(driver.title)
#chromeOptions.add_extension('C:/Users/91702/Documents/Work/Fiverr/ChromePlugin/nbbaiinfgnhkmfpblcihfiodacnoackg.crx')
#chromeOptions.add_extension('C:/Users/91702/Documents/Work/Fiverr/ChromePlugin/ChromePlugin.crx')
#url='https://www.gmail.com'
#gmailUsername = 'anshulfreelancer2015@gmail.com'
#gmailPassword = 'Dell@123'
#driver = webdriver.Chrome("C:/Users/91702/Documents/Work/Fiverr/ChromePlugin/chromedriver.exe", options=chromeOptions)
#driver.get(url)
#driver.implicitly_wait(60)
#driver.find_element_by_id('identifierId').send_keys(gmailUsername)
#driver.find_element_by_id('identifierNext').click()

