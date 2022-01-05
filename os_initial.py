import requests
import re
import json
import time

base = 'https://api.opensea.io/api/v1/assets'
collection = 'sandbox'
order_by = 'pk'
order_direction = 'desc'
limit = 50

no_order = False

offset = 0
while True:
    url = f"{base}?order_by={order_by}&order_direction={order_direction}&offset={offset}&limit={limit}&collection={collection}"
    if no_order:
        url = f"{base}?offset={offset}&limit={limit}&collection={collection}"
    response = requests.request("GET", url)
    if 'assets' in response.json():
        for asset in response.json()['assets']:
            if asset['sell_orders']:
                price = float(asset['sell_orders'][0]['current_price']) / 1000000000000000000
                if  asset['name']:
                    print(price, asset['name'], asset['sell_orders'][0]['created_date'])
                    m = re.search('\((.*), (.*)\)', asset['name'])
                    if len(m.groups()) == 2:
                        with open(fr'C:\Users\base\Documents\Endeavours\Crypt\opensea\assets\land_{m.groups()[0]}_{m.groups()[1]}.json','w') as f:
                            json.dump(asset, f)
        offset += 50

    else:
        print(f'reached offset {offset}, break for 60s and restart')
        time.sleep(60)
        offset = 0
        break

