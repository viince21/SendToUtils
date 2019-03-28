'''
GREP lines with regular expression
'''
import sys
import re
import os


class Grep:
    @staticmethod
    def create_pattern(s):
        ''' create regular expression pattern
        Parameter:
            _s: search pattern, string
        Return:
            p: pattern, <class 're.Pattern'>
        Remark:
            Close the expression with .*
        '''
        # compile
        try:
            pattern = re.compile(s)
        # exit in case of error
        except re.error:
            print(f'Regex Pattern ({s}) is not valid!')
            sys.exit()
        # return
        return pattern
    
    @staticmethod
    def create_filelist(p):
        ''' create file list
        Parameter:
            p: path passed by SendTo command, string
        Return:
            absolute file paths, list
        Remark:
            if path is not valid, exit
        '''
        # list of absolute file paths
        filelist = []
        # file
        if os.path.isfile(p):
            filelist.append(p)
        # folder
        elif os.path.isdir(p):
            for root, _, files in os.walk(p):
                for file in files:
                    fp = os.path.join(root, file)
                    filelist.append(fp)
        # error
        else:
            print(f'ERROR: {p} is not a valid path.')
            sys.exit()
        # return
        return filelist

    @staticmethod
    def grep_lines(_filelist, _encoding, _pattern):
        ''' search lines from files in regular expression
        Parameter:
            _filelist: absolute file paths, list
            _encoding: encoding (utf-8 ascii cp932), string
            _pattern: compiled regular expression, <class 're.Pattern'>
        Return:
            search result, string
        '''
        # result string to be returned
        result = ''
        # loop files
        for fp in _filelist:
            print('\rReading {0}'.format(os.path.basename(fp)), end='')
            # errors should be ignored
            with open(fp, 'r', errors='ignore') as f:
                # loop lines
                for line in f.readlines():
                    # add to result if matching
                    m = _pattern.match(line)
                    if m:
                        result += line
        # return
        return result

    @staticmethod
    def validate_encoding(_encoding):
        ''' validate the passed encoding
        Parameter:
            _encoding: encoding name, string
        Remark:
            exit if invalid
        '''
        # use the path of this very script for open() test
        fp = os.path.realpath(__file__)
        try:
            with open(fp, 'r', encoding=_encoding) as f:
                print(f'{_encoding} is a valid encoding')
        except LookupError:
            print(f'{_encoding} is not a valid encoding.')
            sys.exit()
        else:
            f.close()
    
    @staticmethod
    def save_file(fp, data, encoding):
        ''' save file
        Parameter:
            fp: absolute file path, string
            data: to be written to file, string
            encoding: encoding name, string
        '''
        with open(fp, 'w', encoding=encoding) as f:
            f.write(data) 


def main():
    print('''--- GREP ---''')
    # create line file list
    argv1 = sys.argv[1]
    _filelist = Grep.create_filelist(argv1)
    
    # get regular expression pattern
    rgx = input('Type in Regular Expression: ')
    _pattern = Grep.create_pattern(rgx)
    
    # get encoding
    _encoding = input('Type in Encoding: ')
    Grep.validate_encoding(_encoding)
    
    # create output file path
    outdir = input('D&D output folder: ').replace('"', '')
    outfile = os.path.join(outdir, 'grep.txt')
    
    # get result
    result = Grep.grep_lines(_filelist, _encoding, _pattern)
    
    # write to file
    Grep.save_file(outfile, result, _encoding)


if __name__ == '__main__':
    main()

