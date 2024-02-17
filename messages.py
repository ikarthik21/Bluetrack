import os
import sys
from xml.etree import ElementTree
from nOBEX import headers
from nOBEX.common import OBEXError
from nOBEX.xml_helper import parse_xml
from clients.map import MAPClient

def dump_xml(element, file_name):
    fd = open(file_name, 'wb')
    fd.write(b'<?xml version="1.0" encoding="utf-8" standalone="yes" ?>\n')
    fd.write(ElementTree.tostring(element, 'utf-8'))
    fd.close()

def get_file(c, src_path, dest_path, verbose=True, folder_name=None):
    if verbose:
        if folder_name is not None:
            print("Fetching %s/%s" % (folder_name, src_path))
        else:
            print("Fetching %s" % src_path)

    req_hdrs = [headers.Type(b'x-bt/message'),
                headers.App_Parameters(b'\x0A\x01\x01\x14\x01\x01')]
    hdrs, card = c.get(src_path, header_list=req_hdrs)
    with open(dest_path, 'wb') as f:
        f.write(card)

def dump_dir(c, src_path, dest_path):
    src_path = src_path.strip("/")

    hdrs, cards = c.get(src_path, header_list=[headers.Type(b'x-bt/MAP-msg-listing')])

    if len(cards) == 0:
        return

    try:
        os.makedirs(dest_path)
    except OSError:
        pass

    names = []
    root = parse_xml(cards)
    dump_xml(root, "/".join([dest_path, "mlisting.xml"]))
    for card in root.findall("msg"):
        names.append(card.attrib["handle"])

    c.setpath(src_path)

    for name in names:
        get_file(c, name, "/".join([dest_path, name]), folder_name=src_path)

    depth = len([f for f in src_path.split("/") if len(f)])
    for i in range(depth):
        c.setpath(to_parent=True)

def extract_messages(device_address, dest_dir):
    c = MAPClient(device_address)
    c.connect()
    c.setpath("telecom")
    c.setpath("msg")

    dirs, _ = c.listdir()
    for d in dirs:
        dump_dir(c, d, os.path.join(dest_dir, "telecom/msg", d))

    c.disconnect()

def main():
    if len(sys.argv) != 1:
        sys.stderr.write("Usage: %s\n" % sys.argv[0])
        return 1

    device_address = input("Enter the target device address (MAC): ")
    dest_dir = input("Enter the destination directory: ")

    extract_messages(device_address, dest_dir)
    return 0

if __name__ == "__main__":
    sys.exit(main())
