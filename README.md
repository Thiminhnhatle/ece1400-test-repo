Part 2:
# python generatedata.py 1000 600 50 "ref_1 txt" "read_1.txt"
# /Users/nhatle/Desktop
# reference length:  1000
# number read:  600
# read length:  50
# python generatedata.py 10000 6000 50 "ref_2.txt" "reads_2.txt"
# /Users/nhatle/Desktop
# reference length:  10000
# number read:  6000
# read length:  50
# python generatedata.py 100000 600000 50 "ref_3.txt" "reads_3.txt"
# /Users/nhatle/Desktop
# reference length:  100000
# number read:  600000
# read length:  50
If my code works properly for my test data, I belive it will work correctly for other datasets
I should expect an exact 15% / 75% / 10% distribution for the reads that align zero, one, and
two times. I think that wrong entering data or how you understand a problem, will affect the result
I spend writing the code for 2,5 days.

Part 3:
# python processdata.py ref_1.txt reads_1.txt align_1.txt
# reference length:  1000
# number read:  600
# elapsed time:  0.004067897796630859
# python processdata.py ref_2.txt reads_2.txt align_2.txt
# reference length:  10000
# number read:  6000
# elapsed time:  0.17246794700622559
I spend writing the code for 2 days
