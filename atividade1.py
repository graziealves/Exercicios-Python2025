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
soma1= v1+ v2+ v3+ v4+ v5+ v6+ v7+ v8+ v9
divisao1= soma1%11
digito1= 11 - divisao1
    
if divisao1 <2:
    print(divisao1)
else:
    result1= 11 - divisao1
    print(result1)

d1= cpf[0]*11 
d2= cpf[1]*10
d3= cpf[2]*9
d4= cpf[3]*8
d5= cpf[4]*7
d6= cpf[5]*6 
d7= cpf[6]*5
d8= cpf[7]*4
d9= cpf[8]*3
d10=cpf[9]*2

soma2= d1+d2+d3+d4+d5+d6+d7+d8+d9+d10
divisao2= soma2%11

if divisao2 <2:
    print(divisao2)
else:
    result2= 11 - divisao2
    print(result2)



    

