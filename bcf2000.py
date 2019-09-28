#!/usr/bin/python3

from __future__ import print_function

import os

class BcfConfig(object):
    def __init__(self, header=None):
        self.header = header
        self.text = [] # list of lines of text

    def load_text(self, text):
        self.text = [x.strip() for x in text.split(b'\n')]

    @property
    def dump(self):
        assert self.header
        ret = []
        for seq,line in enumerate(self.text):
            ret.append(b'\xf0'+ # sysex begin
                       self.header+
                       bytes([seq>>7, seq & 0x7f])+
                       line+
                       b'\xf7') # sysex end

        for r in []: #ret:
            print(" ".join("%02x"%ord(c) for c in r), end=' ')
            print(repr(r))
        return ret #''.join(ret)

    @dump.setter
    def dump(self, sysex):
        s = struct.unpack('%dB'%len(sysex), sysex)
        assert s[0] == 0xf0
        assert s[-1] == 0xf7
        if self.header:
            assert s[1:7]==self.header
        else:
            self.header = s[1:7]
        sequence = (s[7]<<7) | s[8]
        assert sequence==len(self.text)
        self.text.append(sysex[9:-1])

config = BcfConfig(bytes([0x00, 0x20, 0x32, 0x00, 0x14, 0x20]))

config.load_text(b"""$rev F1
$preset
  .name 'all controls            '
  .snapshot off
  .request off
  .egroups 4
  .fkeys on
  .lock off
  .init
$encoder 1
  .easypar CC 1 1 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 2
  .easypar CC 1 2 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 3
  .easypar CC 1 3 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 4
  .easypar CC 1 4 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 5
  .easypar CC 1 5 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 6
  .easypar CC 1 6 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 12
$encoder 7
  .easypar CC 1 7 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 3
$encoder 8
  .easypar CC 1 8 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 2
$encoder 9
  .easypar CC 1 9 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 10
  .easypar CC 1 10 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 11
  .easypar CC 1 11 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 12
  .easypar CC 1 12 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 13
  .easypar CC 1 13 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 14
  .easypar CC 1 14 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 15
  .easypar CC 1 15 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 16
  .easypar CC 1 16 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 17
  .easypar CC 1 17 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 18
  .easypar CC 1 18 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 19
  .easypar CC 1 19 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 20
  .easypar CC 1 20 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 21
  .easypar CC 1 21 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 22
  .easypar CC 1 22 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 23
  .easypar CC 1 23 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 24
  .easypar CC 1 24 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 25
  .easypar CC 1 25 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 1
$encoder 26
  .easypar CC 1 26 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 27
  .easypar CC 1 27 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$encoder 28
  .easypar CC 1 28 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 2
$encoder 29
  .easypar CC 1 29 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 43
$encoder 30
  .easypar CC 1 30 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 49
$encoder 31
  .easypar CC 1 31 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 55
$encoder 32
  .easypar CC 1 32 0 127 absolute
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$button 1
  .easypar CC 1 33 127 0 toggleon
  .showvalue on
  .default 0
$button 2
  .easypar CC 1 34 127 0 toggleon
  .showvalue on
  .default 0
$button 3
  .easypar CC 1 35 127 0 toggleon
  .showvalue on
  .default 0
$button 4
  .easypar CC 1 36 127 0 toggleon
  .showvalue on
  .default 127
$button 5
  .easypar CC 1 36 127 0 toggleon
  .showvalue on
  .default 127
$button 6
  .easypar CC 1 38 127 0 toggleon
  .showvalue on
  .default 0
$button 7
  .easypar CC 1 39 127 0 toggleon
  .showvalue on
  .default 0
$button 8
  .easypar CC 1 40 127 0 toggleon
  .showvalue on
  .default 0
$button 9
  .easypar CC 1 41 127 0 toggleon
  .showvalue on
  .default 0
$button 10
  .easypar CC 1 42 127 0 toggleon
  .showvalue on
  .default 0
$button 11
  .easypar CC 1 43 127 0 toggleon
  .showvalue on
  .default 0
$button 12
  .easypar CC 1 44 127 0 toggleon
  .showvalue on
  .default 0
$button 13
  .easypar CC 1 45 127 0 toggleon
  .showvalue on
  .default 0
$button 14
  .easypar CC 1 46 127 0 toggleon
  .showvalue on
  .default 0
$button 15
  .easypar CC 1 47 127 0 toggleon
  .showvalue on
  .default 0
$button 16
  .easypar CC 1 48 127 0 toggleon
  .showvalue on
  .default 0
$button 17
  .easypar CC 1 49 127 0 toggleon
  .showvalue on
  .default 0
$button 18
  .easypar CC 1 50 127 0 toggleon
  .showvalue on
  .default 0
$button 19
  .easypar CC 1 51 127 0 toggleon
  .showvalue on
  .default 0
$button 20
  .easypar CC 1 52 127 0 toggleon
  .showvalue on
  .default 127
$button 21
  .easypar CC 1 53 127 0 toggleon
  .showvalue on
  .default 127
$button 22
  .easypar CC 1 54 127 0 toggleon
  .showvalue on
  .default 127
$button 23
  .easypar CC 1 55 127 0 toggleon
  .showvalue on
  .default 0
$button 24
  .easypar CC 1 56 127 0 toggleon
  .showvalue on
  .default 0
$button 25
  .easypar CC 1 57 127 0 toggleon
  .showvalue on
  .default 0
$button 26
  .easypar CC 1 58 127 0 toggleon
  .showvalue on
  .default 127
$button 27
  .easypar CC 1 59 127 0 toggleon
  .showvalue on
  .default 0
$button 28
  .easypar CC 1 60 127 0 toggleon
  .showvalue on
  .default 0
$button 29
  .easypar CC 1 61 127 0 toggleon
  .showvalue on
  .default 0
$button 30
  .easypar CC 1 62 127 0 toggleon
  .showvalue on
  .default 0
$button 31
  .easypar CC 1 63 127 0 toggleon
  .showvalue on
  .default 127
$button 32
  .easypar CC 1 64 127 0 toggleon
  .showvalue on
  .default 0
$button 33
  .easypar CC 1 65 127 0 toggleon
  .showvalue on
  .default 0
$button 34
  .easypar CC 1 66 127 0 toggleon
  .showvalue on
  .default 0
$button 35
  .easypar CC 1 67 127 0 toggleon
  .showvalue on
  .default 0
$button 36
  .easypar CC 1 68 127 0 toggleon
  .showvalue on
  .default 0
$button 37
  .easypar CC 1 69 127 0 toggleon
  .showvalue on
  .default 0
$button 38
  .easypar CC 1 70 127 0 toggleon
  .showvalue on
  .default 0
$button 39
  .easypar CC 1 71 127 0 toggleon
  .showvalue on
  .default 0
$button 40
  .easypar CC 1 72 127 0 toggleon
  .showvalue on
  .default 0
$button 41
  .easypar CC 1 73 127 0 toggleon
  .showvalue on
  .default 0
$button 42
  .easypar CC 1 74 127 0 toggleon
  .showvalue on
  .default 0
$button 43
  .easypar CC 1 75 127 0 toggleon
  .showvalue on
  .default 0
$button 44
  .easypar CC 1 76 127 0 toggleon
  .showvalue on
  .default 0
$button 45
  .easypar CC 1 77 127 0 toggleon
  .showvalue on
  .default 0
$button 46
  .easypar CC 1 78 127 0 toggleon
  .showvalue on
  .default 0
$button 47
  .easypar CC 1 79 127 0 toggleon
  .showvalue on
  .default 0
$button 48
  .easypar CC 1 80 127 0 toggleon
  .showvalue on
  .default 0
$button 49
  .easypar CC 1 89 127 0 toggleon
  .showvalue on
  .default 0
$button 50
  .easypar CC 1 90 127 0 toggleon
  .showvalue on
  .default 0
$button 51
  .easypar CC 1 91 127 0 toggleon
  .showvalue on
  .default 0
$button 52
  .easypar CC 1 92 127 0 toggleon
  .showvalue on
  .default 0
$button 61
  .easypar CC 1 93 127 0 toggleon
  .showvalue on
  .default 0
$fader 1
  .easypar CC 1 1 0 16383 absolute/14
  .showvalue on
  .motor on
  .override move
  .keyoverride off
$fader 2
  .easypar CC 1 2 0 16383 absolute/14
  .showvalue on
  .motor on
  .override move
  .keyoverride off
$fader 3
  .easypar CC 1 3 0 16383 absolute/14
  .showvalue on
  .motor on
  .override move
  .keyoverride off
  .default 0
$fader 4
  .easypar CC 1 4 0 16383 absolute/14
  .showvalue on
  .motor on
  .override move
  .keyoverride off
  .default 0
$fader 5
  .easypar CC 1 5 0 16383 absolute/14
  .showvalue on
  .motor on
  .override move
  .keyoverride off
  .default 0
$fader 6
  .easypar CC 1 6 0 16383 absolute/14
  .showvalue on
  .motor on
  .override move
  .keyoverride off
  .default 3
$fader 7
  .easypar CC 1 7 0 16383 absolute/14
  .showvalue on
  .motor on
  .override move
  .keyoverride off
  .default 0
$fader 8
  .easypar CC 1 8 0 16383 absolute/14
  .showvalue on
  .motor on
  .override move
  .keyoverride off
  .default 0
$fader 9
  .easypar CC 1 94 0 127 absolute
  .showvalue on
  .motor off
  .override move
  .keyoverride off
$end
""")

