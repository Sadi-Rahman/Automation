from selenium import webdriver
import csv


gecko_path = "C:/Users/User/Desktop/CSPA/gecko/geckodriver.exe"

driver = webdriver.Firefox(executable_path=gecko_path)

url = "https://www.google.com/"
driver.get(url)
page_data = {}

for i in range(10):
    current_url = driver.current_url
    
    load_time = driver.execute_script("return (window.performance.timing.loadEventEnd - window.performance.timing.navigationStart);")

    if current_url not in page_data:
        page_data[current_url] = {'load_time': load_time, 'test_count': 1}
    else:
        page_data[current_url]['load_time'] += load_time
        page_data[current_url]['test_count'] += 1
    
    print(f"{current_url}: {load_time} ms (test {page_data[current_url]['test_count']})")

    driver.get(url)

driver.quit()