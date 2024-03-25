pais=str(input('Qual país você vai viajar?'))
if (pais=='Estados Unidos') or (pais=='Argentina') or (pais=='Japão'):
   reais=float(input('Quantos reais você quer converter?'))
   USD=5
   ARS=180
   JPY=30
   if (pais =='Estados Unidos'):
        valor=reais*USD
        print(f'{valor} USD')
   elif (pais == 'Argentina'):
        valor=reais*ARS
        print(f'{valor} ARS')
   elif (pais == 'Japão'):
        valor=reais*JPY
        print(f'{valor} JPY')
else:
    print('Não temos essa moeda em caixa.')
