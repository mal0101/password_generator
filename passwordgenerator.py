import random       




chars = ['.', '+','-','*','/',',','?',';',':','§','!','&','"','#','{','}','(',')','[',']','-','|','`','_','^','@','=','$','%','<','>']
lets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

random.shuffle(chars)
random.shuffle(lets)

incCaps = False
incNums = False
incChar = False


i = 0



ohh = int(input('How many characters do you want your password to have? (minimum 4)'))
caps = str(input('Do you want your password to have a capital letter? (Yes/No)'))
if caps == 'Yes':
    incCaps = True
nums = str(input('Do you want your password to have numbers? (Yes/No)'))
if nums == 'Yes':
    incNums = True
characters = str(input('Do you want your password to have special characters? (Yes/No)'))
if characters == 'Yes':
    incChar = True

password = ''  
while i < ohh:
    password += random.choice(lets)
    i +=1
    if incCaps and i < ohh :
        password += random.choice(lets).upper()
        i += 1
    if incNums and i < ohh :
        password += str(random.randint(0,10))
        i += 1
    if incChar and i < ohh :
        password += random.choice(chars)
        i += 1              


random.shuffle(list(password))
password.join('')
print(password)  

#while True:
#    m = 0
#    ho = str(input('Would you like to save your password? (Yes/No)'))
#    if ho == 'Yes' :
#        m += 1


#    passwords = {m : password}
#print(passwords)
