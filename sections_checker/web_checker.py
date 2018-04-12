from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from private import pid
from mailer import Mailer

# Email for updates

# Use the headless version of Chrome.
options = webdriver.ChromeOptions()
options.set_headless()

mailer = Mailer()

# Use Chrome
driver = webdriver.Chrome(chrome_options=options)

# Go to sections webpage
driver.get("https://sections.ucsd.edu/default.aspx")
assert "ACMS" in driver.title
elem = driver.find_element_by_name("pid_TextBox")
elem.clear()
elem.send_keys(pid)

select = Select(driver.find_element_by_name('course_DropDownList'))
select.select_by_value("620")
elem.send_keys(Keys.RETURN)
section_title = "CSE 15L - SoftwareTools&TechniquesLab - Weekly Lab Section [SP18]"

lab_path = '//*[@id="DataGrid1"]/tbody/tr[7]/td[2]/span'
#lab_path = '//*[@id="DataGrid1"]/tbody/tr[4]/td[2]/span'

lab_section =  driver.find_element_by_xpath(lab_path)

lab_enrollment = lab_section.get_attribute('innerHTML')
lab_enrollment_num = int(lab_enrollment)

print("Lab Enrollment: {}".format(lab_enrollment_num))

if(lab_enrollment_num == 0):
    print("Lab is still waitlisted")
    mailer.send_full()
elif(lab_enrollment_num >= 1):
    print("LAB HAS SPACE")
    mailer.send_available()
else:
    print("ERROR")

#sleep(5)
driver.close()


