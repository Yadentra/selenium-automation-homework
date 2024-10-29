from selenium import webdriver
from time import sleep

# Set up WebDriver (replace 'path/to/chromedriver' with the actual path of your WebDriver)
driver = webdriver.Chrome(executable_path="path/to/chromedriver")

# Open the HTML file
driver.get("file:///path/to/sample.html")  # Replace with the path to sample.html on your machine

# Locate the input field by CSS selector
input_field = driver.find_element("css selector", "#inputField")

# Type text into the input field
input_field.send_keys("Hello with CSS Selector!")

# Optional delay for observation
sleep(2)

# Locate and click the submit button using CSS selector
submit_button = driver.find_element("css selector", "#submitButton")
submit_button.click()

# Optional delay to observe the click
sleep(2)

# Close the browser
driver.quit()