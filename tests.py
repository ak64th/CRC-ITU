from unittest import TestCase

from crc_itu import crc16


class CRC16Test(TestCase):
    def test_crc16(self):
        self.assertEqual(crc16(b'\x05\x01\x00\x03'), 0xface)
