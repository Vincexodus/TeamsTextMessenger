from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TE
import json
import time

edge_path = "./browser_drivers/msedgedriver.exe"
chrome_path = "./browser_drivers/chromedriver.exe"

# Read info file
with open("info.json") as i:
  j_file = json.load(i)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrome_path, options=options)

# driver = webdriver.Edge(executable_path= edge_path)

# Message structure
# receiver = ""
intake_code = j_file["message_info"]["intake_code"]
course_type = j_file["message_info"]["course_type"]
course_name = j_file["message_info"]["course_name"]
survey_type = j_file["message_info"]["survey_type"]
survey_topic = j_file["message_info"]["survey_topic"]
form_link = j_file["message_info"]["form_link"]

message = f"Hey, my group and I from {intake_code} {course_type} are currently conducting an {survey_type} for our {course_name} assignment. "+\
          f"We would appreciate the help of yours at spending a short 5 mins to fill up the survey about {survey_topic}. "+\
          f"Much appreciated! Thank you in advance and have a great day! {form_link} "

# Navigate to microsoft team login browser
driver.get("https://www.microsoft.com/en-my/microsoft-teams/group-chat-software")
driver.implicitly_wait(4)

# Press sign in button
driver.find_element_by_xpath("//*[@class='c-button f-secondary ow-slide-in ow-slide-in-2 xs-ow-mr-0 ow-mt-10 ow-txt-trans-upper ow-bvr-signin']").click()
driver.implicitly_wait(2)

# Switch to second tab
driver.switch_to.window(driver.window_handles[1])

# Enter email credentials
email_input = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#i0116")))
email_input.send_keys(j_file["credentials"]["email"])
email_input.send_keys(Keys.RETURN)

# Enter password credentials
pw_input = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#i0118")))
pw_input.send_keys(j_file["credentials"]["password"])
time.sleep(10)

# Click sign in button
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='idSIButton9']"))).click()

# Sometimes login might fail
# Click yes button
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='button ext-button primary ext-primary']"))).click()
print("Logging into Teams")

try:
  # Press try again button if login failed
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ts-btn ts-btn-primary oops-button']"))).click()
except:
  pass

# Navigate the chat icon button on side panel
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "app-bar-86fcd49b-61a2-4701-b771-54728cd291fb"))).click()


start_tp = int(j_file["receivers"]["start_tp"])
end_tp = int(j_file["receivers"]["end_tp"])
curr_receiver = ""

for _ in range(end_tp-start_tp + 1):
  curr_tp = "{0:06}".format(start_tp)
  curr_receiver = f"TP{curr_tp}"

  # for loop
  # Navigate new chat icon button
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable\
    ((By.XPATH, "//button[@class ='ts-sym app-icons-fill-hover left-rail-header-button']"))).click()

  # Input to user search text box
  user_search = WebDriverWait(driver, 40).until(EC.presence_of_element_located\
    ((By.XPATH, "//input[@class ='ts-search-input ng-pristine ng-valid ng-empty ng-touched']")))
  user_search.send_keys(curr_receiver)

  print(f"Selecting user {curr_receiver}")
  time.sleep(3)
  # Select first user if exists
  user_search.send_keys(Keys.RETURN)
  time.sleep(2)
  user_search.send_keys(Keys.RETURN)

  # # Press dismiss button
  # WebDriverWait(driver, 20).until(EC.element_to_be_clickable\
  #   ((By.XPATH, "//button[@class ='action-button']"))).click()

  # Locate textbox element and insert inputs
  message_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='cke_1_contents']/div/div")))
  message_input.send_keys(message)

  # Send the message 
  message_input.send_keys(Keys.ENTER)
  print(f"message sent to {curr_receiver}")
  start_tp +=1 