from bluetooth import *
from dtabse import file_read, file_write

def finding_bluetooth():   
   print ("Performing Inquiry! ")
   print("Finding devices...")

   ## geting the nearby devices with active bluetooth
   try :
       
       nearby_devices = discover_devices(lookup_names = True)
       for i in range (len(nearby_devices)):   
            print ("found %d devices" % (i+1, len(nearby_devices)))
   except:
       print("Not Found !!")        

   j = int(input("Select your device else or search again (0):  "))
   
   if (j == 0):
       return finding_bluetooth()
   elif (j) :
       return nearby_devices[j-1][0]
   else :
       print(" Exiting !! ")
       return(-1)
       
   
    
def Main():
       addr = finding_bluetooth()
       if( addr != (-1)):
           
            choice = raw_input("Want to encrypt(E) or decrypt(D) the file or Exit(0) : ")
     
            if choice=='D': 
                  passw = raw_input("Enter the passward: ")
                  my_key = addr + passw
                  file_read( my_key)
         
            elif choice=='E':
                   passw = raw_input("Enter your passward: ")
                   my_key = addr + passw
                   dirpath = " "
                   dirpath = raw_input("Enter the diectory pathof the file to be encrypted : ")
                   filename = raw_input("Enter the file name you want to encrypt : ")
                   file_write(dirpath,filename, my_key)
     
            else:
                print(" No operation wanted :   ")
                
 

if __name__ == '__main__':
      Main()               