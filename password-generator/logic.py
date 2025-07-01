import random,string
from datetime import datetime

def generate_password(fullname,dob,length):
    
    fullname = fullname.strip().replace(' ','')
    dob = dob.strftime("%d%m%Y")    
    characters = fullname + dob + string.punctuation[:7]
    password = "".join(random.choices(characters,k = length))

    return password

            
 

