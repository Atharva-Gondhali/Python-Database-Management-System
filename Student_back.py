import mysql.connector

mydb = mysql.connector.connect( 
	host = "localhost", 
	user = "root", 
	passwd = "atharva123@mysql", 
	database = "project" )

my_cursor = mydb.cursor()

def add_std_database( f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11 ):
	command = "INSERT INTO students (first_name, last_name, father_name, \
									email_id, age, age_group, gender, \
									course, medical_com, address, phone_no) \
									VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

	values = ( f1.get(), f2.get(), f3.get(), f4.get(), f5.get(), f6.get(), 
			   f7.get(), f8.get(), f9.get(), f10.get(), f11.get() )

	my_cursor.execute( command, values )
	mydb.commit()