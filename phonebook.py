import os
import sys
from xml.etree import ElementTree
from xml.dom import minidom
from nOBEX import headers
from nOBEX.common import OBEXError
from nOBEX.xml_helper import parse_xml
from clients.pbap import PBAPClient

def usage():
    sys.stderr.write("Usage: %s [SIM]\n" % sys.argv[0])

def dump_xml(element, file_name):
    rough_string = ElementTree.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_string = reparsed.toprettyxml()
    with open(file_name, 'w') as fd:
        fd.write('<?xml version="1.0"?>\n<!DOCTYPE vcard-listing SYSTEM "vcard-listing.dtd">\n')
        fd.write(pretty_string[23:])  # skip xml declaration

def get_file(c, src_path, dest_path, verbose=True, folder_name=None, book=False):
    if verbose:
        if folder_name is not None:
            print("Fetching %s/%s" % (folder_name, src_path))
        else:
            print("Fetching %s" % src_path)

    if book:
        mimetype = b'x-bt/phonebook'
    else:
        mimetype = b'x-bt/vcard'

    hdrs, card = c.get(src_path, header_list=[headers.Type(mimetype)])
    with open(dest_path, 'wb') as f:
        f.write(card)

def dump_dir(c, src_path, dest_path):
    src_path = src_path.strip("/")

    try:
        os.makedirs(dest_path)
    except OSError as e:
        pass

    hdrs, cards = c.get(src_path, header_list=[headers.Type(b'x-bt/vcard')])

    if len(cards) == 0:
        print("WARNING: %s is empty, skipping" % src_path)
        return

    names = []
    root = parse_xml(cards)
    dump_xml(root, "/".join([dest_path, "listing.xml"]))
    for card in root.findall("card"):
        names.append(card.attrib["handle"])

    c.setpath(src_path)

    for name in names:
        fname = "/".join([dest_path, name])
        try:
            get_file(c, name, fname, folder_name=src_path)
        except OBEXError as e:
            print("Failed to fetch", fname, e)

    depth = len([f for f in src_path.split("/") if len(f)])
    for i in range(depth):
        c.setpath(to_parent=True)

def extract_phonebook(device_address, dest_dir, sim=False):
    if sim:
        prefix = "SIM1/"
    else:
        prefix = ""

    c = PBAPClient(device_address)
    c.connect()

    dump_dir(c, prefix + "telecom/pb", os.path.join(dest_dir, prefix + "telecom/pb"))
    dump_dir(c, prefix + "telecom/ich", os.path.join(dest_dir, prefix + "telecom/ich"))
    dump_dir(c, prefix + "telecom/och", os.path.join(dest_dir, prefix + "telecom/och"))
    dump_dir(c, prefix + "telecom/mch", os.path.join(dest_dir, prefix + "telecom/mch"))
    dump_dir(c, prefix + "telecom/cch", os.path.join(dest_dir, prefix + "telecom/cch"))

    c.setpath(prefix + "telecom")
    get_file(c, "pb.vcf", os.path.join(dest_dir, prefix + "telecom/pb.vcf"),
             folder_name=prefix + "telecom", book=True)
    get_file(c, "ich.vcf", os.path.join(dest_dir, prefix + "telecom/ich.vcf"),
             folder_name=prefix + "telecom", book=True)
    get_file(c, "och.vcf", os.path.join(dest_dir, prefix + "telecom/och.vcf"),
             folder_name=prefix + "telecom", book=True)
    get_file(c, "mch.vcf", os.path.join(dest_dir, prefix + "telecom/mch.vcf"),
             folder_name=prefix + "telecom", book=True)
    get_file(c, "cch.vcf", os.path.join(dest_dir, prefix + "telecom/cch.vcf"),
             folder_name=prefix + "telecom", book=True)

    c.disconnect()
    return 0

def main():
    if not 1 <= len(sys.argv) <= 2:
        usage()
        return -1
    elif len(sys.argv) == 2:
        if sys.argv[1] == "SIM":
            sim_flag = True
        else:
            usage()
            return -1
    else:
        sim_flag = False

    device_address = input("Enter the target device address (MAC): ")
    dest_dir = input("Enter the destination directory: ")

    extract_phonebook(device_address, dest_dir, sim=sim_flag)
    return 0

if __name__ == "__main__":
    sys.exit(main())
