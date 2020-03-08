from math import sqrt as sq
import random

#1
def cetakSiku(x):
    for i in range(x):
        for j in range(i+1):
            print("*" , end=" ")
        print(" ")
#2
def gambarlahSegiEmpat(x,y):
    for i in range(x):
        for k in range(y):
            if(i == 0 or i == x-1 or k == 0 or  k == y-1):
                print("@", end=" ")
            else:
                print("    ",end=" ")
        print()
 #3       
def jumlahHurufVokal(x):
    a=len(x)
    b=0
    vokal=['a','i','u','e','o','A','I','U','E','O'] 
    for i in x:
            if i in vokal:
                b+=1
    return a,b
    print(a,b)
        
def jumlahHurufKonsonan(x):
    a=len(x) 
    b=0
    konsonan=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',
                        'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'] 
    for i in x:
        if i in konsonan:
            b+=1
    return a,b
    print(a,b)
#4
def rerata(x):
    nilai=x
    awal=0
    akhir=0
    for i in range(0,len(nilai)+1):
        awal=awal+nilai[i]
    akhir=awal*len(nilai)/2
    return akhir 
#5
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primaKecil=[2,3,5,7,11]
    bukanPrimaKecil=[0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrimaKecil:
        return False
    else:  
        for i in range(2,int(sq(n))+1):
##                if (i % 2 == 0):
##                    print (i,'bukan bilangan prima')
##                elif i % 9 == 0:
##                    print(i, 'bukan bilangan prima')
##                else:
##                    print (i,'bilangan prima')

               
                if n%i==0: 
                    print (n,'bukan bilangan prima, karena habis dibagi',i, 'dan menghasilkan sisa',n/i)
                    break
                else : print(i,'bilangan prima')
#6
def prima(x,y):
    for i in range(x,y+1):
            if n % i == 1: 
                print(i, end=' ')

#7
def no7(x):
    a=[]
    step=2
    while step<=x:
        if x%step==0:
            x=x/step
            a.append(step)
        else:
            step+=1
    return a
    
#8
def apakahTerkandung(a,b):
    if a in b:
        return True
    else:
        return False
#9
def soal9(a,b):
    for i in range(a,b):
        if i % 3 ==0 and i % 5 == 0:
            print('Python UMS')
        elif i % 3 ==0 :
            print('Python')
        elif i % 5 == 0:
            print('UMS')
        else:
            print(i)
#10
def selesaikanABC(a,b,c):
    try:
        a = float(a)
        b = float(b) 
        c= float(c)
        D= b**2 - 4*a*c
        x1 = (-b + ty(D))/(2*a)
        x2 = (-b - ty(D))/(2*a)
        hasil = (x1,x2)
        print(D)
        return hasil
    except:
        print('Determinannya negatif. Persamaan tidak memiliki akar real')
#11
def apakahKabisat(x):
    if x % 4 == 0:    
        print(str(x) + " Adalah Tahun kabisat")
    elif x % 100 == 0 and x % 400 == 0:
        print(str(x) + " Adalah Tahun kabisat")
    else:
        print(str(x) + ' Bukan tahun kabisat')
#12
def no12():        
    x=random.randint(1,100)
    print('Saya menyimpan angka. sebernanya angkanya adalah: ',x) 
    for i in range(1,10):
        y=int(input('masukkan tebakkan: '))
        if y > x :
            print('itu terlalu besar. Coba lagi')
        elif y < x :
            print('itu terlalu kecil. Coba lagi')
        else:
            print('Ya,Anda benar')
            break
#13
def no13Function(x):
    angka={0:'',1:'satu',2:'dua',3:'tiga',4:'empat',5:'lima',6:'enam',7:'tujuh',8:'delapan',9:'sembilan'}
    if (x<10): 
        return (str(angka[x]))
    elif (x < 20):
        y=x%10
        return (str(angka[y] +' belas'))
    elif x<99:
        return (str(angka[x//10] + ' puluh ' +no13Function(x%10)))
    elif x<999:
        return (str(angka[x//100] + ' ratus ' +no13Function(x%100)))
    elif x<9999:
        return(str(angka[x//1000] + ' ribu ' + no13Function(x%1000)))
    elif x<99999:
        return(str(angka[x//10000] + ' puluh ' + no13Function(x%10000)))
    elif x<999999:
        return(str(angka[x//100000] + ' ratus ' + no13Function(x%100000)))
    elif x<9999999:
        return(str(angka[x//1000000]) + ' juta ' + no13Function(x%1000000))
    elif x<99999999:
        return(str(angka[x//10000000]) + ' puluh ' + no13Function(x%10000000))
    elif x<=999999999:
        return(str(angka[x//100000000]) + ' ratus ' + no13Function(x%100000000))
    else:
        print('Input melebihi limit')
def no13(x):
    x=no13Function(x).replace('satu belas','sebelas').replace('satu puluh','sepuluh').replace("satu ratus","seratus")
    return x

#14
def no14(x):
    uang=str(x)
    if len(uang) <= 3 :
        return 'Rp ' + uang
    else :
        p = uang[-3:]
        q = uang[:-3]
        return no14(q) + '.' + p
        print('Rp ' + no14(q) + '.' + p)

