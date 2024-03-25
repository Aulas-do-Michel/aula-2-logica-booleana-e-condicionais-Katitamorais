cromossomo=str(input('Digite o cromossomo da variante:'))
position=int(input('Digite a posiçao da variante:')) 
right_position= (position >= 41196312) and (position <= 41277500)          
if (cromossomo == 'chr17') and (right_position):
    print('Sim')
else:
    print('Não')
