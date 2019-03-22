'''
list absolute file paths
'''
import sys
import os

class FList:
    def __init__(self, indir):
        ''' constructor '''
        if os.path.isdir(indir):
            self.indir = indir
            print('Selected Folder: {0}'.format(self.indir))
        else:
            print('ERROR: Not Folder')
            sys.exit()
    
    @property
    def file_list(self):
        ''' create absolute file path list '''
        result = []
        for root, _, files in os.walk(self.indir):
            for file in files:
                fp = os.path.join(root, file)
                result.append(fp)
        return result
    
    def file_list_to_yaml(self):
        ''' dump file list to text file ''' 
        fn = '_filelist(utf-8).txt'
        outfp = os.path.join(self.indir, fn)
        data = '\n'.join(self.file_list)
        with open(outfp, 'w', encoding='utf-8') as f:
            f.write(data)
            print('{0} was created in {1}.'.format(fn, self.indir))

def main():
    print('''--- file list ---''')
    # get argument1
    argv1 = sys.argv[1]
    # create file list
    o = FList(argv1)
    o.file_list_to_yaml()


if __name__ == '__main__':
    main()

