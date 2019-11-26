"""
    created by Jordan Gassaway, 11/21/2019
    Test for pn532i2c class
"""
from unittest import TestCase
from PN532_I2C.pn532i2c import pn532i2c


class TestPn532i2c(TestCase):
    def setUp(self):
        self.pn532 = pn532i2c(1)
        self.pn532.begin()

    def test_wakeup(self):
        self.pn532.wakeup()  #  check no exceptions

    def test_writeCommand(self):
        self.pn532.writeCommand(bytearray([0x2]), bytearray())
        rsp = self.pn532.readResponse(10)
        print('Response {!r}'.format(rsp))
        self.assertEqual(bytearray([0x32, 0x1, 0x6, 0x7]), rsp[1])    # Check against known firmware ver
        self.assertEqual(4, rsp[0])    # Check length is correct

    # def test_getResponseLength(self):
    #     self.fail()

    # def test_readResponse(self):
    #     self.fail()

    # def test_readAckFrame(self):
    #     self.fail()
