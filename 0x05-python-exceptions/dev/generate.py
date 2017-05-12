#!/usr/bin/python3
import os


# name of file containing copied text from intranet
# generate this page manually with ctrl/command 'a', 'c', 'v')
intrapage = 'intrapage.txt'

# string to find a match to begin writing file and file extension
M = 'main.py'

# string to find a match to end writing a file
END = 'guillaume@ubuntu:'

# first line to write to your files
firstline = '#!/usr/bin/python3\n'


# main function
def app():
    intrapage_list = initialize()
    parsefile(intrapage_list)
    print('*******************', '** SWEET SUCCESS **', '*******************',
          sep='\n')


# initialize file as list
def initialize():
    fout = open(intrapage, 'r')
    intrapage_list = fout.readlines()
    fout.close()
    return intrapage_list


#extracts filename from line from file
def extractname(aline):
    s = aline.index(M)
    i = s
    while aline[i] != ' ':
        i -= 1
    i += 1
    filename = aline[i:s] + M
    return filename


def writeyourfile(aline):
    f = aline[6:-1]
    fout = open(f, 'w')
    fout.write(firstline)
    fout.close()
    os.chmod(f, 500)


# parses list of lines from file and writes to new files one at a time
def parsefile(intrapage_list):
    l = 0
    while l < len(intrapage_list):
        line = intrapage_list[l]
        if ('cat ' and M in line) and './' not in line:
            f = extractname(line)
            fout = open(f, 'w')
            l += 1
            while END not in intrapage_list[l]:
                line = intrapage_list[l]
                fout.write(line)
                l += 1
            fout.close()
            os.chmod(f, 500)
        elif 'File:' in line:
            writeyourfile(line)
        l += 1



if __name__ == '__main__':
    app()
