from itertools import islice
import math


def create_chars():
    for char in open("inputs/d16.txt").read().strip():
        # print(" === starting to consume char", char)
        num = int(char, 16)
        bin_str = f"{num:0>{4}b}"
        for i, c in enumerate(bin_str):
            # if i == len(bin_str) - 1:
            #    print("=== yielding last bit of char")
            yield c


contents = []
versions = []


def read_packet(gen, as_subpacket=False):
    # print("starting to read new packet")
    value = None
    bits_read = 0
    vers_bits = list(islice(gen, 3))
    bits_read += 3
    if len(vers_bits) == 0:
        return
    version = int("".join(vers_bits), 2)
    versions.append(version)
    type_id = int("".join(islice(gen, 3)), 2)
    bits_read += 3
    # print("version", version)
    # print("type id", type_id)
    if type_id == 4:
        content = []
        while True:
            bits = list(islice(gen, 5))
            bits_read += 5
            content.extend(bits[1:])
            if bits[0] == "0":
                break
        value = int("".join(content), 2)
    else:
        length_type_id = int("".join(islice(gen, 1)), 2)
        bits_read += 1
        values_from_subs = []
        # print("len type", length_type_id)
        if length_type_id == 0:
            sub_packet_bit_len = int("".join(islice(gen, 15)), 2)
            bits_read += 15
            sub_packet_bits_read = 0
            while sub_packet_bits_read < sub_packet_bit_len:
                bits_from_sub, value = read_packet(gen, as_subpacket=True)
                sub_packet_bits_read += bits_from_sub
                values_from_subs.append(value)
            bits_read += sub_packet_bits_read
        else:
            num_of_sub_packets = int("".join(islice(gen, 11)), 2)
            bits_read += 11
            for _ in range(num_of_sub_packets):
                bits_from_sub, value = read_packet(gen, as_subpacket=True)
                bits_read += bits_from_sub
                values_from_subs.append(value)
        if type_id == 0:
            value = sum(values_from_subs)
        elif type_id == 1:
            value = math.prod(values_from_subs)
        elif type_id == 2:
            value = min(values_from_subs)
        elif type_id == 3:
            value = max(values_from_subs)
        elif type_id == 5:
            value = 1 if values_from_subs[0] > values_from_subs[1] else 0
        elif type_id == 6:
            value = 1 if values_from_subs[0] < values_from_subs[1] else 0
        elif type_id == 7:
            value = 1 if values_from_subs[0] == values_from_subs[1] else 0
        else:
            raise Exception("Unknown type id")
    if not as_subpacket:
        extrabits = ((bits_read // 8) + 1) * 8 - bits_read
        list(islice(gen, extrabits))  # consume the extra bits
    else:
        return bits_read, value
    if value is not None:
        contents.append(value)
    read_packet(gen)


chars2 = create_chars()
read_packet(chars2)

print("part 01", sum(versions))
print("part 02", contents[0])
