from com.android.monkeyrunner import MonkeyRunner
import commands
import re
import telnetlib
import sys
import os
import config
import checkpic
from Log import Log
if '/Library/Python/2.7/site-packages/' not in sys.path:
    sys.path.append('/Library/Python/2.7/site-packages/')
try:
    import json
except ImportError:
    import simplejson as json


class Device:
    def __init__(self, device_id):
        self.__deviceId = device_id
        self.__device = MonkeyRunner.waitForConnection(5, device_id)
        assert self.__device is not None
        status, output = commands.getstatusoutput("adb -s %s shell ifconfig wlan0 | grep 'inet addr'" % device_id)
        if not status == 0:
            status, output = commands.getstatusoutput("adb -s %s shell ifconfig eth0 | grep 'inet addr'" % device_id)
        assert status == 0
        if output.strip() == '':
            print "please connect wlan on your device"
            raise BaseException
        s = re.search(r"inet addr:(\d+\.\d+\.\d+\.\d+)", output)
        assert s is not None
        self.__ip = s.groups()[0]
        self.tn = None
        self.resolution_width = config.standard_width
        self.resolution_height = config.standard_height
        self.real_width = config.standard_width
        self.real_height = config.standard_height
        self.data = {}
        self.is_running = False
        self.running_case_name = ''
        self.check_num = 0
        self.log = Log("common")

    def set_case_name(self, suite, name):
        self.log = Log(suite)
        self.running_case_name = name
        self.check_num = 1

    def run(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def get_device(self):
        return self.__device

    def get_device_id(self):
        return self.__deviceId

    def start_activity(self):
        self.stop_activity()
        self.__device.startActivity(config.package + '/' + config.activity)
        MonkeyRunner.sleep(35)
        self.tn = None
        self.get_screen_info()

    def stop_activity(self):
        os.system('adb -s %s shell am force-stop ' % self.__deviceId + config.package)
        MonkeyRunner.sleep(2)

    def get_screen_info(self):
        if self.tn is None:
            self.tn = telnetlib.Telnet(self.__ip, 20000)
        self.tn.read_until('>', 3)
        self.tn.write("winsize\n")
        res = self.tn.read_until('>')[:-1]
        s = re.search(r"(\d+)\s*x\s*(\d+)\s*\(design\s*resolution\)", res)
        assert s is not None
        self.resolution_width = int(s.groups()[0])
        self.resolution_height = int(s.groups()[1])
        s = re.search(r"(\d+)\s*x\s*(\d+)\s*\(real\s*screen\)", res)
        assert s is not None
        self.real_width = int(s.groups()[0])
        self.real_height = int(s.groups()[1])

    def refresh_ui_data(self):
        if self.tn is None:
            self.tn = telnetlib.Telnet(self.__ip, 20000)
        self.tn.read_until('>', 3)
        self.tn.write("nodeInfo\n")
        res = self.tn.read_until('>')[:-1]
        d = json.loads(res)
        for item in d["nodes"]:
            for info in item:
                if info in self.data:
                    self.data[info].append(item[info])
                else:
                    self.data[info] = []
                    self.data[info].append(item[info])

    def press_back(self, wait_time=2):
        try:
            self.__device.press('KEYCODE_BACK', 'DOWN_AND_UP')
        except Exception, e:
            self.log.error(e.message)
        finally:
            MonkeyRunner.sleep(wait_time)

    def press_home(self, wait_time=2):
        try:
            self.__device.press('KEYCODE_HOME', 'DOWN_AND_UP')
        except Exception, e:
            self.log.error(e.message)
        finally:
            MonkeyRunner.sleep(wait_time)

    def touch_pos(self, x, y, wait_time=2):
        x = x * self.real_width / config.standard_width
        y = y * self.real_height / config.standard_height
        try:
            self.__device.touch(x, y, 'DOWN_AND_UP')
        except Exception, e:
            self.log.error(e.message)
        finally:
            MonkeyRunner.sleep(wait_time)

    def touch(self, ccb, name, wait_time=2, index=0):
        self.refresh_ui_data()
        key = ccb + '-' + name
        assert key in self.data
        info = self.data[key][index]
        x, y = self.get_rect_center(info['x'], info['y'], info['width'], info['height'])
        assert self.in_screen(x, y)
        try:
            self.__device.touch(x, y, 'DOWN_AND_UP')
        except Exception, e:
            self.log.error(e.message)
        finally:
            MonkeyRunner.sleep(wait_time)

    def type(self, str, wait_time=2):
        self.__device.type(str)
        try:
            MonkeyRunner.sleep(wait_time)
        except Exception, e:
            self.log.error(e.message)
        finally:
            MonkeyRunner.sleep(wait_time)

    def in_screen(self, x, y):
        if 0 <= x < self.real_width and 0 <= y < self.real_height:
            return True
        return False

    def get_rect_center(self, x, y, width, height):
        res_x = (x + width/2) * self.real_width / self.resolution_width
        res_y = (y + height/2) * self.real_width / self.resolution_width
        return res_x, res_y

    def check_widget(self, name, fault=True, index=0):
        self.refresh_ui_data()
        info = self.data[name][index]
        x = int(info['x'] * self.real_width / self.resolution_width)
        y = int(info['y'] * self.real_width / self.resolution_width)
        width = int(info['width'] * self.real_width / self.resolution_width)
        height = int(info['height'] * self.real_width / self.resolution_width)
        res = self.check_pic(x, y, width, height, fault)
        return res

    def check_saved_pic(self, name, fault=True):
        res = checkpic.saved_pic_check(self.__device, self.running_case_name, 1.0, self.check_num, name, fault)
        if fault:
            self.check_num += 1
        return res

    def check_pic(self, x, y, width, height, fault=True):
        res = checkpic.pic_check(self.__device, self.running_case_name, 1.0, self.check_num, x, y, width, height, fault)
        if fault:
            self.check_num += 1
        return res

    def screen_shot_to_fault(self, case_name=None, check_num=0):
        image = self.__device.takeSnapshot()
        num = 1
        if case_name is None:
            case_name = self.running_case_name
        if check_num == 0:
            check_num = self.check_num
        while os.path.isfile('fault/%s_%d_%d.png' % (case_name, check_num, num)):
            num += + 1
            image.writeToFile('fault/%s_%d_%d.png' % (case_name, check_num, num), 'png')