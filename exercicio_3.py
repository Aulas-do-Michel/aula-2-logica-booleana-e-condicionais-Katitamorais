cromossomo=str(input('Digite o cromossomo da variante:'))
position=int(input('Digite a posiçao da variante:')) 
genoma=str(input('Digite o genoma de referência, ou seja, hg19" ou "hg38":'))
right_position1= (position >= 41196312) and (position <= 41277500) and (genoma == 'hg19')
right_position2= (position >= 43044295) and (position <= 43125483) and (genoma == 'hg38')      
if (cromossomo == 'chr17') and (right_position1) or (right_position2):
   print('Sim')
else:
    print('Não')
