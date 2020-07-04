def det(a):
    if len(a)>=3:
        for i in range(len(a)): #loop ini berguna untuk 
            a[i]=a[i]+a[i][:-1] #mengubah menjadi sorrus
        print(a)
        b2=[ 1 for i in range(len(a))] #determinan kekiri negatif
        b1=[ 1 for i in range(len(a))] ##determinan kekanan positif
        for i in range(len(a)):##
            x=list(reversed(a[i])) #kita balik susunannya dari belakang 
            for j in range(len(a)):##
                b1[j]=a[i][i+j]*b1[j]##
                b2[j]=-1*x[i+j]*b2[j]
        return(sum(b2)+sum(b1))
    elif len(a)==2:
        return(a[0][0]*a[1][1]-a[0][1]*a[1][0])

#debug
#print(det([ [1,2],
#            [2,1]   ]))
#print(det([ [1,2,3],
#            [4,5,6],
#            [7,8,7] ]))

class DNode(object):
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

def kunjungi1(head):
    cursor,daftar=head,[]
    while cursor is not None:
        print(cursor.data)
        cursor=cursor.next

def kunjungi2(head):
    cursor,daftar=head,[]
    while cursor is not None:
        print(cursor.data)
        cursor=cursor.prev

def tambahkan(head,tambah):
    tambah.next=head
    head.prev=tambah

def sisipkan(head,tersisip,posisi):
    if posisi==0:
        tambahkan(head,tersisip)
    else:
        cursor,daftar=head,[]
        while cursor is not None:
            daftar.append(cursor)
            cursor=cursor.next
        tersisip.next=daftar[posisi]
        tersisip.prev=daftar[posisi-1]
        daftar[posisi-1].next=tersisip


def tambahkan3(head,tambah):
    temp=None
    cursor=head
    while cursor is not None:
        temp=cursor
        cursor=cursor.next
    temp.next=tambah
    tambah.prev=temp

a=[1,2,6,4,23,3,5,56,79]
for j in range (len(a)-1):
    for i in range (len(a)-1):
        if a[i+1]<a[i]:
            a[i+1],a[i]=a[i],a[i+1]
            

print(a)

#a=DNode( 11 )
#b=DNode( 52 )
#c=DNode( 18 )
#d=DNode( 1  )
#e=DNode( 34 )
#f=DNode( 31 )
#a.next=b   
#b.next=c
#c.prev=b
#b.prev=a
#kunjungi1(a)
#kunjungi2(c)
#sisipkan(a,d,0)
#kunjungi1(a)
#tambahkan(d,e)
#kunjungi1(e)
#tambahkan3(a,f)
#kunjungi1(e)



def terbalik(semula,semula_2='',urut=0,):
    if urut < len(semula):
        semula_2+=semula[len(semula)-urut-1]
        urut+=1
        return terbalik(semula,semula_2,urut)
    else:
        if semula.lower() == semula_2.lower():
            return True
        return False
print(terbalik('level'))


number=[77, 38, 129, 34, 25, 50, 80]
def bubbleSort(number):
    for j in range (len(number)-1):
        for i in range (len(number)-1):
            if number[i+1]<number[i]:
                number[i+1],number[i]=number[i],number[i+1]

def insertSort(number):
    for i in range(1,len(number)):
        point=number[i]
        pos=1
        while pos > 0 and point < number[pos-1]:
            number[pos] = number[pos-1]
            pos=pos-1
        number[pos]=point

def selectSort(number):
    for i in range(len(number)-1):
        small = searching(number,i,len(number))
        if small != i:
            number[i],number=number,number[i]


numbers=[77,38,129,34,25,50,80]
#print(sorted(numbers)) 
def mergeSort(numbers):
    mid=len(numbers)//2
    up=numbers[mid+1:]
    low=numbers[:mid+1]
    pointer=0
    a=b=c=0
    while pointer > len(numbers):
        if low[a] < up[b]:
            numbers[c]=low[a]
            a+1
        else:
            numbers[c]=up[b]
            b+1
        c+1

###def msort(x):
#    result = []
#    if len(x) < 2:
#        return x
#    mid = int(len(x)/2)
#    y = msort(x[:mid])
#    z = msort(x[mid:])
#    while (len(y) > 0) or (len(z) > 0):
#        if len(y) > 0 and len(z) > 0:
#            if y[0] > z[0]:
#                result.append(z[0])
#                z.pop(0)
#            else:
#                result.append(y[0])
#                y.pop(0)
#        elif len(z) > 0:
#            for i in z:
#                result.append(i)
#                z.pop(0)
#        else:
#            for i in y:
#               result.append(i)
#                y.pop(0)
#    return result

#print(msort(numbers))



def msort3(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    y = msort3(x[:mid])
    z = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

print(msort3(numbers))

def sort(numbers=[77,38,129,34,25,50,80]):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(numbers) > 1:
        pivot =numbers[0]
        for x in numbers:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return numbers
print(sort(numbers))


