import requests


def ball(wallet):
  # Адрес кошелька пользователя
  #wallet = '12VeK1eRgPHRUikNLXq3Nuz99gS2S46QMD'
  # wallet = gen_address(0)

  url = f'https://blockchain.info/rawaddr/{wallet}'
  x = requests.get(url)
  wallet = x.json()

  print('Итоговый баланс:'+str(wallet['final_balance']))
  print('Транзакции:'+str(wallet['txs']))

  if wallet['total_received']==0:
    print('баланс пустой')

  return wallet
if __name__ == '__main__':
  ball('12VeK1eRgPHRUikNLXq3Nuz99gS2S46QMD')