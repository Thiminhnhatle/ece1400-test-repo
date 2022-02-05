import sys
import random  

error_msg = 'Usage :$ python generatedata.py <ref_length> <nreads> <read_len> <ref_file> <reads_file>'

def write_file(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()

try:
    #ref_length, nreads, read_len, ref_file, reads_file = input("").split()
    #ref_length = int(ref_length)
    #nreads = int(nreads)
    #read_len = int(read_len)
    ref_length = int(sys.argv[1])
    nreads = int(sys.argv[2])
    read_len = int(sys.argv[3])
    ref_file = sys.argv[4]
    reads_file = sys.argv[5]

    # Define the characters
    spec_char = 'acgt'
    # Get the length of 75% and 25%
    len_75 = round(ref_length*75/100)
    len_25 = ref_length - len_75
    
    #print(len_75)
    #print(len_25)
    
    # Generate string of characters above and have length is len_75
    str_75 = ''.join((random.choice(spec_char)) for x in range(len_75))  
    str_75 = str_75.upper()

    #get 25% string from 75% string
    str_25 = str_75[-len_25:]
    #print(str_75)
    #print(str_25)

    # Concat those strings
    final_str = str_75 + str_25
    #print(final_str)    
    write_file(ref_file, final_str)
    
    read_lst = []
    for i in range(0, nreads):
        ran_pos = random.randint(0,(ref_length-read_len))
        ran_pos = int(ran_pos)
        read_str = final_str[ran_pos:ran_pos + 50]
        read_lst.append(read_str)
    # 1000 600 50 "reference_test.txt" "reads_test.txt"
    # Write read list to file
    import os
    print(os.path.abspath(os.getcwd()))
    file=open(reads_file,'w')
    for items in read_lst:
        file.writelines(items+'\n')
    file.close()

    print('reference length: ',ref_length)
    print('number read: ',nreads)
    print('read length: ',read_len)
except ValueError:
    print(error_msg)
except IndexError:
    print(error_msg)
