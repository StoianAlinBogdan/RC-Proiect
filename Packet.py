import ipaddress
import struct
import socket


class Packet(object):
    def __init__(self, gui):
        self.OP = None
        self.HTYPE = 1  # Hardware type: Ethernet
        self.HLEN = 6  # Hardware address length: 6
        self.HOPS = 0  # Hops: 0
        self.XID = None  # Transaction ID (random)
        self.SECS = 0  # Seconds elapsed: 0
        self.FLAGS = 32768  # Flags: 8
        self.CIADDR = ipaddress.ip_address('0.0.0.0')  # Client IP address: 0.0.0.0
        self.YIADDR = ipaddress.ip_address('0.0.0.0')  # Your (client) IP address: 0.0.0.0
        self.SIADDR = ipaddress.ip_address('0.0.0.0')  # Next Server IP address: 0.0.0.0
        self.GIADDR = ipaddress.ip_address('0.0.0.0')  # Gateway IP address: 0.0.0.0
        self.CHADDR = None  # Client hardware address(16 bytes)
        self.SNAME = b'\x00' * 64  # Server name
        self.BNAME = b'\x00' * 128  # Boot file name
        self.MAGIC_COOKIE = b'\x63\x82\x53\x63'  # Magic Cookie: DHCP
        self.MSG_TYPE = None
        self.gui = gui
        self.ip = ipaddress.ip_address('0.0.0.0')
        self.options = []

    def pack(self):
        packet = b''
        packet += struct.pack('!BBBB', self.OP, self.HTYPE, self.HLEN, self.HOPS)
        packet += struct.pack('!I', self.XID)
        packet += struct.pack('!HH', self.SECS, self.FLAGS)
        packet += struct.pack('!IIII', int(self.CIADDR), int(self.YIADDR), int(self.SIADDR), int(self.GIADDR))
        packet += self.CHADDR + b'\x00' * 10
        packet += self.SNAME + self.BNAME
        packet += self.MAGIC_COOKIE
        # options
        packet += b'\x35\x01' + struct.pack('!B', self.MSG_TYPE)  # Option 53, Message type
        if self.gui.REQUESTED_IP.get():
            packet += b'\x32\x04' + struct.pack('!I', int(self.ip))  # Option 50, Request IP address
        if self.gui.TIME_OFFSET.get():
            packet += b'\x02\x04\x00\x00\x00\x00'
        if self.gui.PARAMETER_REQUEST_LIST.get():
            length = 0
            temp = b''
            if self.gui.SUBNET_MASK.get():
                length += 1
                temp += b'\x01'
            if self.gui.TIME_SERVER.get():
                length += 1
                temp += b'\x04'
            if self.gui.DOMAIN_NAME.get():
                length += 1
                temp += b'\x0f'
            if self.gui.DNS.get():
                length += 1
                temp += b'\x06'
            if length >= 1:
                packet += b'\x37' + struct.pack('!B', length) + temp
        if self.gui.HOST_NAME.get():
            host_name = socket.gethostname()
            packet += b'\x0c' + struct.pack('!B' + str(len(host_name)) + 's', len(host_name), bytes(host_name, 'utf-8'))
        if self.gui.LEASE_TIME.get():
            packet += b'\x33\x04\x00\x00\xff\x00'
        if self.gui.RENEWAL_TIME.get():
            packet += b'\x3a\x04\x00\x00\x00\x00'
        if self.gui.REBINDING_TIME.get():
            packet += b'\x3b\x04\x00\x00\x00\x00'

        packet += b'\xff'
        return packet

    def unpack(self, packet):
        self.OP, self.HTYPE, self.HLEN, self.HOPS = struct.unpack_from('BBBB', packet, 0)
        self.XID = struct.unpack_from('!I', packet, 4)[0]
        self.SECS, self.FLAGS = struct.unpack_from('HH', packet, 8)
        self.CIADDR = ipaddress.ip_address(struct.unpack_from('!I', packet, 12)[0])
        self.YIADDR = ipaddress.ip_address(struct.unpack_from('!I', packet, 16)[0])
        self.SIADDR = ipaddress.ip_address(struct.unpack_from('!I', packet, 20)[0])
        self.GIADDR = ipaddress.ip_address(struct.unpack_from('!I', packet, 24)[0])
        self.CHADDR = packet[28:34]
        self.SNAME = struct.unpack_from('64s', packet, 44)[0]
        self.BNAME = struct.unpack_from('124s', packet, 108)[0]
        self.MAGIC_COOKIE = hex(struct.unpack_from('!I', packet, 236)[0])

        start = 240
        while start <= len(packet):
            if packet[start] == 255:
                break
            length = packet[start + 1]
            offset = start + 2
            if packet[start] == 53:
                self.MSG_TYPE = packet[start + 2]
                start += 2 + length
                continue
            self.options.append((packet[start], length, packet[offset:offset + length]))
            start += 2 + length
