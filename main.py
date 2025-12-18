import umail    # for sending email
import network  # for WiFi connection

import urequests    # for HTTP requests
import time         # for sleep
import re           # for regular expressions

# Your network credentials
ssid = 'Your WiFi SSID'
password = 'Your WiFi Password'

# Email details
sender_email = 'yoursenderemail@gmail.com'      # sender email
sender_name = 'ESP32'                           # sender name
sender_app_password = 'yourapppassword'         # App password for email
recipient_email ='yourrecipientemail@gmail.com'  # recipient email
email_subject ='Test Email'

# Tracker definitations
URL = "https://www.ibbmeslekfabrikasi.com/tr/kursmerkezleri/57"  # Website link here
CHECK_INTERVAL = 10                                              # Check interval (sn)
COURSE_NAME = "KAHVE YAPIMI VE SUNUMU - HALKAPINAR KURS MERKEZİ" # Course name here

def connect_wifi(ssid, password):   # WiFi connection method
  #Connect to your network
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())
    
# Connect to your network
connect_wifi(ssid, password)                # call WiFi connection method

# check course status method
def get_course_status(url, course_name):    # Course status getting method
    # without BeautifulSoup
    try:
        response = urequests.get(url)
        html = response.text
        response.close()
    except:
        return None

    # Find all <li> ... </li> blocks
    li_tags = re.findall(r'(?s)<li.*?>(.*?)</li>', html)

    # Search for the li that includes the course name
    for li in li_tags:
        # Check course name exist
        if course_name in li:
            # Extract <a>...</a>
            match = re.search(r'<a[^>]*>(.*?)</a>', li)     # Extract the text inside <a> tag

            # If found, return the text inside <a> tag
            if match:
                print("a_tag:", match.group(1).strip())     # Debug print
                return match.group(1).strip()               # Return the course status text

    return None

# Save first stauts
previous_status = get_course_status(URL, COURSE_NAME)

# loop for course status
while True:
    time.sleep(CHECK_INTERVAL)
    current_status = get_course_status(URL, COURSE_NAME)          # Save current status

    # print(current_status)
    if current_status and current_status != previous_status:
        print(f"{COURSE_NAME} kursunun kayıt durumu değişti!")
        print(f"Önceki Durum: {previous_status}")
        print(f"Şu Anki Durum: {current_status}")
        previous_status = current_status
        
        # Course status has been changed
        # Send the email
        smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
        smtp.login(sender_email, sender_app_password)
        smtp.to(recipient_email)
        smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
        smtp.write("Subject:" + email_subject + "\n")
        smtp.write("Hello from ESP32")
        smtp.send()
        smtp.quit()
        
    else:
        print(f"{COURSE_NAME} kursunda değişiklik yok.")

