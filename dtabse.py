import os
import sqlite3
from encryption import getkey, encrypt, decrypt



def file_write(file_dir, file_name,  password):
       password = getkey(password)
       filepath = dirpath + '\\' + filename
		curr.execute("INSERT INTO CREDENTIALS (FILENAME,KEY) \
		VALUES ( ?,?,? )",(file_dir, file_name, password,));
		conn.commit()
		conn.close()
		encrypt(password,file_dir, file_name)
		os.popen('attrib +h (encrypted)' + file_name)
		os.remove(file_name)
     
        
        
def file_read(password): 
    
		password = getkey(password)
		files = curr.execute("SELECT FILENAME FROM CREDENTIALS WHERE KEY = ?",(password,));
		files = list(files)
		for i in range(len(files)):
			print(str(i+1)+"-"+str(files[i][0])+"/"+str(files[i][1]))
		index = int(input("Enter file Index: "))
		file_dir =str(files[index-1][0])
       file_name =str(files[index-1][1])
		conn.close()
		decrypt(password,file_dir, file_name)
		os.remove(file_name)
       
       
       
conn = sqlite3.connect('Credentials.db')
conn.text_factory = str
curr = conn.cursor()
curr.execute("SELECT name FROM sqlite_master WHERE type='table';")
try:
	curr.execute('''CREATE TABLE USER_INFO
	(ID INTEGER PRIMARY KEY    AUTOINCREMENT,
    FILEDIR CHAR    NOT NULL,
	FILENAME CHAR    NOT NULL,
	KEY      CHAR    NOT NULL);''')
except :
   pass
      
        
        
        
        
        
        
        