#Maureen Mbugua
#12/02/2026
#string formating
#get string length

sentence="i sleep a lot"

string_length=len(sentence)

print(f"the length is:{string_length}")

#splitting a string
sentence_2="english mathematics"
split=sentence_2.split(" ")

print(f"the first subject is:",split[0])

#make everything CAPS
mpesa_code="ubcl26abmr"

capitalised=mpesa_code.upper()

print("new mpesa code:",capitalised)

#make everything small
mpesa_code="UBCL26AMBR"

decapitalized=mpesa_code.lower()

print("new mpesa code:",decapitalized)

#replacing  characters in a string

balance="209kes"
ammount_added="316kes"

cleaned_balance=balance.replace("kes","")

print("cleaned balance:",cleaned_balance)

cleaned_ammount_added=ammount_added.replace ("kes","")

print("cleaned ammount added:",cleaned_ammount_added)

new_balance=int(cleaned_balance)+int(cleaned_ammount_added)

print(f"the new balance is:",new_balance)