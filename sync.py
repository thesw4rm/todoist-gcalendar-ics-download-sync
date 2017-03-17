from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.chrome.options import Options
import time
os.environ["webdriver.chrome.driver"] = "chromedriver.exe"

options = webdriver.ChromeOptions()
#options.add_argument("--user-data-dir=C:\\Users\\ytpil\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome("chromedriver.exe", chrome_options = options) #firefox_binary=FirefoxBinary("../Drivers/geckodriver.exe")
driver.get("https://calendar.google.com")

try:
    driver.execute_script("""
            document.getElementById("Email").value = "[Email]";
            setTimeout(function(){},5000);
                document.querySelector("#next").click();

        """)
    time.sleep(1)
    driver.execute_script("""
        document.querySelector("#username").value = "[AUTH_STUFF]";
        document.querySelector("#password").value = "[AUTH_STUFF]";
        document.querySelector("button[type='submit']").click();
    """)
    time.sleep(2)
    driver.execute_script("""
        window.location = "https://calendar.google.com/calendar/render#settings-calendars_9";


    """)
    time.sleep(3)
    driver.execute_script("""
        document.querySelector("a.actionlink[href='javascript:void(0)']").click();
    """)
    import urllib.request
    url = "https://ext.todoist.com/export/ical/todoist?user_id=6515030&ical_token=e0c8b20f7df06c937a5e81bf266c0dcec60f0ee20562467c48b90b78ac584f45&r_factor=2103"
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    with open("[ICS_FILE]", "w") as f:
        f.write(data)
    driver.find_element_by_name("filename").send_keys(os.getcwd() + "/[ICS_FILE]")
    driver.find_element_by_name("import").click()
except Exception as e:
    raise e
