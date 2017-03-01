from __future__ import print_function, division

import nsfg


    
pres = nsfg.ReadFemResp()


pres.columns
pres.head(20)
pres.tail(30)

columns = 0
rows = 0

for columns in pres and rows in pres.agescrn:
    columns = columns + 1
    rows = rows + 1

print ("There are %d rows and %d columns.' %(rows,columns)")


min = None       
max = None

for num in pres.agescrn:                          
    if min== None or num < min :
        print (num)

for num in pres.agescrn:        
    if max== None or max < num :
       print (num)

    
search= 0
for values in pres.numpregs:
    if search == 2298:
        print ("Pregnancies: " + str(values))
    search = search+ 1


under25 =pres[pres['agescrn'] <= 25]
avgpreg = under25['pregnum']

print ("Average number of pregnanices for women aged 25 or under: ", avgpreg.mean())