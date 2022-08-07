from selenium import webdriver
from sendsms import NotificationManager
import datetime

sms = NotificationManager()
chrome_path = "/home/prasanth/chromedriver/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://earthquake.usgs.gov/earthquakes/map/?extent=21.00247,-128.67188&extent=52.45601,-61.30371")

search_city = driver.find_elements_by_css_selector(".details h6")
result_list = [item.text for item in search_city]

magnitude_result = driver.find_elements_by_class_name("callout")
magnitude_list = [item.text for item in magnitude_result]

time_of_quake = driver.find_elements_by_css_selector(".details .subheader .time")
time_list = [item.text for item in time_of_quake]
print(time_list)

for item in range(0, len(magnitude_list)):
    if float(magnitude_list[item]) > 5.5:
        country_with_quake_location = result_list[item]
        spilt = country_with_quake_location.split(",")
        #print(spilt)
        try:
            country = spilt[1]
            if country[1:] == "Japan":
                print(country)
                sms.send_sms(f"Please Take caution.there is a earthquake in {country}.With intensity greater than magnitude of 5 at the location {spilt[0]}")
        except IndexError:
            country = spilt[0]
            if country[1:] == "Japan":
                print(country)
                sms.send_sms(f"please be careful. there is a earthquake in {country}.With intensity greater than magnitude of 5")
