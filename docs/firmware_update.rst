Firmware Update
===============

Following example code shows how the firmware update is intended to be used:

.. sourcecode:: python

    from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
    from sensirion_shdlc_svm41 import Svm41ShdlcDevice

    FIRMWARE_HEX_FILE = r'C:/path/to/Svm41Firmware.hex'

    def main():
        with ShdlcSerialPort(port='COM1', baudrate=115200) as port:
            device = Svm41ShdlcDevice(ShdlcConnection(port), slave_address=0)
            device.update_firmware(FIRMWARE_HEX_FILE, status_callback=print,
                                   emergency=False)
            print("Version after update: {}".format(device.get_version()))

    if __name__ == "__main__":
        main()

.. note:: This can take several seconds, don't abort it! If aborted, the device
          stays in the bootloader and you need to restart the update with
          ``emergency=True`` to recover.
