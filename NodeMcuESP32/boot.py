
# This file is executed on every boot (including wake-boot from deepsleep)

import ina219 
import machine
import logging
import os
import main
import lcd
import i2c_lcd
import i2c_lcd_backlight
import i2c_lcd_screen


machine.main('main.py')
main.start()


