#!/usr/bin/python
import math
import time

class Mpu6050(object):
    def __init__(self, i2c, adr):
        self.i2c = i2c
        self.adr = adr
        self.power_mgmt_1 = 0x6b
        self.power_mgmt_2 = 0x6c
        self.reggyro_x_H = 0x43
        self.reggyro_x_L = 0x44
        self.reggyro_y_H = 0x45
        self.reggyro_y_L = 0x46
        self.reggyro_z_H = 0x47
        self.reggyro_z_L = 0x48
        self.regaccel_x_H = 0x3b
        self.regaccel_x_L = 0x3c
        self.regaccel_y_H = 0x3d
        self.regaccel_y_L = 0x3e
        self.regaccel_z_H = 0x3f
        self.regaccel_z_L = 0x40
        self.i2c.write_byte_data(self.adr, self.power_mgmt_1, 0)

    def read_gyro_x(self):
        buf = bytearray([0, 0]) 
        buf[1] = self.i2c.read_byte_data(self.adr, self.reggyro_x_H)
        buf[0] = self.i2c.read_byte_data(self.adr, self.reggyro_x_L)
        value = (buf[1] << 8) + buf[0]
        return value

    def read_gyro_y(self):
        buf = bytearray([0, 0]) 
        buf[1] = self.i2c.read_byte_data(self.adr, self.reggyro_y_H)
        buf[0] = self.i2c.read_byte_data(self.adr, self.reggyro_y_L)
        value = (buf[1] << 8) + buf[0]
        return value

    def read_gyro_z(self):
        buf = bytearray([0, 0]) 
        buf[1] = self.i2c.read_byte_data(self.adr, self.reggyro_z_H)
        buf[0] = self.i2c.read_byte_data(self.adr, self.reggyro_z_L)
        value = (buf[1] << 8) + buf[0]

    def read_accel_x(self):
        buf = bytearray([0, 0]) 
        buf[1] = self.i2c.read_byte_data(self.adr, self.regaccel_x_H)
        buf[0] = self.i2c.read_byte_data(self.adr, self.regaccel_x_L)
        value = (buf[1] << 8) + buf[0]
        return value

    def read_accel_y(self):
        buf = bytearray([0, 0]) 
        buf[1] = self.i2c.read_byte_data(self.adr, self.regaccel_y_H)
        buf[0] = self.i2c.read_byte_data(self.adr, self.regaccel_y_L)
        value = (buf[1] << 8) + buf[0]
        return value

    def read_accel_z(self):
        buf = bytearray([0, 0]) 
        buf[1] = self.i2c.read_byte_data(self.adr, self.regaccel_z_H)
        buf[0] = self.i2c.read_byte_data(self.adr, self.regaccel_z_L)
        value = (buf[1] << 8) + buf[0]
        return value



