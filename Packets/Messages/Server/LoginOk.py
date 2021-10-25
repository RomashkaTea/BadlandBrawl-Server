# -*- coding: utf-8 -*-

import time
from Utils.Writer import Writer


class LoginOk(Writer):

    def __init__(self, device):
        self.id = 20104
        self.version = 1
        self.device = device
        super().__init__(self.device)

    def encode(self):
        self.writeHexa('''01 00 00 00 02 00 30 1D 96 00 00 00 02 00 30 1D 96 00 00 00 28 6E 32 61 38 36 77 62 61 78 33 68 37 67 36 72 34 74 6A 79 64 77 6E 77 79 61 33 74 74 7A 6B 34 65 73 64 72 6B 6A 36 67 37 FF FF FF FF FF FF FF FF 01 00 AA 38 01 00 00 00 04 70 72 6F 64 2D 9E 10 00 00 00 00 00 00 00 00 0D 31 36 33 35 31 37 30 32 38 32 33 33 37 00 00 00 0D 31 36 33 35 31 36 35 36 31 31 30 30 30 00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 00 00 00 2D 68 74 74 70 73 3A 2F 2F 64 6B 66 77 74 6A 30 68 38 68 6A 33 32 2E 63 6C 6F 75 64 66 72 6F 6E 74 2E 6E 65 74 2F 31 5F 30 5F 33 36 32 36''')
        self.writeString("228.228.228.228") # clientIp