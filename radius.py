radius=0
while(radius==0):
    try:
        radius=int(input('the the value of your radius: '))
        answer=3.14*radius*radius
        print('the area of circle is',answer)
    except Exception:
        print('Please do not enter any letter')
