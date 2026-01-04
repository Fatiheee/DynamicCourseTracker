# ESP32 Dynamic Course Tracker & Email Notifier by using Thonny IDE

This project monitors a course availability status on a website and sends an **email notification** when the course status changes (e.g. from *“KAYIT DOLDU”* to *“KAYIT OL”*).

The project demonstrates **three different implementations**:
- ESP32 (Arduino / C++) – Email sending only
- Python (PC) – Course availability detection
- ESP32 (MicroPython) – Full solution: detection + email notification

---

## 📁 Project Structure

```text
.
├── main.cpp
├── main.py
├── course_check.py
└── README.md
```
```main.cpp```

Written for ESP32 used by Arduino Framework.
For understanding the SMTP and testing it.

```course_check.py```

Python code works on PC.
Track the course status in dedicated Web page.

```main.py```

The standalone main **MicroPython** file from this repo, and execute on ESP32.
- Set up Wi-Fi Connection
- Check the course status from Web page
- Send E-mail when status is changed

# Read the instructions

```
1) Sign up an e-mail account(e.g. Google) for sending e-mail
2) Generate an app password for the e-mail account
3) Install Thonny IDE and open it
4) Connect the ESP32 to your PC and select it in Thonny
5) Flash the MicroPython firmware to the ESP32 using esptool.py (via Thonny)
6) Lastly, upload ## main.py ## from this repo
```

# Usage
For Usage just wait to e-mail that ESP32 will send.

**Do not forget that the ESP32 must remain powered on continuously and connected to Wi-Fi.**

# Media

![ESP32 Setup](images/IMG_9090.jpg)

## References
- https://randomnerdtutorials.com/esp32-send-email-smtp-server-arduino-ide/

