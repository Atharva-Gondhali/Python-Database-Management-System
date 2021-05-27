import mysql.connector

mydb = mysql.connector.connect( 
	host = "localhost", 
	user = "root", 
	passwd = "atharva123@mysql", 
	database = "project" )

my_cursor = mydb.cursor()