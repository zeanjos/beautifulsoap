import requests
from bs4 import BeautifulSoup
link = 'https://www.infomoney.com.br/cotacoes/cambio/moeda/dolar/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)
site = BeautifulSoup(requisicao.text, 'lxml')
status = requisicao.status_code
if status == 200:
    print('Requisição concluida com sucesso!')
else:
    print(f'Requisição não disponivel, erro {status}')

dolar = site.select_one('div.value p')
valor_convertido = dolar.text.strip()
print(f'O valor atual do dolar é de R$ {valor_convertido}')

cotacao = site.select_one("span.text-success")
print(cotacao)