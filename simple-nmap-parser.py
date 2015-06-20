__author__ = 'fl64'
import xml.etree.ElementTree as ET
tree = ET.parse('/home/user/nmap-scans/homenet.xml')
root = tree.getroot()
for child in root:
        print (child.tag, child.attrib)
        if ((child.tag == 'host') and (child.find('status').attrib['state'] == 'up')): print (child.find('address').attrib['addr'])