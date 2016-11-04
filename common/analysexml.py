from xml.dom import minidom


def get_attrvalue(node, attrname):
     return node.getAttribute(attrname) if node else ''


def get_nodevalue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''


def get_xmlnode(node,name):
    return node.getElementsByTagName(name) if node else []


def xml_to_string(filename='testcase.xml'):
    doc = minidom.parse(filename)
    return doc.toxml('UTF-8')


def get_xml_data(filename='testcase.xml'):
    doc = minidom.parse(filename) 
    root = doc.documentElement

    testcase_nodes = get_xmlnode(root, 'testcase')
    user_list=[]
    for node in testcase_nodes:
        user_module = get_attrvalue(node,'module') 
        user_name = get_attrvalue(node,'Name')
        user_loops = get_attrvalue(node,'loops')
        user = {
            'module': user_module,
            'Name': user_name,
            'loops': user_loops
        }
        user_list.append(user)
    return user_list


def test_xmltostring():
    print xml_to_string()


def load_xml():
    user_list = get_xml_data()
    for user in user_list :
        #print user['sex']
        print '-----------------------------------------------------'
        if user:
            user_str='module: %s\nName: %s\nloops:%d\n ' %(user['module'], user['Name'], int(user['loops']))
            print user_str
            print '====================================================='

if __name__ == "__main__":
    test_xmltostring()
