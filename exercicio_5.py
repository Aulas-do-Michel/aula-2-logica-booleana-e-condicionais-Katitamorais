frequencia_populacional = float(input('Digite a frequencia populacional (em porcentagem):'))
gene = str(input('Digite o gene:'))
impacto = str(input('Digite a Impacto (ALTO ou BAIXO):'))
reads = int(input('Digite os reads:'))
frequencia_alelica = float(input('Digite a frequencia alélica (em porcentagem):'))

eh_artefato = (frequencia_alelica < 20) or (reads < 10)
impacto_baixo = impacto == 'BAIXO'
esta_em_genes_de_excecao = (gene == 'HFE') or (gene == 'MEFV') or (gene == 'GJB2')
frequencia_populacional_alta = frequencia_populacional > 5

if eh_artefato:
    print('Não é relevante.')
elif impacto_baixo or (frequencia_populacional_alta and not esta_em_genes_de_excecao):
    print('Não é relevante.')
else:
    print('É relevante.')
