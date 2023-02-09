
key = input('Please write key.')

moji = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = {'a':26,'b':27,'c':28,'d':29,'e':30,'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,'z':51}

bunn = input('please write code.')

anngoubunn = ''
a = -1
for i in range(len(bunn)):
    a = a + 1
    z = x[bunn[a]]
    anngoubunn = anngoubunn + moji[z + key] + moji[z - key]
print(anngoubunn)