# Decreasing Triangle program
i =1
while(i<=5):
    j=i
    while(j<=5):
     print("*",end="")
     j+=1
    print()
    i+=1
""" output :-
*****
****
***
**
*
"""
# Number Decreasing Triangle program
i = 1
while(i<=5):
    j=i
    while(j<=5):
        print(f"{i}",end="")
        j+=1
    print()          
    i+=1
"""output:-
11111
2222
333
44
5  
"""

#Increasing Triangle program
i =5
while(i>=1):
    j=i
    while(j<=5):
     print("*",end="")
     j+=1
    print()
    i-=1
"""output:-
*
**
***
****
*****
"""
# Number Increasing Triangle program
i = 1
while(i<=5):
    j=i
    while(j>=1):
        print(f"{i}",end = "")
        j-=1
    print()
    i+=1
"""output:-
1
22
333
4444
55555
"""
#Squre patten program
i = 1
while(i<=5):
    j=5
    while(j>=1):
        print(" * ",end="")
        j-=1
    print()
    i+=1
"""output:-
*  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  *
"""
#Number Squre patten 
i = 1
while(i<=5):
    j = 5
    while(j>=1):
        print(f"{i}",end="")
        j-=1
    print()
    i+=1
"""output:-
11111
22222
33333
44444
55555
"""

#Half butterfly pattern
i = 5
while(i>=1):
    j=i
    while(j<=5):
        print(" * ",end="")
        j+=1
    print()
    i-=1

i = 1
while(i<=5):
    j=5
    while(j>=1):
        print(" * ",end="")
        j-=1
    print()
    i+=1
  
i = 1
while(i<=5):
    j=i
    while(j<=5):
        print(" * ",end="")
        j+=1
    print()
    i+=1
"""output:-
*  
 *  * 
 *  *  * 
 *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  * 
 *  *  * 
 *  * 
 * 
"""

#pattern 
i = 1
while(i<=4):
    j =1
    while(j<=4):
        if(j==2 or j==3) and (i==2 or i ==3):
         print(" ",end="")
        else:
           print("*",end="")
        j+=1
    print()
    i+=1
""" output-:
 ****
 *  *
 *  *
 ****   """

#program
i = 1
while(i<=4):
    j =1
    while(j<=5):
        if(j==2 or j ==4 ) and (i==2) or (j==2 or j==3 or j==4) and (i==3) or (j==2 or j==3 or j==4) and (i==4):
         print(" ",end="")
        else:
           print("*",end="")
        j+=1
    print()
    i+=1
    """
output:-
*****
* * *
*   *
*   *
""" 

#program
i = 1
while(i<=4):
    j =1
    while(j<=4):
        if(j ==1 or j==2 or j ==3 or j==5) and (i==2) or ( j==3 or j ==4 or j==5 or j==1 ) and (i==3):
         print(" ",end="")
        else:
           print("*",end="")
        j+=1
    print()
    i+=1
"""
output:-
****
   *
 *
****"""

#use for loop
w = int(input("enter"))
for i in range(w):
    for j in range(w,i,-1):
        print("*",end = "")
    for k in range(i):
           print("*",end ="")
    print()
"""output:-
*****
*****
*****
*****
*****
"""
# second patterm
x  = 5 
for i in range(x):
    for j in range(x):
        if(j==1 or j==2 or j==3 ) and (i==1):
            print(" ",end ="")
        elif(j==1 or j==2 or j==3) and (i==2):
            print( " ",end= "")
        elif(j==1 or j==2 or j==3) and (i==3):
            print( " ",end= "")
        else:
            print("*",end=" ")
    print()
"""output:-
* * * * * 
*    * 
*    * 
*    * 
* * * * * 
"""
#pattern program
x  = int(input("enter your row"))
m =1
for i in range(x):
    for j in range(1,i+1):
        print(j,end="")
    print()
"""output:-
1
12
123
1234"""

#program
x  = int(input("enter your row"))
for i in range(x):
    for j in range(i+1):
        for k in range(x,i,-1):
            print( " * ",end="")
    print()
  """output:-
*  *  *  *  * 
 *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  * 
 *  *  *  *  * """  
