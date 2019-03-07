'''
Visualize Folder Structure
'''

import os
import sys
import json


class Tree:
    '''
    visualize the folder structure in tree
    '''
    
    def __init__(self, root_folder, max_depth, include_files):
        ''' constructor
        Parameter:
            root_folder: absolute sendto to the folder, string
            max_depth:   how deep you dive, integer
            include_files: whether to include files, boolean
        '''
        self.max_depth   = max_depth
        root_dir_name = os.path.basename(root_folder)
        self.tree_dict   = {root_dir_name: {}}
        self.include_files = include_files
        self.scan_folder(
            cur_item=self.tree_dict[root_dir_name], 
            cur_dir=root_folder, 
            cur_depth=0)
    
    def scan_folder(self, cur_item, cur_dir, cur_depth):
        ''' scan the folder
        Parameter:
            cur_item:  specific item of self.tree_dict, dictionary value as list
            cur_dir:   current directory, string
            cur_depth: current depth, integer
        '''
        # Exit function 
        # if current depth is greater than maximum depth
        if cur_depth > self.max_depth: return
        
        # Loop through files/folders in current directory
        # "item" holds the base name, NOT the absolute sendto
        for item in os.listdir(cur_dir):
            # create absolute file/folder sendto
            fp = os.path.join(cur_dir, item)
            
            # file
            if os.path.isfile(fp) and self.include_files:
                # create key '.' to hold file list
                # '.' represent current directory
                # '.' is not allowed as a folder name; => no conflict with folder names.
                if not '.' in cur_item:
                    cur_item['.'] = []
                # append file name to the current directory list
                cur_item['.'].append(item)
            
            # folder
            elif os.path.isdir(fp):
                # Create a new key with the folder base name.
                # Set the value as a new dictionary instance
                cur_item[item] = {}
                _sub_item = cur_item[item]
                # increment depth
                _sub_depth = cur_depth + 1
                # current directory
                _sub_dir = os.path.join(cur_dir, item)
                # call back
                self.scan_folder(cur_item  = _sub_item, 
                                 cur_dir   = _sub_dir, 
                                 cur_depth = _sub_depth)
                

def get_positive_integer():
    ''' get a positive integer from the user 
    Return:
        integer
    '''
    s = input('Type in a positive integer: ')
    try:
        x = int(s)
    except ValueError:
        raise ValueError(f'Could not convert {s} to integer.')
    else:
        return x

def get_boolean():
    ''' get boolean from user input
    Return:
        boolean
    '''
    # get user input by 1 or 0
    s = input('1=Yes, 0=No: ')
    # return
    if s =='1':
        return True
    elif s == '0':
        return False
    # if input is invalid kill the execution
    else:
        raise ValueError('Input 1 or 0')

def main():
    # read the 1st argument
    argv1 = sys.argv[1]
    
    # file name
    fn = 'tree.json'
    
    # get a positive integer as max depth
    print('How deep do you want to recurse?')
    max_depth = get_positive_integer()
    
    # get boolean as files included
    print('Do you want to include files?')
    include_files = get_boolean()
    
    # if argv1 is a folder
    if os.path.isdir(argv1):
        # warning for file creation
        input(f'''Caution!
    Directory structure will be saved in this folder.
    The file name will be {fn}.
    Press Enter to proceed!''')
        o_tree = Tree(
            root_folder=argv1, 
            max_depth=max_depth,
            include_files=include_files)
        # print on json file.
        outfile = os.path.join(argv1, fn)
        with open(outfile, 'w') as f:
            json.dump(o_tree.tree_dict, f, indent=4)
    
    # if argv1 is not a folder
    else:
        # argument is not a folder
        print(f'''ERROR!
    passed parameter {argv1} is not a directory''')


if __name__ == '__main__':
    main()
