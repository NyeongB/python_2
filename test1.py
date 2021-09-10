arr = [('SI', 55), ('CONTENTS', 53), ('HARDWARE', 19), ('PORTAL', 55), ('GAME', 22)]

arr.sort(key=lambda x:[-x[1],x[0]])

print(arr)