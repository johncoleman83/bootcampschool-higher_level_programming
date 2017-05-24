#!/usr/bin/python3
import os


# name of file containing copied text from intranet
# generate this page manually with ctrl/command 'a', 'c', 'v')
intrapage = 'intrapage.txt'

# string to find a match to begin writing file and file extension

ALPHA = 'guillaume@ubuntu:~/'

# ALPHA is beginning and end of writing for main file
C = '$ cat'
M = 'main.py'


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


def writeyourfile(line, prototype):
    global firstline
    s1 = e1 = s2 = 0
    for i in range(len(line)):
        if line[i] == ':':
            s1 = i + 2
        if line[i] == ',':
            e1 = i
            s2 = i + 2
            break
        if line[i] == '\n':
            e1 = i
    f1 = line[s1:e1]
    fout = open(f1, 'w')
    writeline = firstline + prototype
    fout.write(writeline)
    fout.close()
    os.chmod(f1, 500)
    if s2:
        f2 = line[s2:-1]
        fout = open(f2, 'w')
        writeline = '\n'
        fout.write(writeline)
        fout.close()


# parses list of lines from file and writes to new files one at a time
def parsefile(intrapage_list):
    l = 0
    while l < len(intrapage_list):
        line = intrapage_list[l]
        if 'Prototype:' in line:
            prototype = line[11:]
        else:
            prototype = ''
        if ALPHA in line and C in line and M in line:
            f = extractname(line)
            fout = open(f, 'w')
            l += 1
            while ALPHA not in intrapage_list[l]:
                line = intrapage_list[l]
                fout.write(line)
                l += 1
            fout.close()
            os.chmod(f, 500)
        elif 'File:' in line:
            writeyourfile(line, prototype)
        l += 1



if __name__ == '__main__':
    app()
