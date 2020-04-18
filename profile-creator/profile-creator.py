# -*- coding: utf-8 -*
import xlrd 
import pdfkit  
import copy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}



def readProfileTemplate():
    file = open('profile.html',mode='r')
    all_of_it = file.read()
    file.close()
    return all_of_it



loc = ("data.xlsx") 
  
wb = xlrd.open_workbook(loc)#, #encoding_override="utf-8") 
sheet = wb.sheet_by_index(0) 

master_profile = readProfileTemplate()

flag = int(0)

profile1 = str()
profile2 = str()
profile3 = str()
counter = 0
for i in range(sheet.nrows): 

    if flag == 0:
        profile1 = copy.copy(master_profile)
        profile2 = copy.copy(master_profile)
        profile3 = copy.copy(master_profile)
        flag=1

    #print(sheet.cell_value(i, 0))
    profile1 = profile1.replace('#'+str(counter)+'#', str(sheet.cell_value(i, 1)))
    profile2 = profile2.replace('#'+str(counter)+'#', str(sheet.cell_value(i, 2)))
    profile3 = profile3.replace('#'+str(counter)+'#', str(sheet.cell_value(i, 3)))
    counter += 1
    if counter == 18:
        pdfkit.from_string(profile1, '1.pdf', options)
        pdfkit.from_string(profile2, '2.pdf', options)
        pdfkit.from_string(profile3, '3.pdf', options)