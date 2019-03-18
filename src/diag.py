'''
Create diagram
'''
import sys
import os
import subprocess


# key = type of diagram, value = executable name
diags = {'actdiag': 'actdiag.exe',
         'blockdiag': 'blockdiag.exe',
         'nwdiag': 'nwdiag.exe',
         'packetdiag': 'packetdiag.exe',
         'rackdiag': 'rackdiag.exe',
         'seqdiag': 'seqdiag.exe'}


def get_scripts_folder():
    ''' get Scripts folder '''
    # get absolute file path of python.exe or pythonw.exe
    exe = sys.executable
    # get python.exe parent folder
    parent = os.path.dirname(exe)
    # get Scripts folder
    scripts = os.path.join(parent, 'Scripts')
    # return Scripts folder
    return scripts


def create_diagram(diag_fp, scripts_dir):
    ''' create diagram '''
    # open diagram file
    try:
        with open(diag_fp, 'r', encoding='ascii') as f:
            # read text contents
            s = f.read()
            # loop through dictionary
            for key, val in diags.items():
                # check if text contents starts with valid diagram name
                if s.startswith(key):
                    # print diagram type
                    print(key)
                    # create diagram file path
                    exe = os.path.join(scripts_dir, val)
                    # create diagram
                    subprocess.run([exe, diag_fp])
                    # break
                    break
            # in case of no matching diagram type, notify the user
            else:
                print('ERROR: Diagram name not detected!')
    # if failed to read file.
    except:
        print('ERROR: Failed to read file.')


def main():
    ''' entry point '''
    print('--- Create Diagram ---')
    scripts_dir = get_scripts_folder()
    diag_fp = sys.argv[1]
    create_diagram(diag_fp, scripts_dir)


if __name__ == '__main__':
    main()

