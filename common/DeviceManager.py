from singleton import singleton
from Device import Device
import commands
import time


@singleton
class DeviceManager:
    def __init__(self):
        self.devices = []
        status, output = commands.getstatusoutput("adb devices")
        assert status == 0
        lines = output.split('\n')
        for i in range(1, len(lines)):
            if not lines[i].strip() == "":
                device_id = lines[i].split('\t')[0]
                device = Device(device_id)
                self.devices.append(device)

    def apply_device(self, count):
        assert count <= len(self.devices)
        ret_device = []
        while True:
            for d in self.devices:
                if not d.is_running:
                    ret_device.append(d)
                    if len(ret_device) == count:
                        return ret_device
            time.sleep(5)


if __name__ == "__main__":
    de = DeviceManager()
