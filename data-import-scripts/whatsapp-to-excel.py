
import sys
import csv


fileName = sys.argv[1]
chat = open(fileName, 'r') 
Lines = chat.readlines() 

profile = []
for line in Lines:
    num = line.split('\t')[0].strip() 
    if  len(num) == 1 and num.startswith('1'):
        profile = [None] * int(34)
        profile[1] = line.split('=')[1].strip()

    if  len(num) == 1 and num.startswith('2'):
        profile[2] = line.split('=')[1].strip()

    if  len(num) == 1 and num.startswith('3'):
        profile[3] = line.split('=')[1].strip()

    if  len(num) == 1 and num.startswith('4'):
        profile[4] = line.split('=')[1].strip()

    if  len(num) == 1 and num.startswith('5'):
        profile[5] = line.split('=')[1].strip()

    if  len(num) == 1 and num.startswith('6'):
        profile[6] = line.split('=')[1].strip()

    if  len(num) == 1 and num.startswith('7'):
        profile[7] = line.split('=')[1].strip()

    if  len(num) == 1 and num.startswith('8'):
        profile[8] = line.split('=')[1].strip()

    if  len(num) == 1 and num.startswith('9'):
        profile[9] = line.split('=')[1].strip()

    if  len(num) == 2 and num.startswith('10'):
        profile[10] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('11'):
        profile[11] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('12'):
        profile[12] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('13'):
        profile[13] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('14'):
        profile[14] = line.split('=')[1].strip()

    if  len(num) == 2 and num.startswith('15'):
        profile[15] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('16'):
        profile[16] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('17'):
        profile[17] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('18'):
        profile[18] = line.split('=')[1].strip()

    if  len(num) == 2 and num.startswith('19'):
        profile[19] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('20'):
        profile[20] = line.split('=')[1].strip()

    if  len(num) == 2 and num.startswith('21'):
        profile[21] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('22'):
        profile[22] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('23'):
        profile[23] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('24'):
        profile[24] = line.split('=')[1].strip()

    if  len(num) == 2 and num.startswith('25'):
        profile[25] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('26'):
        profile[26] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('27'):
        profile[27] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('28'):
        profile[28] = line.split('=')[1].strip()

    if  len(num) == 2 and num.startswith('29'):
        profile[29] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('30'):
        profile[30] = line.split('=')[1].strip()

    if  len(num) == 2 and num.startswith('31'):
        profile[31] = line.split('=')[1].strip()
    
    if  line.startswith('If Service'):
        profile[32] = line.split('=')[1].strip()
    
    if  len(num) == 2 and num.startswith('33'):
        profile[33] = line.split('=')[1].strip()
        profile.pop(0)
        with open("Profiles.csv", 'a+') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(profile)

