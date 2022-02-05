import sys
import time

error_msg = 'Usage :$ python processdata.py <ref_file> <reads_file> <align_file>'

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches
try:
    #ref_file, reads_file, align_file = input("").split()
    start = time.time()
    ref_file = sys.argv[1]
    reads_file = sys.argv[2]
    align_file = sys.argv[3]

    # Read ref_file
    f = open(ref_file, "r")
    ref_str = f.read()
    f.close()
    #print(ref_str)
    ref_length = len(ref_str)

    # Read reads_file
    f = open(reads_file, "r")
    reads_file = []
    for line in f:
        reads_file.append(line.splitlines())
    f.close()
    nreads = len(reads_file)

    # process align file
    align_list = []
    for i in reads_file:    
        align_list.append([i[0], list(find_all(ref_str, i[0]))])

    # write align_file
    f = open(align_file,"a") # append mode
    for line in align_list:
        pos = ""
        for i in line[1]:
            pos = pos + " "+ str(i)
        #print(pos)
        if pos == "": pos = "-1"
        f.write(line[0]+" "+pos+"\n")
    f.close()
    end = time.time()
    print('reference length: ',ref_length)
    print('number read: ',nreads)
    print('elapsed time: ',end - start)
except ValueError:
    print(error_msg)
except IndexError:
    print(error_msg)