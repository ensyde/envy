from struct import *


class Reader:
    def __init__(self, data=None):
        self.data = data
        self.pos = 0

    def __len__(self):
        return len(self.data)

    def read_byte(self):
       b = self.data[self.pos]
       self.pos += 1
       return b

    def read_raw(self, length):
        b = self.data[self.pos:self.pos + length]
        self.pos += length
        return b

    def read_int16(self):
        s = unpack('<H', self.data[self.pos:self.pos + 2])[0]
        self.pos += 2
        return s

    def read_int32(self):
        i = unpack('<L', self.data[self.pos:self.pos + 4])[0]
        self.pos += 4
        return i

    def read_int64(self):
        l = unpack('<Q', self.data[self.pos:self.pos + 8])[0]
        self.pos += 8
        return l

    def read_string(self):
        idx = self.pos
        while idx < self.length():
            if self.data[idx] == 0x00:
                break
            idx += 1
        s = self.data[self.pos:idx].decode("ISO-8859-1")
        self.pos = idx + 1
        return s

class Writer:
    def __init__(self):
        self.data = b''

    def length(self):
        return len(self.data)

    def writeByte(self, value):
        self.data += bytes([value])

    def write_raw(self, value):
        self.data += value

    def write_int16(self, value):
        self.write_raw(pack('<H', value))

    def write_int32(self, value):
        self.write_raw(pack('<L', value))

    def writeInt64(self, value):
        self.write_raw(pack('<Q', value))

    def write_string(self, value):
        self.write_baw(value.encode("utf-8"))
        self.write_byte(0x00)
