import json

with open ('ccNasabah.json', 'r') as x: 
    out = json.load(x)

print(type(out))
print(out)

with open('ccValid.json', 'w') as y: 
    json.dump(out, y)
with open('ccInvalid.json', 'w') as y: 
    json.dump(out, y)

#===================================================================

letter = ['a','b','c','d','e','f','g','h','i',
        'j','k','l','m','n','o','p','q','r','s','t','u',
        'v','w','x','y','z'
]
ccValid = []
ccInvalid = []
for i in range(len(out)):
    no = out[i]['noCreditCard']
    no = no.split('-')
    no = ''.join(no)
    
    if no[0]=='4' and len(no) == 16:
            
        if ' ' in no:
            ccInvalid.append(out[i])
        elif no[i].isalpha():
            ccInvalid.append(out[i])
        elif '-' in no:
            ccInvalid.append(out[i])
        elif '44444' in no:
            ccInvalid.append(out[i])
        else: 
            ccValid.append(out[i])
    elif no[0] == '5' and len(no) == 16:
        # for j in range(len(no)):
        #     if no[j].isalpha():
        #         invalid.append(out[i])
        
        if ' ' in no:
            ccInvalid.append(out[i])
        elif no[i].isalpha():
            ccInvalid.append(out[i])
        elif '-' in no:
            ccInvalid.append(out[i])
        elif '9999' in no:
            ccInvalid.append(out[i])
        else:
            ccValid.append(out[i])
    elif no[0] == '6' and len(no) == 16:
       
        if ' ' in no:
            ccInvalid.append(out[i])
        elif no[i].isalpha():
            ccInvalid.append(out[i])
        elif '-' in no:
            ccInvalid.append(out[i])
        elif '61234' in no:
            ccInvalid.append(out[i])
        else: 
            ccValid.append(out[i])
    else:
        ccInvalid.append(out[i])

