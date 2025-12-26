# ESP32 Dynamic Course Tracker & Email Notifier by using Thonny IDE

This project monitors a course availability status on a website and sends an **email notification** when the course status changes (e.g. from *“KAYIT DOLDU”* to *“KAYIT OL”*).

The project demonstrates **three different implementations**:
- ESP32 (Arduino / C++) – Email sending only
- Python (PC) – Course availability detection
- ESP32 (MicroPython) – Full solution: detection + email notification

---

## 📁 Project Structure
.
├── main.cpp
├── main.py
├── course_check.py
└── README.md

main.cpp
Written for ESP32 used by Arduino Framework.
For unnderstanding the SMTP and testing it.

course_check.py
Python code works on PC.
Track the course status in dedicated Web page.

main.py
The standalone main **MicroPython** file from this repo, and execute on ESP32.
- Set up Wi-Fi Connection
- Check the course status from Web page
- Send E-mail when status is changed

# Read the instructions




