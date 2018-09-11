i= input('Enter a positive integer')
try:
    j = int(i)
except:
    j=-1
if(j>=0):
    print('its a number')
else:
    print('invalid integer')
