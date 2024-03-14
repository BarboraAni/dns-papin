import random
import socket
import struct
from itertools import cycle
from threading import Thread

from enums import DnsRecordType


class Sender:
    def __init__(self, target: str, port: int, records: list, thread_count: int):
        self.target = target
        self.port = port
        self.records = records
        self.packets = None
        self.threads = []
        self.init_packets()
        self.init_threads(thread_count)

    def create_packet(self, record: tuple):
        packet = struct.pack(">H", random.randrange(1, 65535))
        packet += struct.pack(">H", 256)
        packet += struct.pack(">H", 1)
        packet += struct.pack(">H", 0)
        packet += struct.pack(">H", 0)
        packet += struct.pack(">H", 0)
        split_record = record[0].split(".")
        for part in split_record:
            packet += struct.pack("B", len(part))
            for byte in part:
                packet += struct.pack("c", bytes(byte, "utf-8"))
        packet += struct.pack("B", 0)
        packet += struct.pack(">H", getattr(DnsRecordType, record[1]))
        packet += struct.pack(">H", 1)
        return packet

    def init_packets(self):
        packets = []
        for record in self.records:
            packets.append(self.create_packet(record))

        self.packets = cycle(packets)

    def init_threads(self, thread_count: int):
        for i in range(thread_count):
            thread = Thread(target=self.send_packets, args=(i,))
            self.threads.append(thread)

    def send_packets(self, thread_id):
        n = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("", 0))
        while True:
            s.sendto(bytes(next(self.packets)), (str(self.target), self.port))
            n += 1

    def run(self):
        for i, thread in enumerate(self.threads):
            print(f"Starting thread #{i+1}")
            thread.start()

        for thread in self.threads:
            thread.join()
