import sys,math
def factorize(n):
    def isPrime(n):
        return not [x for x in xrange(2,int(math.sqrt(n))+1)
                    if n%x == 0]
    primes = []
    candidates = xrange(2,n+1)
    candidate = 2
    while not primes and candidate in candidates:
        if n%candidate == 0 and isPrime(candidate):
            primes = primes + [candidate] + factorize(n/candidate)
        candidate += 1
    return primes

def condense(L):
  prime,count,list=0,0,[]
  for x in L:
    if x == prime:
      count = count + 1
    else:
      if prime != 0:
        list = list + ['{' + str(prime) + '}^{' + str(count) + '}']
      prime,count=x,1
  list = list + ['{' + str(prime) + '}^{' + str(count) + '}']
  return list

with open("EA-4.txt") as fh:
    ea = fh.readlines()

with open("ea-to-ccz-4.txt") as fh:
    ccz = fh.readlines()

with open("EA-4-sizes.txt") as fh:
    sizes = fh.readlines()

with open("EA-4-bijective-summary.txt") as fh:
    bijective = fh.readlines()
    
with open("EA-4-degree.txt") as fh:
    degree = fh.readlines()

with open("EA-4-walsh.txt") as fh:
    walsh_list = fh.readlines()


walsh_index = {}
walsh_cnt = 0
with open("052-dim-4-walsh.tex", "w") as fh:
    for idx, w in enumerate(walsh_list):
        if w not in walsh_index:
            walsh_cnt = walsh_cnt + 1
            walsh_index[w] = walsh_cnt
            f = [ "$w_{" + str(walsh_cnt) + "}$" ]
            ws = w.split()
            ws[0] = str(int(ws[0]) - 15)
            ws[16] = str(int(ws[16]) - 1)
            f.extend(ws)
            print >> fh, " & ".join(f) + r" \\"
    
for i in xrange(4713):
    fields = [str(i+1)]
    fields.extend(ea[i].split())

    size = int(sizes[i].split()[-1])
    size = 6818690079129600 / size
    #size = 18446744073709551616 / size
    #factors = condense(factorize(size))
    #fields.append("".join(factors))
    fields.append(str(size))

    fields.append(degree[i].strip())
    fields.append("$w_{" + str(walsh_index[walsh_list[i]]) + "}$")

    bij = bijective[i].split()[-1]
    if bij == 'bijective':
        fields.append("N")
    elif bij == "something:":
        fields.append("Y")
    else:
        raise Exception("bij " + i)

    ccz_eq = int(ccz[i])
    if (ccz_eq == i+1):
        fields.append("can.")
    else:
        fields.append(r"\#" + str(ccz_eq))


    print " & ".join(fields) + r' \\'

# xx=[    
#     [      1,          1048576],
#     [      1,        251658240],
#     [      1,        440401920],
#     [      1,        550502400],
#     [      1,       1887436800],
#     [      1,       7046430720],
#     [      1,       8808038400],
#     [      1,      12331253760],
#     [      1,      13212057600],
#     [      1,      23121100800],
#     [      1,      26424115200],
#     [      2,      39636172800],
#     [      1,      46242201600],
#     [      1,      61656268800],
#     [      1,      92484403200],
#     [      1,      98650030080],
#     [      2,     123312537600],
#     [      2,     184968806400],
#     [      2,     277453209600],
#     [      1,     317089382400],
#     [      4,     369937612800],
#     [      2,     554906419200],
#     [      1,     591900180480],
#     [      1,     634178764800],
#     [      6,     739875225600],
#     [      1,     986500300800],
#     [      5,    1109812838400],
#     [      1,    1183800360960],
#     [      6,    1479750451200],
#     [      1,    1664719257600],
#     [      1,    1973000601600],
#     [     10,    2219625676800],
#     [      1,    2367600721920],
#     [      1,    2959500902400],
#     [      3,    3329438515200],
#     [     11,    4439251353600],
#     [      2,    5073430118400],
#     [      5,    5919001804800],
#     [      7,    6658877030400],
#     [      8,    8878502707200],
#     [      2,   11838003609600],
#     [     13,   13317754060800],
#     [     26,   17757005414400],
#     [      1,   20293720473600],
#     [      6,   23676007219200],
#     [     27,   26635508121600],
#     [     29,   35514010828800],
#     [      2,   40587440947200],
#     [      2,   47352014438400],
#     [     65,   53271016243200],
#     [      1,   56822417326080],
#     [     25,   71028021657600],
#     [      3,   94704028876800],
#     [     87,  106542032486400],
#     [      1,  113644834652160],
#     [      1,  121762322841600],
#     [     35,  142056043315200],
#     [      6,  189408057753600],
#     [    139,  213084064972800],
#     [     27,  284112086630400],
#     [      1,  324699527577600],
#     [    240,  426168129945600],
#     [     45,  568224173260800],
#     [    273,  852336259891200],
#     [      3,  974098582732800],
#     [     51, 1136448346521600],
#     [      1, 1363738015825920],
#     [    513, 1704672519782400],
#     [     24, 2272896693043200],
#     [    930, 3409345039564800],
#     [   2033, 6818690079129600]
# ]
# z=0
# for i,j in xx:
#     z += i*j
# print z
