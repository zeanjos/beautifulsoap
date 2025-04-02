import requests
from bs4 import BeautifulSoup
link = 'https://wise.com/br/currency-converter/dolar-hoje'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, 'lxml')
status = requisicao.status_code
if status == 200:
    print('Requisição concluida com sucesso!')
else:
    print(f'Requisição não disponivel, erro {status}')

dolar = site.select_one('span.text-success')
valor_convertido = dolar.text
print(f'O valor atual do dolar é de R$ {valor_convertido}')
