
#this program is made for counting the letter which shows is it present or not in string
letter1 = input("enter your letter:")
SubjectName= "marahdrfd;iulysgl,kthhhhhi marathi"
value = SubjectName.count(letter1)
if value>0:
    print(letter1 + " is present" +str(value))
else:
    print(letter1 +" not present" + str(value))
    
    
    
    
    
    
    
    
##### use find method

x = SubjectName.find("marathi")
print(x)



name = "dashbrard/joint/unverse"




#split method
print(name.split('/')[2])