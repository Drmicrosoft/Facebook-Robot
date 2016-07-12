#Drmicrosoft - Omar Okasha
#Python
 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
 
 
 def init_email () :
      return " YOUR EMAIL HERE "
 def init_password () :
      return " YOUR PASSWORD HERE "
 
 
from ssds import init_email
from ssds import init_password
 
 
email = init_email()
password = init_password()
#print email , password
xxx = raw_input (" What Do you want to post to your Facebook ? \n")
 
 
 
driver = webdriver.Firefox()
actions = ActionChains(driver)
 
driver.get("http://www.facebook.com")
time.sleep(2)
#elem = driver.find_element_by_title("email")
 
 
 
 
 
elem = driver.find_element_by_name("email")
elem = driver.find_element_by_id("email")
elem = driver.find_element_by_xpath("//input[@id='email']")
 
 
try :
  x = driver.find_element_by_xpath('//div[@class="_52lr fsm fwn fcg"]')
  print "omar"
except :
  print "error"
 
 
 
elem.send_keys(email)
elem = driver.find_element_by_name("pass")
 
elem.send_keys(password)
 
elem.send_keys(Keys.RETURN)
time.sleep(4)
driver.get("https://www.facebook.com")
time.sleep(4)
 
 
 
try :
  elem = driver.find_element_by_xpath("//textarea[@placeholder=\"What's on your mind?\"]")
 
  print "omar1"
except :
  print "error"
 
time.sleep(4)
 
elem.send_keys(xxx)
 
 
 
 
 
try :
  elem = driver.find_element_by_xpath("//button[@value=\"Post\"]")
 
   
  actions = ActionChains(driver)
  actions.click(elem)
  print "done"
  print "Action"
except :
  print "error"
 
 
try :
  elem = driver.find_element_by_xpath("//button[@class=\"_42ft _4jy0 _ej1 _4jy3 _4jy1 selected _51sy\"]")
 
  actions = ActionChains(driver)
  actions.click(elem)
  print "done" 
  print "Action1"
except :
  print "error"
 
 
 
 
 
#elem.send_keys(Keys.RETURN)
 
 
 
 
try :
  elem = driver.find_element_by_xpath("//button[@class=\"_42ft _4jy0 _ej1 _4jy3 _4jy1 selected _51sy\"]")
  print "l"
  elem.send_keys(Keys.RETURN)
 
  print "Return 1"
 
except :
  print "error"
 
 
 
try :
  elem = driver.find_element_by_xpath("//button[@value=\"Post\"]")
  print "l"
  elem.send_keys(Keys.RETURN)
 
  print "Return 2"
 
except :
  print "error"
 
try :
  elem = driver.find_element_by_xpath("//button[@value=\"Post\"]")
  print "l"
  elem.submit()
 
  print "submit 1"
except :
  print "error"
 
 
try :
  elem = driver.find_element_by_xpath("//button[@class=\"_42ft _4jy0 _ej1 _4jy3 _4jy1 selected _51sy\"]")
  print "l"
  elem.submit()
 
  print "Submit 2"
except :
  print "error"
 
 
 
try :
  print driver.text
except :
  print "error hacked"
 
try :
  print driver.content
except :
  print "error hacked"
 
try :
  print driver.context_diff
except :
  print "error hacked"
 
try :
  print driver.contextmanager
except :
  print "error hacked"
 
try :
  print driver.read
except :
  print "error hacked"
 
 
 
 
x = input ("omar");
 
for x in z :
  time.sleep(1)
  driver.get(x)
  time.sleep(10)
 
  try :
    elem = driver.find_element_by_id("u_0_z")
    print " omar"
    actions = ActionChains(driver)
    actions.click(elem)
    print "clicked"
    time.sleep(10)
    elem.send_keys(Keys.RETURN)
    time.sleep(10)
  except :
    print "error "
    time.sleep(1)
   
  try :
    elem = driver.find_element_by_xpath("//a[@class=\"_42ft _4jy0 _4jy4 _517h _51sy\"]")
    print " oamr"
    actions = ActionChains(driver)
    actions.click(elem)
    print "clicked"
    time.sleep(10)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
  except :
    print "error"
 
 
 
  print " done with message "
  print "start typing "
  message = '''Hello XProgrammer .. This is Omar A.Okasha ..
I am the Founder of the Xcompany that you had done with its form ..
 
We have some questions to you ..
 
From where are you ?
 
What is the best language you speak ?
 
If you from Egypt .. Will you be with us from first day ?
 
What is the best time to start ?
 
If there some fees in the first time like 200 Pounds per month .. can you accept that with first few months ?
 
What is the best programming language you prefer ?
 
Do you prefer to share your knowledge in a specific field ?
 
 
Tell me about your experience ?
Thank you for you interesting ...
Have a nice day ..
Omar Okasha'''
 
  print "\n \n " , message ,"\n \n "
 
 
  try :
    elem = driver.find_element_by_xpath("//div[@title=\"Type a message...\"]")
    time.sleep(10)
    print " oamr"
    elem.send_keys(message)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(10)
  except :
    print "error "
    
