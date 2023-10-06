import random 
def generate_password(length):
    len=int(input("Enter length of password :"))
    combination="ABCDEFGHIJKLMNOPQRSTUVWXYabchdefghijklmnopqrstuvwxyz123456789#@$%^&*()"
    password=" ".join(random.sample(combination,len))
    
    return password    
    
if __name__ == "__main__":  
        password=generate_password(len)
        print(f"Your password {password}")






















#import random

#combination="ABCDEFGHIJKLMNOPQRSTUVWXYabchdefghijklmnopqrstuvwxyz123456789#@$%^&*()"

#len=int(input("Enter length of password :"))
#password=" ".join(random.sample(combination ,len))
#print(f"Your password {password}")