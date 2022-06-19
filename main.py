#A function report incorrect because of else case in the fucntion.
def is_prime(n):
    Prime=True
    for i in range(2,n):
        if n%1==0:
            Prime=False
    return Prime
print(is_prime(3))

#B define list of vowel, and it will return true statement if charector is in list.
def is_vowel(value):
    li=["a","e","i","o","u","A","E","I","O","U"]
    if value in li:
        return True
    else:
        return False
print(is_vowel("E"))

#C.
li1=["apple","ball","car","dog"]
li2=[i[0].upper() for i in li1]
li3=[i*2 for i in li1]
li5=[i[0] for i in li1]
li6=[i for i in zip(li1,li5)]
print(li2)
print(li3)
print(li6)