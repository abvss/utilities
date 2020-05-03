import csv
import pymysql as MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='amey',
    passwd='amey',
    db='abvss')
cursor = mydb.cursor()

csv_data = csv.reader(file('FORM_DATA.csv'))
for row in csv_data:
    sql = 'INSERT INTO abvss.person' \
'(first_name, middle_name, last_name,' \
'birth_date, gender,  gotra, blood_group, email, mobile_no,highest_qualification,' \
'marital_status,' \
'father_first_name,father_middle_name ,father_last_name,' \
'mother_first_name, mother_middle_name,mother_last_name,' \
'spouse_first_name, spouse_last_name, spouse_middle_name,' \
'sangh)' \
' VALUES("'+row[1]+'","'+row[2]+'","'+row[3]+'","'+row[5]+'","'+row[6]+'","'+row[7]+'","'+row[8]+'"'\
' ,"'+row[9]+'","'+row[10]+'","'+row[11]+'","'+row[12]+'"'\
' ,"'+row[13]+'","'+row[14]+'","'+row[15]+'"'\
' ,"'+row[17]+'","'+row[18]+'","'+row[19]+'"'\
' ,"'+row[20]+'","'+row[21]+'","'+row[22]+'","'+row[33]+'"'\
' );'

    print (sql)

    cursor.execute(sql)

mydb.commit()
cursor.close()
print("Done")