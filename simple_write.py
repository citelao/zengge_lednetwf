import asyncio
from bleak import BleakClient, BleakScanner


# Add your device's address here.
# Can be UUID or MAC address
address = '08:65:f0:a5:a9:b7'

counter = 1

def create_initial_packet():
    base = bytearray.fromhex('0001 8000 000C 0D0B 1014 1906 1114 2331 0200 0FCD')
    packet = base[:]
    global counter
    packet[1] = counter & 0xff
    packet[0] = (counter >> 8) & 0xff
    counter += 1
    return packet

def create_red_packet():
    base = bytearray.fromhex('0001 8000 000D 0E0B 3BA1 B464 6400 0000 0014 0000 6C')
    packet = base[:]
    global counter
    packet[1] = counter & 0xff
    packet[0] = (counter >> 8) & 0xff
    counter += 1
    return packet

def create_blue_packet():
    base = bytearray.fromhex('0002 8000 000D 0E0B 3BA1 9664 6400 0000 0014 0000 4E')
    packet = base[:]
    global counter
    # Update the correct indices for the counter (swap 3 and 4 if needed)
    packet[1] = counter & 0xff
    packet[0] = (counter >> 8) & 0xff
    counter += 1
    return packet

async def main():
    device = await BleakScanner.find_device_by_address(address)

    async with BleakClient(device) as client:
        print(f'Client connection = {client.is_connected}') # prints True or False

        for service in client.services:
            print(f'Service: {service}')

            for char in service.characteristics:
                print(f'  Characteristic: {char}')

                try:
                    ip = create_initial_packet()
                    print(f'  Writing to characteristic {char.uuid} with packet: {ip.hex()}')
                    await client.write_gatt_char(
                        char,
                        ip
                    )

                    rp = create_red_packet()
                    print(f'  Writing to characteristic {char.uuid} with packet: {rp.hex()}')
                    await client.write_gatt_char(
                        char,
                        # '0000ff01-0000-1000-8000-00805f9b34fb',
                        # '0000ff02-0000-1000-8000-00805f9b34fb',
                        # '0000ff01-0000-1000-8000-00805f9b34fb',

                        # # 0066 8000 000D 0E0B 3BA1 B464 6400 0000
                        # bytearray.fromhex('00668000000d0e0b3ba1b46464000000')
                        # 0001 8000 000D 0E0B 3BA1 B464 6400 0000
                        rp
                    )

                    await asyncio.sleep(1)

                    bp = create_blue_packet()
                    print(f'  Writing to characteristic {char.uuid} with packet: {bp.hex()}')
                    await client.write_gatt_char(
                        char,
                        bp
                    )

                    await asyncio.sleep(1)

                    rp2 = create_red_packet()
                    print(f'  Writing to characteristic {char.uuid} with packet: {rp2.hex()}')
                    await client.write_gatt_char(
                        char,
                        rp2
                    )

                    await asyncio.sleep(1)

                except Exception as e:
                    print(f'Error writing to characteristic {char.uuid}: {e}')


if __name__ == "__main__":
    asyncio.run(main())