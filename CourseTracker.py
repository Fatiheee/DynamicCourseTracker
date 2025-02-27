import requests
import time
from bs4 import BeautifulSoup

URL = "https://www.ibbmeslekfabrikasi.com/tr/kursmerkezleri/57"  # Website link here
CHECK_INTERVAL = 10                                              # Check interval (sn)
COURSE_NAME = "BARİSTA - HALKAPINAR KURS MERKEZİ"                # Course name that be followed by

def get_course_status(url, course_name):                         # Course status getting method
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <li> tags
    for li in soup.find_all("li"):
       
        # Check course name exist
        if course_name in li.get_text():
            print(li.get_text())
            a_tag = li.find("a")  # Find <a> tag
            if a_tag:
                #print(a_tag.text.strip())
                return a_tag.text.strip()                         # "KAYIT DOLDU" or "KAYIT OL"
    return None                                                   # Return when does not exist

# Save first stauts
previous_status = get_course_status(URL, COURSE_NAME)

while True:
    time.sleep(CHECK_INTERVAL)
    current_status = get_course_status(URL, COURSE_NAME)          # Save current status

    print(current_status)
