#import random library
import random
#declare spanish dict
low = "abcdefghijklmnñopqrstuvwxyz"
upp = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
num = "0123456789"
symb = "!$%&(){}+-¿?"
#save all in one var
all = low+upp+num+symb
#Define lenght of password
lenght = 12
#create random pass
passw = "".join(random.sample(all,lenght))

print(passw)