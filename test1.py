import functools 


arr = ['fab', 'fed', 'f', 'ed','e']
ab = {'f':10,'e':11,'d':12,'c':13,'b':14,'a':15}
def comparator(a,b):
    s_a = ''
    s_b = ''
    
    for i in a:
        s_a += str(ab[i])

    for i in list(b):
        s_b += str(ab[i])
    print(s_a,s_b)
    if s_a > s_b:
        return 1
    else:
        return -1

print(arr)

arr.sort(key=functools.cmp_to_key(comparator))

print(arr)