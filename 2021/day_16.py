import json
import re
from functools import reduce
from itertools import count
from operator import mul

from utils import read_input


def get_cleaned_input():
    raw_in = read_input("inputs/day_16.txt")
    transmission = raw_in[0]
    return transmission


def hex_to_bin(hex_packet):
    b = "".join(bin(int(c, 16))[2:].zfill(4) for c in hex_packet)
    return b


def decode_first(transmission):
    """Decodes the first packet in transmission and returns
    it along with the rest of the transmission"""
    version = int(transmission[:3], 2)
    type = int(transmission[3:6], 2)
    payload = transmission[6:]

    if type == 4:
        s = ""
        for i in count(0, 5):
            s += payload[i + 1 : i + 5]
            if payload[i] == "0":
                break
        content = int(s, 2)
        rest = payload[i + 5 :]

    else:
        length_type = payload[0]
        if length_type == "0":
            total_length = int(payload[1:16], 2)
            tmp = payload[16:]

            packet_data = tmp[:total_length]
            rest = tmp[total_length:]

            content = []
            while packet_data:
                packet, packet_data = decode_first(packet_data)
                content.append(packet)

        elif length_type == "1":
            n_packets = int(payload[1:12], 2)
            packet_data = payload[12:]
            content = []
            for _ in range(n_packets):
                packet, packet_data = decode_first(packet_data)
                content.append(packet)
            rest = packet_data

    decoded = {"version": version, "type": type, "content": content}

    return decoded, rest


def decode(hex_transmission):
    transmission = hex_to_bin(hex_transmission)
    decoded, _ = decode_first(transmission)
    return decoded


def sum_versions(decoded):
    js = json.dumps(decoded)
    versions = re.findall('"version": (\d*)', js)
    s = sum(map(int, versions))
    return s


def resolve(packet):
    type = packet["type"]

    if type == 0:
        result = sum(resolve(x) for x in packet["content"])
    elif type == 1:
        result = reduce(mul, [resolve(x) for x in packet["content"]])
    elif type == 2:
        result = min(resolve(x) for x in packet["content"])
    elif type == 3:
        result = max(resolve(x) for x in packet["content"])
    elif type == 4:
        result = packet["content"]
    elif type == 5:
        a, b = map(resolve, packet["content"])
        result = a > b
    elif type == 6:
        a, b = map(resolve, packet["content"])
        result = a < b
    elif type == 7:
        a, b = map(resolve, packet["content"])
        result = a == b

    return result


if __name__ == "__main__":
    hex_transmission = get_cleaned_input()

    packet = decode(hex_transmission)

    answer_1 = sum_versions(packet)
    answer_2 = resolve(packet)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
