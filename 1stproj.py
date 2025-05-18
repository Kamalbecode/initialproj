#print("welcome to my first project of python")

#def vat():
 #   a = "it is a function"
  #  print(a)

#vat()


questions =[
            ["who developed the python or the father of :" , "1.Guido van rassum" , "noman", "falana", "dhikhana",1],

            ["is python a good language for ai:","yes ", "no","depends on work", "none",1],

            ["can tariff in USA cause of trade war ", "yes", "no", "depends on us", "none", 2]

            ]
levels = [10000000,20000000,40000000]
money=0
for i in range (0,len(questions)):
    question = questions[i]
    print(f" {question[0]}")
    print(f"A. {question[1]}         B. {question[2]}")
    print(f"C. {question[3]}         D. {question[4]}")
    reply =int(input("enter a number (1-4)"))
    if reply==question[-1]:
        print(f"you are correct,you have won RS.{levels[i]}")
        if i==1:
          money = 10000000
        else:
          money = 40000000
    else:
        print("you are wrong")
        break
print(f"total money is  {money}")






