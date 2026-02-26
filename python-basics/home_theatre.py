#Maureen Mbugua
#26/02/2026
#program to show how a home theatre operates


from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import utime

# LCD Setup
I2C_ADDR = 0x27
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# Buzzer
buzzer = Pin(10, Pin.OUT)

# Keypad setup
rows = [Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT)]
cols = [Pin(4, Pin.IN, Pin.PULL_DOWN), Pin(5, Pin.IN, Pin.PULL_DOWN),
        Pin(6, Pin.IN, Pin.PULL_DOWN), Pin(7, Pin.IN, Pin.PULL_DOWN)]

keys = [
    ["1","2","3","A"],
    ["4","5","6","B"],
    ["7","8","9","C"],
    ["*","0","#","D"]
]

password = "123456"
entered = ""

def scan_keypad():
    for i in range(4):
        rows[i].high()
        for j in range(4):
            if cols[j].value() == 1:
                utime.sleep(0.2)
                rows[i].low()
                return keys[i][j]
        rows[i].low()
    return None

lcd.putstr("Enter Password:")

while True:
    key = scan_keypad()
    if key:
        if key.isdigit():
            entered += key
            lcd.move_to(len(entered)-1, 1)
            lcd.putstr("*")
        
        if len(entered) == 6:
            utime.sleep(0.5)
            lcd.clear()
            
            if entered == password:
                lcd.putstr("Access Granted")
            else:
                lcd.putstr("Wrong Password")
                buzzer.high()
                utime.sleep(1)
                buzzer.low()
            
            utime.sleep(2)
            lcd.clear()
            lcd.putstr("Enter Password:")
            entered = ""


⸻

🚨 If It Shows Error

1️⃣ LCD not displaying?
	•	Check I2C address → try 0x3F instead of 0x27

Change:

I2C_ADDR = 0x3F


⸻

2️⃣ “pico_i2c_lcd not found” error?

In Wokwi:
	•	Click Library Manager
	•	Add:
	•	pico_i2c_lcd.py
	•	lcd_api.py

Or tell me and I’ll give you the exact files 😭

⸻

🎯 Expected Output

LCD:

Enter Password:
******

If correct:

Access Granted

If wrong:

Wrong Password
(Buzzer sounds)


⸻