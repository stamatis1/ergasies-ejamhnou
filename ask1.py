import random
#b1 einai oi theseis pou mporoun na mpoun ta megala
b1=[0,3,6,9,12,15,18,21,24]
#b2 einai oi theseis pou mporoun na mpoun ta mesaia
b2=[1,4,7,10,13,16,19,22,25] 
#b3 einai oi theseis pou mporoun na mpoun ta mikra
b3=[2,5,8,11,14,17,20,23,26]
syn=0
for i in range(99):
    c=0
    flag = 0 
    count=0
    #my_list einai h lista pou mpainoun oi epiloges sthn opoia lista kathe 3 stoixeia apoteloyn to ena keli tou 3*3 pinaka  
    my_list=[" " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " ", " " , " " , " "]

    #A=megalo B=mesaio C=mikro
    board=['A','A','A','A','A','A','A','A','A','B','B','B','B','B','B','B','B','B','C','C','C','C','C','C','C','C','C']

    while flag==0 and c<=26:
        #eyresh epiloghs kai theshs
        #to x einai h thesh kai to y h epilogh 

             count=count+1 
             y=random.choice(board)
             
             if y=='A':
                 x = random.choice(b1)
                 board[x]= " "
             elif y=='B':
                 x = random.choice(b2)
                 board[x]= " "
             else:
                 x = random.choice(b3)
                 board[x]= " "

             if my_list[x] == " ":
                 my_list[x]=y 
             else:
                if y=='A':
                    x = random.choice(b1)
                    board[x]= " "
                elif y=='B':
                    x = random.choice(b2)
                    board[x]= " "
                else:
                    x = random.choice(b3)
                    board[x]= " "

                for i in range(2):
                   #elegxos gia triliza 
                   if my_list[i]==my_list[i+3] and my_list[i]==my_list[i+6] and my_list[i]!="":
                          flag = 1
                   elif my_list[i]==my_list[i+9] and my_list[i]==my_list[i+18] and my_list[i]!="":
                          flag = 1
                   elif my_list[i]==my_list[i+12] and my_list[i]==my_list[i+24] and my_list[i]!="":
                          flag = 1
                   elif my_list[i+3]==my_list[i+12] and my_list[i]==my_list[i+21] and my_list[i+3]!="":
                          flag = 1
                   elif my_list[i+6]==my_list[i+15] and my_list[i+6]==my_list[i+24] and my_list[i+6]!="":
                          flag = 1
                   elif my_list[i+9]==my_list[i+12] and my_list[i+9]==my_list[i+15] and my_list[i+9]!="":
                        flag = 1
                   elif my_list[i+18]==my_list[i+21] and my_list[i]==my_list[i+24] and my_list[i+18]!="":
                        flag = 1
                   elif my_list[i+6]==my_list[i+12] and my_list[i]==my_list[i+18] and my_list[i+6]!="":
                        flag = 1
                   elif my_list[i]=='A'  and   my_list[i+3]=='B' and my_list[i+6]=='C':
                        flag = 1
                   elif my_list[i]=='A'  and my_list[i+9]=='B'   and my_list[i+18]=='C':
                        flag = 1
                   elif my_list[i]=='A' and  my_list[i+12]=='B' and my_list[i+24]=='C':
                        flag = 1
                   elif my_list[i+3]=='A'  and  my_list[i+12]=='B' and my_list[i+21]=='C':
                        flag = 1
                   elif my_list[i+6]=='A'  and   my_list[i+15]=='B' and my_list[i+24]=='C':
                        flag = 1
                   elif my_list[i+9]=='A'   and   my_list[i+12]=='B' and my_list[i+15]=='C':
                        flag = 1
                   elif my_list[i+18]=='A'  and   my_list[i+21]=='B' and my_list[i+24]=='C':
                        flag = 1
                   elif my_list[i+6]=='A'  and    my_list[i+12]=='B' and my_list[i+18]=='C':
                        flag = 1
                   elif my_list[i]=='C'  and  my_list[i+3]=='B' and my_list[i+6]=='C':
                         flag = 1
                   elif my_list[i]=='C'  and my_list[i+9]=='B'   and my_list[i+18]=='A':
                        flag = 1
                   elif my_list[i]=='C' and  my_list[i+12]=='B' and my_list[i+24]=='A':
                        flag = 1
                   elif my_list[i+3]=='C'  and  my_list[i+12]=='B' and my_list[i+21]=='A':
                        flag = 1
                   elif my_list[i+6]=='C'  and   my_list[i+15]=='B' and my_list[i+24]=='A':
                        flag = 1
                   elif my_list[i+9]=='C'   and   my_list[i+12]=='B' and my_list[i+15]=='A':
                        flag = 1
                   elif my_list[i+18]=='C'  and   my_list[i+21]=='B' and my_list[i+24]=='A':
                        flag = 1
                   elif my_list[i+6]=='C'  and    my_list[i+12]=='B' and my_list[i+18]=='A':
                        flag = 1
    print(flag)       
                        
                       

    syn=syn+count 
    
               
                   
    c=c+1


MO=syn/100  
print(MO)
