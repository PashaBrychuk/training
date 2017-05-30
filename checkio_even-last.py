def checkio(array):
    if len(array)>0:
        z = array[::2]
        s = 0
        for i in z:
            s = s+i
        
        return array[len(array)-1] *s
    return 0

z = [0,1,2,3,4,5]
print checkio(z)