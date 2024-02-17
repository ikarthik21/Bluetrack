import os
from clients.ftp import FTPClient

def _pjoin(paths):
    return "/".join(paths)

def dump_ftp_directory(mac_address, destination_directory):
    try:
        c = FTPClient(mac_address)
        c.connect()

        dump_recurse(c, (), destination_directory)

        c.disconnect()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def dump_recurse(client, path, save_path=None):
    offset = len(path)
    if len(path) > 0:
        client.setpath(path[-1])

    if save_path:
        try:
            os.makedirs(save_path + "/" + _pjoin(path))
        except OSError as e:
            pass

    dirs, files = client.listdir()

    for f in files:
        print("\t" * offset + f)
        if save_path:
            _, data = client.get(f)
            fpath = _pjoin([save_path, _pjoin(path), f])
            with open(fpath, "wb") as fd:
                fd.write(data)

    for d in dirs:
        print("\t" * offset + "> " + d)
        new_path = path + (d,)
        dump_recurse(client, new_path, save_path)

    if len(path) > 0:
        client.setpath(to_parent=True)

if __name__ == "__main__":
    mac_address = input("Enter MAC address: ")
    destination_directory = input("Enter destination directory: ")

    success = dump_ftp_directory(mac_address, destination_directory)

    if success:
        print("FTP directory dumped successfully.")
    else:
        print("Failed to dump FTP directory.")
