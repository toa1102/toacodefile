
key = input('Please write key.')

moji = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

anngoubunn = ''
bunn = input()
a = len(bunn)//len(key)
keycode = ''
for i in range(a + 1):
    keycode = key + keycode
print(keycode)
c = -1
d = -1
for i in range(len(bunn)):
    c = c + 1
    kazu = x[keycode[c]]
    d = d + 1
    z = x[bunn[d]]
    anngoubunn = str(anngoubunn) + str(moji[z + kazu])
print(anngoubunn)