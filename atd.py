#validador de CPF

cpf= [5,1,8,7,9,0,3,5,8,6,3]

v1= cpf[0]*10 
v2= cpf[1]*9
v3= cpf[2]*8
v4= cpf[3]*7
v5= cpf[4]*6
v6= cpf[5]*5 
v7= cpf[6]*4
v8= cpf[7]*3
v9= cpf[8]*2
soma= v1+ v2+ v3+ v4+ v5+ v6+ v7+ v8+ v9
divisao= soma%11
dig1= 11 - divisao
    
if divisao <2:
    primeirodig= 0
else:
    print(dig1)
    

