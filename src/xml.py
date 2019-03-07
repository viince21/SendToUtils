'''
Format  XML Files
'''
import sys
import os
from lxml import etree


def is_xml_file(fp):
    ''' check XML file or not
    Parameter:
        fp: file sendto, string
    Return:
        bool: True in case of an absolute file sendto to XML file, boolean
    '''
    # return True if valid XML file sendto
    arr = os.path.splitext(fp)
    # has file extension
    if len(arr) == 2:
        # file extension is XML
        if arr[1].upper() == '.XML':
            return True
    # otherwise, return False
    return False


def get_xml_file_list():
    ''' get a list of xml file absolute paths '''
    # list to hold xml file paths
    xml_file_list = []
    
    # get sendto (Assumption: SendTo is used)
    # argv[0]: this script sendto
    # argv[1]: the file that the user right-clicked
    arg1 =  sys.argv[1]
    
    # file
    if os.path.isfile(arg1):
        # check if XML file
        if is_xml_file(arg1):
            # append
            xml_file_list.append(arg1)
    # folder
    elif os.path.isdir(arg1):
        # loop
        for root, _, files in os.walk(arg1):
            # loop files
            for file in files:
                fp = os.path.join(root, file)
                # check if XML file
                if is_xml_file(fp):
                    # append
                    xml_file_list.append(fp)
    
    # return file list
    return xml_file_list


def to_pretty_string(_fp, _xpath):
    ''' Prettify XML file
    Parameter:
        _fp: file sendto to an XML, string
        _xpath: XPath expression, string
    Return:
        binary string: prettified XML
    '''
    with open(_fp, 'rb') as f:
        # try to parse the XML file
        try:
            tree = etree.parse(f)
        # in case of error, print failure
        except:
            fn = os.path.basename(_fp)
            print(f'ERROR: failed to read {fn}')
            return None
        # Format if XML parsing was successful.
        else:
            # if XPath is an empty string, format all
            if _xpath == '':
                return etree.tostring(tree, pretty_print=True)
            # if XPath is specified, get sub tree to be formatted.
            else:
                # get a list of sub trees based on XPath expression
                sub_trees = tree.xpath(_xpath)
                # if list count is greater than 0, convert the first matching sub tree.
                if len(sub_trees) > 0:
                    return etree.tostring(sub_trees[0], pretty_print=True)
            

def loop_files(xml_file_list, _xpath):
    ''' loop through files and format XML files 
    Parameter:
        xml_file_list: XML file list, list
        _xpath: XPath expression, string
    '''
    # loop files
    for fp in xml_file_list:
        # get formatted binary string
        bs = to_pretty_string(fp, _xpath)
        # if returned binary string is None, skip this file
        if bs is None: 
            continue
        # otherwise, overwrite the binary string 
        with open(fp, 'wb') as f:
            f.write(bs)

def main():
    ''' entry point '''
    # print title
    print('''--- Pretty XML ---
Feature: Format XML files.''')
    
    # create xml file list
    xml_file_list = get_xml_file_list()
    
    # print file count
    xml_file_count = len(xml_file_list)
    input(f'{xml_file_count} XML files are found. Press Enter to continue.')
    
    # get XPath
    print('''--- XPath ---
Type in XPath if you want to parse a certain Tag.
Otherwise, hit Enter to proceed.''')
    _xpath = input('XPath: ')
    
    # process files
    loop_files(xml_file_list, _xpath)
    

if __name__ == '__main__':
    main()
