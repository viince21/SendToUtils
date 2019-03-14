'''
Compress sub directories
'''
import sys
import os
import shutil


def get_subdirs():
    ''' get sub directories '''
    # read the passed argument
    rootdir = sys.argv[1]
    # if directory is passed
    if os.path.isdir(rootdir):
        subdirs = []
        for name in os.listdir(rootdir):
            path = os.path.join(rootdir, name)
            if os.path.isdir(path):
                subdirs.append(path)
        return subdirs
    # if passed argument is not a directory
    else:
        print('The passed item is not a folder.')
        sys.exit()


def zip_folder(p):
    ''' ZIP folder
    Parameters:
        p: absolute path to a folder, string
    '''
    shutil.make_archive(p, 'zip', root_dir=p)
    print('Archived: {}'.format(os.path.basename(p)))


def main():
    ''' entry point '''
    print('--- ZIP Sub Directories ---')
    # get file 
    subdirs = get_subdirs()
    for subdir in subdirs:
        zip_folder(subdir)


if __name__ == '__main__':
    main()