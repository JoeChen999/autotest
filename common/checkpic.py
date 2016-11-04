from __future__ import division

import math
import os

from com.android.monkeyrunner import MonkeyRunner

import config

max_check_point_count = 10000


def saved_pic_check(device, case_name, factor, check_num, name, fault=True):
    area = config.check_areas[name]
    return pic_check(device, case_name, factor, check_num, area['x'], area['y'], area['width'], area['height'], fault)


def pic_check(device, case_name, factor, check_num, x, y, width, height, fault=True):
    num = 0
    image1 = device.takeSnapshot()
    if not config.is_record:
        i = x
        rc = gc = bc = 0
        total = 255 * width * height / 4
        step = 1
        size = width * height
        if size >= max_check_point_count:
            step = int(math.sqrt(size / max_check_point_count))
        image2 = MonkeyRunner.loadImageFromFile('pic/%s_%d.png' % (case_name, check_num))
        while i < x + width:
            j = y
            while j < y + height:
                pa = image1.getRawPixel(i, j)
                pb = image2.getRawPixel(i, j)
                r = abs(pa[1] - pb[1])
                g = abs(pa[2] - pb[2])
                b = abs(pa[3] - pb[3])
                if r + g + b > 25:
                    rc = rc + r
                    gc = gc + g
                    bc = bc + b
                j += step
            i += step
        r_sub = rc / total
        g_sub = gc / total
        b_sub = bc / total
        pic_same = 1 - (r_sub + g_sub + b_sub) / 3
        if pic_same >= factor:
            return True
        else:
            if fault:
                while os.path.isfile('fault/error_%s_%d_%d.png' % (case_name, check_num, num)):
                    num += + 1
                    image2.writeToFile('fault/error_%s_%d_%d.png'
                                    % (case_name, check_num, num), 'png')
            return False
    else:
        image1.writeToFile('pic/%s_%d.png' % (case_name, check_num), 'png')
        return True
