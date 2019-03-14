'''
Delete sub directories
'''
import sys
import os
import shutil


def get_subdir_list(folder_name):
    ''' get sub directories 
    Parameter:
        folder_name: folder name, string
    Return:
        absolute folder paths, list
    '''
    # read the passed argument
    rootdir = sys.argv[1]
    # if directory is passed
    if os.path.isdir(rootdir):
        subdirs = []
        # loop
        for root, dirs, _ in os.walk(rootdir):
            for d in dirs:
                # check folder name
                if d.upper() == folder_name.upper():
                    # populate list
                    full_path = os.path.join(root, d)
                    subdirs.append(full_path)
                    # print
                    print('Found: {0}'.format(full_path))
        return subdirs
    # if passed argument is not a directory
    else:
        print('The passed item is not a folder.')
        sys.exit()


def delete_folders(folder_list):
    ''' delete folders
    Parameter:
        folder_list: folders to be deleted, list
    '''
    for folder in folder_list:
        shutil.rmtree(folder)
        print('deleted: {0}'.format(folder))
        
        
def double_check(folder_name, folder_list):
    ''' double check folder name and then delete folders
    Parameter:
        folder_name: folder name, string
        folder_list: list of absolute folder paths, list
    '''
    # exit if not found, exit
    folder_count = len(folder_list)
    if folder_count == 0:
        print('folder name {0} was not found.'.format(folder_name))
        sys.exit()
    else:
        print('Found founder count = {0:d}'.format(folder_count))
    
    # prompt folder name again for sanity check
    print('--- Double Check ---')
    folder_name_check = get_folder_name()
    if folder_name.upper() == folder_name_check.upper():
        delete_folders(folder_list)
    # exit in case of typo
    else:
        print('Input Error: {0} <> {1}'.format(folder_name, folder_name_check))
        sys.exit()


def get_folder_name():
    ''' get folder name with input prompt 
    Return
        folder name, string
    '''
    folder_name = input('Folder name to delete recursively: ')
    return folder_name


def main():
    ''' entry point '''
    print('--- Delete Sub Directories ---')
    # get folder name
    folder_name = get_folder_name()
    # get directory list
    folder_list = get_subdir_list(folder_name)
    # delete
    double_check(folder_name, folder_list)


if __name__ == '__main__':
    main()
