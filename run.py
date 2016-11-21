from xml.dom import minidom
from common import Log, analysexml
from common.Color import Color
from common import DeviceManager
import threading
import traceback
import shutil
import os

DM = DeviceManager.DeviceManager()
THREAD_POOL = []


def init():
    shutil.rmtree("log")
    shutil.rmtree("fault")
    os.mkdir("log")
    os.mkdir("fault")


def read_test_cases_xml():
    filename = 'testcases.xml'
    doc = minidom.parse(filename)
    root = doc.documentElement
    total_loops = int(analysexml.get_attrvalue(root, 'loops'))
    test_suites = []
    for node in root.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            test_suite = {
                'name': analysexml.get_attrvalue(node, 'name'),
                'loops': int(analysexml.get_attrvalue(node, 'loops')),
                'device_count': int(analysexml.get_attrvalue(node, 'device_count')),
                'cases': []
            }
            test_case_nodes = analysexml.get_xmlnode(node, 'testcase')
            for t_node in test_case_nodes:
                test_case = {
                    'name': analysexml.get_attrvalue(t_node, 'name'),
                    'loops': int(analysexml.get_attrvalue(t_node, 'loops'))
                }
                test_suite['cases'].append(test_case)
            test_suites.append(test_suite)

    Color.print_blue_text("===========================Start===========================")
    for i in range(total_loops):
        for test_suite in test_suites:
            devices = DM.apply_device(int(test_suite["device_count"]))
            t = threading.Thread(target=run_test_suite, args=(test_suite, devices))
            THREAD_POOL.append(t)
            Color.print_blue_text(">>>>>>>>>>>Start test suite: %s" % test_suite['name'])
            t.setDaemon(True)
            t.start()
    for t in THREAD_POOL:
        t.join()
    Color.print_blue_text("============================End============================")


def run_test_suite(test_suite, devices):
    for j in range(test_suite["loops"]):
        for test_case in test_suite['cases']:
            try:
                exec "from testcase import " + test_case['name']
            except Exception, e:
                Color.print_red_text(e + '\n' + traceback.print_exc())
            for k in range(test_case['loops']):
                Color.print_green_text("+++++++++++ start test case: %s" % test_case['name'])
                try:
                    exec "case = %s.%s(devices, '%s', '%s')" % (test_case['name'], test_case['name'], test_suite['name'], test_case['name'])
                    exec "case.set_up()"
                    exec "case.init()"
                    exec "if case.success: case.execute()"
                    exec "case.dispose()"
                except Exception, e:
                    Color.print_red_text(e)
                    Color.print_red_text(traceback.print_exc())
                finally:
                    Color.print_green_text("---------- end test case: %s" % test_case['name'])


if __name__ == "__main__":
    init()
    read_test_cases_xml()
