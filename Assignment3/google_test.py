# Import the necessary modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website you want to automate
driver.get("https://www.google.com/")

# Find the search box element and enter a search term
search_box = driver.find_element("name","q")
search_box.send_keys("python selenium")

# Submit the search by pressing Enter
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(10)

# Find the first search result link and click on it
# Find the first search result link and click on it
search_result = driver.find_element("xpath","/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div[1]/a/h3")
search_result.click()
# Wait for the page to load
driver.implicitly_wait(10)

# Extract the URL of the current page
current_url = driver.current_url
print("Current URL:", current_url)

# Close the browser
driver.quit()
