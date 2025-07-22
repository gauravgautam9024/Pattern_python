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