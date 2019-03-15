'''
Print properties about the selected file/folder
'''
import sys
import os
import datetime
import hashlib
import binascii


class Hash:
    def __init__(self, fp):
        self.fp = fp
        self.buffer_size = 65536
    
    def get_hash(self, h):
        ''' get hash
        Parameter:
            h: hash such as md5 ,<class '_hashlib.HASH'>
        Return:
            string: hex representation of the hash
        '''
        with open(self.fp, 'rb') as f:
            while True:
                buf = f.read(self.buffer_size)
                if len(buf) > 0:
                    h.update(buf)
                else:
                    break 
            return h.hexdigest()
    
    def get_bytes(self):
        with open(self.fp, 'rb') as f:
            return f.read()
    
    def get_md5(self):
        ''' get MD5 '''
        return self.get_hash(hashlib.md5())
    
    def get_sha1(self):
        return self.get_hash(hashlib.sha1())
    
    def get_sha256(self):
        return self.get_hash(hashlib.sha256())
    
    def get_crc32(self):
        return binascii.crc32(self.get_bytes())

def print_hash(fp):
    o = Hash(fp)
    print('MD5:', o.get_md5())
    print('SHA1:', o.get_sha1())
    print('SHA256:', o.get_sha256())
    print('CRC32: {0:08x}'.format(o.get_crc32()))

def print_modified_date(fp):
    ''' print modified date '''
    # get file modified date
    _mtime = os.path.getmtime(fp)
    _mdt = datetime.datetime.fromtimestamp(_mtime)
    print(f'Date modified: {_mdt}')

def analyze_file_type(fp):
    ''' analyze file type '''
#     if os.sendto.islink(fp):
#         print('Type: Link')
    if os.path.isfile(fp):
        print('Type: File')
        # print file size
        print('file size:', os.path.getsize(fp))
        # print hash
        print_hash(fp)
    elif os.path.isdir(fp):
        print('Type: Folder')
        # print file count
        _file_count, _total_size = get_file_count_size(fp)
        print('file count: {0:d}'.format(_file_count))
        print('total file bytes: {0:,d}'.format(_total_size))
    
def get_file_count_size(rootdir):
    ''' get file count
    Parameter:
        rootdir: root directory, string
    Return:
        integer: count of files
        integer: total size of files
    '''
    _count = 0
    _size = 0
    for root, _, files in os.walk(rootdir):
        for file in files:
            _count += 1
            fp = os.path.join(root, file)
            _size += os.path.getsize(fp)
    return _count, _size

def get_file_path():
    ''' get file sendto '''
    # get passed argument
    # [0]: sendto to this script
    # [1]: sendto to the selected file
    fp = sys.argv[1]
    
    # add r to escape back slash.
    # add double-quotes to handle space.
    print(f'Path: r"{fp}"')
    
    return fp

def main():
    ''' entry point '''
    # get file sendto
    fp = get_file_path()
    # analyze file type
    analyze_file_type(fp)
    # print modified date
    print_modified_date(fp)
    # prevent the console from closing
    input()


if __name__ == '__main__':
    main()
