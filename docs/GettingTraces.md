# How can you get a BLE trace?

You can use an external sniffer, but if you don't have one, the easiest way is to snoop on packets from one of your devices. Usually your phone.

## For Android

Use the Bluetooth HCI Snoop Log to grab packets.

I don't have an Android :(.

## For iOS/macOS

Use Packet Sniffer.

1. Install the Bluetooth profile on your phone to capture Bluetooth logs.
   * https://developer.apple.com/bug-reporting/profiles-and-logs/?name=bluetooth
2. Install Packet Sniffer on your Mac.
   * In [Additional Tools for XCode](https://developer.apple.com/download/all/?q=additional%20tools%20for%20Xcode)
3. Plug in the phone to your MAc & authorize the connection.
4. Create a new iOS trace in Packet Sniffer.
5. You can see all packets! You probably want `ATT Receive` and `ATT Send`; that's what these devices use to communicate.

Summarized from here: https://novelbits.io/debugging-sniffing-secure-ble-ios/
See also: https://www.bluetooth.com/blog/a-new-way-to-debug-iosbluetooth-applications/