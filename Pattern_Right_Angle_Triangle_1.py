''' Write a program for printing Pattern like a Right angle Triangle (Pattern 1) with stars.
                  *
                  **
Pattern like ==>  ***
                  ****       
'''
n=int(input("Enter the number of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
