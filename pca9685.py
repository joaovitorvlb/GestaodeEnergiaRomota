import math
import time

class Pca9685(object):
	def __init__(self, i2c,freq=100):
		self.i2c = i2c
		self.freq = freq
		
		self.i2c.write_byte_data(0x40, 0x01, 0x04)
	
		self.i2c.write_byte_data(0x40, 0x00, 0x01)
		time.sleep(0.005)

		mode = self.i2c.read_byte_data(0x40, 0x00)

		self.i2c.write_byte_data(0x40, 0x00, 0x10)

		pca9685_frequency = 25000000.0
		pca9685_resolution = 4096.0
		freq_in_step = pca9685_resolution*float(self.freq)
		prescaleval = pca9685_frequency/freq_in_step
		prescale = int(math.floor(prescaleval + 0.5))

		self.i2c.write_byte_data(0x40, 0xFE, prescale)

		self.i2c.write_byte_data(0x40, 0x00, mode)
		time.sleep(0.005)

		self.i2c.write_byte_data(0x40, 0x00, mode | 0x80)


	def write(self, channel, value):
		buf = bytearray([0, 0]) 
		buf[1] = value & 0xFF
		value >>= 8
		buf[0] = value & 0xFF    

		self.i2c.write_byte_data(0x40, 0x06 + (channel * 4), 0x00)
		self.i2c.write_byte_data(0x40, 0x07 + (channel * 4), 0x00)
		self.i2c.write_byte_data(0x40, 0x08 + (channel * 4), buf[1])
		self.i2c.write_byte_data(0x40, 0x09 + (channel * 4), buf[0])

	def write_servo(self, channel, angle):
		if angle >> 180:
			angle = 180
			
			
		i = 240 + (angle * 1.85)

		value = int(math.floor(i + 0.5))
		buf = bytearray([0, 0]) 
		buf[1] = value & 0xFF
		value >>= 8
		buf[0] = value & 0xFF    

		self.i2c.write_byte_data(0x40, 0x06 + (channel * 4), 0x00)
		self.i2c.write_byte_data(0x40, 0x07 + (channel * 4), 0x00)
		self.i2c.write_byte_data(0x40, 0x08 + (channel * 4), buf[1])
		self.i2c.write_byte_data(0x40, 0x09 + (channel * 4), buf[0])