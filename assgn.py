yr=int(input("ENTER the year"))
if yr % 4 ==0 and (yr % 100 !=0 or yr %400):
    print(yr,"this is a leap yaer")
else:
    print(yr,"this is not a leap year")


