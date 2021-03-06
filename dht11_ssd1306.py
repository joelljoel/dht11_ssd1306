
import subprocess
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import RPi.GPIO as GPIO
import dht11
import time
import datetime


# initialize GPIO
GPIO.setwarnings(False)

# read data using pin 14
instance = dht11.DHT11(pin = 4)


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.

disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)


# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.

width = disp.width
height = disp.height
image = Image.new("1", (width, height))


# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)


# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.

padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.

x = 0

# Load default font.

font = ImageFont.load_default()

while True:

    # Draw a black filled box to clear the image.
    result = instance.read()
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "Temp:"+ str(result.temperature) , font=font, fill=255)
    draw.text((x, top + 15), "Humidity: " +str(result.humidity), font=font, fill=255)


    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(2)



