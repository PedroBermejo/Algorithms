data = [
    ["Literatura", 0.01, []], 
    ["Arquitectura", 0.01, []], 
    ["Civil", 0.04, []],
    ["Electronica", 0.04, []],
    ["Derecho", 0.10, []],
    ["Medicina", 0.15, []],
    ["Biologia", 0.20, []],
    ["Quimica", 0.20, []],
    ["Sistemas", 0.25, []]
]

codigos = {}

root = -1

#Data se extiende y termina de la siguiente forma
#  [0,      1,            2,                   3,   4]
# [nombre, probabilidad, [hijo izq, hijo der], 0/1, padre]
def buildHoffman():
    probabilidad = i = 0
    
    while probabilidad < 1:
        global root
        probabilidad = data[i][1] + data[i+1][1]
        j = i+1
        #print(i, data)
        while j < len(data) and probabilidad > data[j][1]:
            j = j+1
        data[i].extend(['0', j])
        data[i+1].extend(['1', j])
        if( probabilidad != 1):
            data.insert(j, ["generico" + str(j), probabilidad, [i, i+1]]) 
        else:
            data.insert(j, ["generico" + str(j), probabilidad, [i, i+1], "", ""])
            root = j 
        i = i+2

    for d in data:
        if ( "generico" not in d[0]):
            #print(d)
            codigo = d[3]
            prob = 0
            nodo = d
            while prob < 1:
                nodo = data[nodo[4]]
                codigo = nodo[3] + codigo
                prob = nodo[1]

            codigos[d[0][0]] =  codigo
    
def encryptText(text):
    result = ""
    for i in range(len(text)):
        result = result + codigos[text[i]]
    return result

def decryptText(text):
    result = ""
    i = 0
    node = data[root]
    while i < len(text):
        if("generico" in node[0]):
            #print(node[0], i, text[i], int(text[i]), node[2])
            node = data[node[2][int(text[i])]]
            i = i+1
        else:
            result = result + node[0][0]
            node = data[root]
    return result



buildHoffman()

text = "CEEQLAALBQSSQQMBCDDDELABAQBBDLSSDLSASSSACCQSSDLBQQQ"
encrypted = encryptText(text)
print("Texto:", text, "\n")
print("Texto encriptado:", encrypted, "\n")
decrypted = decryptText(encrypted)
print("Texto desencriptado:", decrypted, "\n")




'''
print("Interpretacion Tree: \n[nombre, probabilidad, [hijo izq, hijo der], 0/1, padre]")
for d in data:
    print(d)

for key, value in codigos.items():
    print(key, value)
'''

