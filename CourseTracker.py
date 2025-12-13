import requests
import time
from bs4 import BeautifulSoup

# without BeautifulSoup library
import urequests
import time
import re

URL = "https://www.ibbmeslekfabrikasi.com/tr/kursmerkezleri/57"  # Website link here
CHECK_INTERVAL = 10                                              # Check interval (sn)
COURSE_NAME = "KAHVE YAPIMI VE SUNUMU - HALKAPINAR KURS MERKEZİ" # Course name that be followed by

# Course status getting method
def get_course_status(url, course_name):                         
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, "html.parser")

    # # Find all <li> tags
    # for li in soup.find_all("li"):
       
    #     # Check course name exist
    #     if course_name in li.get_text():
    #         # print(li.get_text())
    #         a_tag = li.find("a")  # Find <a> tag
    #         if a_tag:
    #             #print(a_tag.text.strip())
    #             return a_tag.text.strip()                         # "KAYIT DOLDU" or "KAYIT OL"
    # return None                                                   # Return when does not exist
    
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
            match = re.search(r'<a[^>]*>(.*?)</a>', li)

            # If found, return the text inside <a> tag
            if match:
                print("a_tag:", match.group(1).strip())
                return match.group(1).strip()

    return None

# Save first stauts
previous_status = get_course_status(URL, COURSE_NAME)

while True:
    time.sleep(CHECK_INTERVAL)
    current_status = get_course_status(URL, COURSE_NAME)          # Save current status

    # print(current_status)
    if current_status and current_status != previous_status:
        print(f"{COURSE_NAME} kursunun kayıt durumu değişti!")
        print(f"Önceki Durum: {previous_status}")
        print(f"Şu Anki Durum: {current_status}")
        previous_status = current_status
    else:
        print(f"{COURSE_NAME} kursunda değişiklik yok.")