import time
class BCF2000(object):
    def __init__(self):
        fdnum = os.open('/dev/midi2',os.O_NONBLOCK | os.O_RDWR)
        self.fd = os.fdopen(fdnum, 'wb+', 0)
        self.buf = b''
        self.controllers = [None]*122
        self.load_sysex(config)

    def load_sysex(self, config):
        time.sleep(0.1)
        for i,d in enumerate(config.dump):
            while 1:
                try:
                    self.fd.write(d)
                    time.sleep(.005)
                    break
                except IOError as e:
                    if e.errno != 11:
                        raise
                    print("retry",i,d)

    def setup_fader(self, number, ccnum, fmin, fmax):
        config = BcfConfig(bytes([0x00, 0x20, 0x32, 0x00, 0x14, 0x20]))
        config.load_text(b"""$rev F1
$preset
$fader %d
  .easypar CC 1 %d %d %d absolute/14
  .showvalue on
  .motor on
  .override move
  .keyoverride off
  .default 0
$end
"""%(number, ccnum, fmin, fmax))
        self.load_sysex(config)

    def setup_encoder(self, number, ccnum, fmin, fmax):
        config = BcfConfig(bytes([0x00, 0x20, 0x32, 0x00, 0x14, 0x20]))
        config.load_text(b"""$rev F1
$preset
$encoder %d
  .easypar CC 1 %d %d %d absolute/14
  .showvalue on
  .mode 12dot
  .resolution 96 96 96 96
  .default 0
$end
"""%(number, ccnum, fmin, fmax))
        self.load_sysex(config)

    def poll(self):
        while 1:
            try:
                b = self.fd.read(1)
            except IOError as e:
                if e.errno != 11:
                    raise
                return

            if not b is None:
                self.buf = self.buf + b
                self.checkbuf()

    def checkbuf(self):
        while self.buf and not (self.buf[0] & 0x80):
            del self.buf[0]

        if len(self.buf):
            cmd = self.buf[0]
            len_ = len(self.buf)

            channel = cmd & 0x0f
            command = cmd & 0xf0
            if command==0xb0: # CC
                if len_ == 3:
                    self.cc(self.buf)
                    self.buf=b''
            elif command==0xf0: # SysEx dump
                if self.buf[-1] == 0xf7:
                    self.sysex(self.buf)
                    self.buf=b''
            else:
                raise Exception("unknown command 0x%02x"%command)

    def cc(self, buf):
        controller = buf[1]
        value = buf[2]
        if controller < 0x20:
            self.controllers[controller] = value << 7
        elif controller < 0x40:
            self.controllers[controller-0x20] |= value
            self.on_new_cc(controller-0x20)
        else:
            self.controllers[controller] = value
            self.on_new_cc(controller)

    def on_new_cc(self, cont):
        print("cont",cont,self.controllers[cont])
        # Example: tie faders 1 & 2 together

        if cont==2:
            self.set_cc(1, 16383-self.controllers[cont])
        if cont==1:
            self.set_cc(2, 16383-self.controllers[cont])

    def set_cc(self, cont, val):
        if cont < 32:
            val_msb = val >> 7
            val_lsb = val & 0x7f
            cmd = [0xb0, cont, val_msb, cont+32, val_lsb]
            self.fd.write(bytes(cmd))

    def sysex(self, buf):
        if not self.config:
            self.config = BcfConfig()
        self.config.dump = buf

if __name__=="__main__":
    bc = BCF2000()
    bc.setup_fader(3, 3, 500, 800)
    bc.setup_encoder(3, 13, 500, 800)
    while 1:
        bc.poll()
