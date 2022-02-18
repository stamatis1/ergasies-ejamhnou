from urllib.request import Request, urlopen

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
list01 = []
max0 = 0
max1 = 0
list0 = []
list1 = []
max00 = 0
max_1 = 0

for i in range(0,100):

    #thesh round kai eyresh twn 100 teleutaiwn

    data2 = data.decode('utf8')
    th = data2.find(':')
    b = data2.find(',')
    a = data2[:b]
    a = a[th+1:]
    a = int(a)
    a = a-i
    a = str(a)

    #meiomenh timh 

    url = 'https://drand.cloudflare.com/public/{}'
    req = Request(url.format(a), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data2 = data.decode('utf8')

    #thesh randomness kai metatroph se diadiko

    thesh1 = data2.find(":",b)+2
    mn = data2[thesh1:]
    thesh2 = mn.find(',') 
    mn	= mn[:thesh2-1]
    mn = int(mn,16)
    mn = bin(mn)
    list01.append(mn[2:])

#eyresh twn max 0 kai 1 se seira     

for i in range(0,100):
    m0 = 0
    m1 = 0
    l = list(list01[i])
    for j in range(0,len(l)):
        if int(l[j]) == 0:
            m0 = m0 + 1
        elif m0 >= max0:
            max0 = m0
            m0= 0
        elif m0 < max0 :
            m0 = 0
        if int(l[j]) == 1:
            m1 = m1 + 1
        elif m1 >= max1 :
            max1 = m1
            m1 = 0
        elif m1 < max1 :
            m1 = 0             

for i in range(0,100):
    m0 = 0
    m1 = 0
    l = list(list01[i])

    for j in range(0,len(l)):

        if int(l[j]) == 0:
            m0 = m0 + 1
        elif m0 >= max00:
            max00 = m0
            m0 = 0
        elif m0 < max00 :
            m0 = 0
        if int(l[j]) == 1:
            m1 = m1 + 1
        elif m1 >= max_1 :
            max_1 = m1
            m1 = 0
        elif m1 < max_1 :
            m1 = 0

    if max00 == max0 :
        max00 = 0
        list0.append(list01[i])
    if max_1 == max1 :
        list1.append(list01[i])
        max_1 = 0


print(" oi akolou8ies me to megalutero mhkos mhdenikon einai ," ,len(list0), "exoun mhkos : " ,max0, " kai einai oi : ")     
for i in range(0,len(list0)):
    print(list0[i])
print(" oi akolou8ies me to megalutero mhkos monadon einai ," ,len(list1), "exoun mhkos : " ,max1, "kai einai oi e3hs")     
for i in range(0,len(list1)):
    print(list1[i]) 



    