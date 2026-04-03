dia = input('dia')
mês = input('mês')
ano = input('ano')
print('Você nasceu no dia', dia, 'de', mês, 'de', ano, '.' 'Correto?')
            
# Adicionando calculoo de idade
from datetime import date
ano_atual = date.today().year
idade = ano_atual - int(ano)
print('Você tem', idade, 'anos.')