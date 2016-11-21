import os
import time

import checkpic
import config

CASE_NAME = "Common"


def start_complete(device):
    for i in range(10):
        if not checkpic.saved_pic_check(device.get_device(), "Common", 0.9, 1, "start_complete", False):
            device.press_back()
        else:
            return True
    device.screen_shot_to_fault("common", 98)
    return False


def skip_FTE(device):
    device.touch_pos(1274, 211, 5)
    device.touch_pos(720, 12)
    device.touch_pos(720, 12)
    device.touch_pos(720, 1280, 10)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280, 5)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280, 5)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(720, 1280)
    device.touch_pos(70, 70, 1)
    do_profile_fte(device)
    device.press_back(1)


def force_exit_activity(device):
    os.system('adb -s %s shell am force-stop ' % device.get_device_id() + config.package)


def exit_activity(device):
    device.press_back(1)
    for i in range(10):
        if not checkpic.saved_pic_check(device.get_device(), "Common", 0.9, 2, "exit_confirm", False):
            device.press_back(2)
        else:
            device.touch_pos(700, 1560, 1)
            return True
    return False


def is_new_account(device):
    if checkpic.saved_pic_check(device.get_device(), "Common", 0.9, 3, "new_account", False):
        return True
    return False


def do_profile_fte(device):
    if checkpic.saved_pic_check(device.get_device(), "Common", 0.9, 4, "guide_conversation", False):
        device.touch_pos(700, 1150, 1)
        device.touch_pos(310, 820, 1)
        device.touch_pos(310, 820, 1)
        name = str(time.time())
        device.type(name)
        device.touch_pos(700, 1150)
        force_exit_activity(device)
        os.system('python common/sqlExecute.py update userprofile set gmFlag=1 where name="%s"' % name)
        device.start_activity()
        if not start_complete(device):
            device.screen_shot_to_fault("common", 99)
        device.touch_pos(70, 70, 1)
    if checkpic.saved_pic_check(device.get_device(), "Common", 0.9, 7, "guide_conversation", False):
        device.touch_pos(700, 1150, 1)
        device.touch_pos(1100, 2450)
        device.touch_pos(310, 820)
        device.touch_pos(700, 1150)
        device.press_back(1)
        if not checkpic.saved_pic_check(device.get_device(), "Common", 0.9, 5, "account_normal"):
            print "do profile fte failed"
            raise BaseException


def switch_account(device, account='', pwd=''):
    device.touch_pos(70, 70)
    if not checkpic.saved_pic_check(device.get_device(), "Common", 0.9, 5, "account_normal", False):
        do_profile_fte(device)
    device.touch_pos(1350, 2450)
    device.touch_pos(220, 1000)
    if account == '':
        device.touch_pos(750, 2100, 1)
        device.touch_pos(450, 1600, 1)
        device.touch_pos(450, 1600, 35)
    else:
        device.touch_pos(750, 1920, 1)
        device.touch_pos(750, 1020, 5)
        if not checkpic.saved_pic_check(device.get_device(), "Common", 0.9, 6, "facebook_login"):
            print "can not open facebook"
            raise BaseException
        device.touch_pos(700, 1150, 1)
        device.type(account)
        device.touch_pos(700, 1300, 1)
        device.type(pwd)
        device.touch_pos(750, 1000, 5)
        device.touch_pos(750, 1000, 5)
        device.touch_pos(1080, 2400, 5)
        device.touch_pos(700, 1570, 5)
        device.touch_pos(700, 1570, 40)
