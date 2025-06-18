# All of these end in a number that looks like a checksum. What's it a checksum of?

a1 = bytearray.fromhex('0003 8000 000D 0E0B 3BA1 7864 6400 0000 0014 0000 30')
a2 = bytearray.fromhex('0004 8000 000D 0E0B 3BA1 5A64 6400 0000 0014 0000 12')
a3 = bytearray.fromhex('0005 8000 000D 0E0B 3BA1 3C64 6400 0000 0014 0000 F4')
a4 = bytearray.fromhex('0006 8000 000D 0E0B 3BA1 1E64 6400 0000 0014 0000 D6')
a5 = bytearray.fromhex('0007 8000 000D 0E0B 3BA1 0064 6400 0000 0014 0000 B8')

if __name__ == "__main__":
    # Calculate the checksum for each packet
    packets = [a1, a2, a3, a4, a5]
    for i, packet in enumerate(packets, start=1):
        checksum = packet[-1]
        calculated_checksum = sum(packet[:-1]) % 256
        print(f'Packet {i} checksum: {checksum:02x}, calculated: {calculated_checksum:02x}')
        if checksum != calculated_checksum:
            print(f'Packet {i:02x} checksum does not match calculated value!')
        else:
            print(f'Packet {i:02x} checksum matches calculated value.')

        # Brute-force all continuous ranges
        found = False
        for start in range(len(packet)):
            for end in range(start + 1, len(packet)):
                rng_sum = sum(packet[start:end]) % 256
                if rng_sum == checksum:
                    print(f'  Match: bytes[{start}:{end}] sum % 256 == {checksum:02x}')
                    print(f'  Range: {packet[start:end].hex()}')
                    found = True
        if not found:
            print('  No matching continuous range found.')