import asyncio
from bleak import BleakClient, BleakScanner

# Add your device's address here.
# Can be UUID or MAC address
address = '08:65:f0:a5:a9:b7'

COLOR_UUID = '0000ff01-0000-1000-8000-00805f9b34fb'

counter = 1

def set_counter(packet: bytearray):
    global counter
    packet[1] = counter & 0xff
    packet[0] = (counter >> 8) & 0xff
    counter += 1
    return packet

# Needs this to reset the counter (?).
def create_initial_packet():
    base = bytearray.fromhex('0001 8000 000C 0D0B 1014 1906 1114 2331 0200 0FCD')
    packet = base[:]
    return set_counter(packet)

def create_red_packet():
    base = bytearray.fromhex('0001 8000 000D 0E0B 3BA1 B464 6400 0000 0014 0000 6C')
    packet = base[:]
    return set_counter(packet)

def create_purple_packet():
    base = bytearray.fromhex('0002 8000 000D 0E0B 3BA1 9664 6400 0000 0014 0000 4E')
    packet = base[:]
    return set_counter(packet)

# Interesting note: I have a trace on another computer, but Copilot was able to
# guess these next 4 packets correctly, without knowing what colors they were.
def create_blue_packet():
    base = bytearray.fromhex('0003 8000 000D 0E0B 3BA1 7864 6400 0000 0014 0000 30')
    packet = base[:]
    return set_counter(packet)

def create_cyan_packet():
    base = bytearray.fromhex('0004 8000 000D 0E0B 3BA1 5A64 6400 0000 0014 0000 12')
    packet = base[:]
    return set_counter(packet)

def create_green_packet():
    base = bytearray.fromhex('0005 8000 000D 0E0B 3BA1 3C64 6400 0000 0014 0000 F4')
    packet = base[:]
    return set_counter(packet)

def create_yellow_packet():
    base = bytearray.fromhex('0006 8000 000D 0E0B 3BA1 1E64 6400 0000 0014 0000 D6')
    packet = base[:]
    return set_counter(packet)

# TODO: wrong
def create_white_packet():
    base = bytearray.fromhex('0007 8000 000D 0E0B 3BA1 0064 6400 0000 0014 0000 B8')
    packet = base[:]
    return set_counter(packet)

async def main():
    device = await BleakScanner.find_device_by_address(address)

    async with BleakClient(device) as client:
        print(f'Client connection = {client.is_connected}') # prints True or False

        ip = create_initial_packet()
        print(f'Writing initial packet: {ip.hex()}')
        await client.write_gatt_char(COLOR_UUID, ip)
        await asyncio.sleep(1)

        # 5 times:
        # for _ in range(5):
        rp = create_red_packet()
        print(f'Writing red packet: {rp.hex()}')
        await client.write_gatt_char(COLOR_UUID, rp)
        await asyncio.sleep(1)

        bp = create_purple_packet()
        print(f'Writing purple packet: {bp.hex()}')
        await client.write_gatt_char(COLOR_UUID, bp)
        await asyncio.sleep(1)

        ap = create_blue_packet()
        print(f'Writing blue packet: {ap.hex()}')
        await client.write_gatt_char(COLOR_UUID, ap)
        await asyncio.sleep(1)

        ap = create_cyan_packet()
        print(f'Writing cyan packet: {ap.hex()}')
        await client.write_gatt_char(COLOR_UUID, ap)
        await asyncio.sleep(1)

        ap = create_green_packet()
        print(f'Writing green packet: {ap.hex()}')
        await client.write_gatt_char(COLOR_UUID, ap)
        await asyncio.sleep(1)

        ap = create_yellow_packet()
        print(f'Writing yellow packet: {ap.hex()}')
        await client.write_gatt_char(COLOR_UUID, ap)
        await asyncio.sleep(1)

        ap = create_white_packet()
        print(f'Writing white packet: {ap.hex()}')
        await client.write_gatt_char(COLOR_UUID, ap)
        await asyncio.sleep(1)

        # for service in client.services:
        #     print(f'Service: {service}')

        #     for char in service.characteristics:
        #         print(f'  Characteristic: {char}')

        #         try:
        #             ip = create_initial_packet()
        #             print(f'  Writing to characteristic {char.uuid} with packet: {ip.hex()}')
        #             await client.write_gatt_char(
        #                 char,
        #                 ip
        #             )

        #             rp = create_red_packet()
        #             print(f'  Writing to characteristic {char.uuid} with packet: {rp.hex()}')
        #             await client.write_gatt_char(
        #                 char,
        #                 # '0000ff01-0000-1000-8000-00805f9b34fb',
        #                 # '0000ff02-0000-1000-8000-00805f9b34fb',
        #                 # '0000ff01-0000-1000-8000-00805f9b34fb',

        #                 # # 0066 8000 000D 0E0B 3BA1 B464 6400 0000
        #                 # bytearray.fromhex('00668000000d0e0b3ba1b46464000000')
        #                 # 0001 8000 000D 0E0B 3BA1 B464 6400 0000
        #                 rp
        #             )

        #             await asyncio.sleep(1)

        #             bp = create_blue_packet()
        #             print(f'  Writing to characteristic {char.uuid} with packet: {bp.hex()}')
        #             await client.write_gatt_char(
        #                 char,
        #                 bp
        #             )

        #             await asyncio.sleep(1)

        #             rp2 = create_red_packet()
        #             print(f'  Writing to characteristic {char.uuid} with packet: {rp2.hex()}')
        #             await client.write_gatt_char(
        #                 char,
        #                 rp2
        #             )

        #             await asyncio.sleep(1)

        #         except Exception as e:
        #             print(f'Error writing to characteristic {char.uuid}: {e}')


if __name__ == "__main__":
    asyncio.run(main())