import os
while(True):
    #os.system('cls')
    
    p=input("\n==================================================================\nHi Enter user name: ")
    print("--------------------Hi "+p+"------------------------------")
    a=int(input("How many strings you want to compare : "))

    if a >1 and a<=5:
        
        b=[]
        count=0
        for i in range(a):
            c=input("Enter string "+str(i+1)+" :")
            if c.isalpha():
                b.append(c)
            else:
                print("You have entered an invalid input")
                count=1
                break
            
        
        if count!=1:
            if a==2:
                imp=input("Do you want to add another string press y/n : " )
            if imp=="y":
                      b.append(input("Please Enter string 3 :"))
                      a+=1
            else:
                pass
            print("Press 'v' for vowels\npress 'c' for consonets\npress 'vc' for both vowels and consonets")
            k=input("Please provide your input: ")
            for i in b:
                vowel=["a","e","i","o","u","A","E","I","O","U"]
                V=0
                C=0
        
                for j in i:
                    if j in vowel:
                        V+=1
                    else:
                        C+=1
            
                if k=='v':
                    print("The vowels count in "+i+" string is : " +str(V))
                elif k=='c':
                    print("The Consonets count in "+i+" string is : " +str(C))
                elif k=='vc':
                    print("The vowels count in "+i+" string is : " +str(V))
                    print("The Consonets count in "+i+" string is : " +str(C))
        else:
            break
                
    else:
        inp=input("Sorry You have Entered invalid integer\n If you want to reset press y \n If you want to exit press n :")
        if inp=="y" or inp=="Y":
            pass
        else:
            break
