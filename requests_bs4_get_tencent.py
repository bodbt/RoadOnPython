from bs4 import BeautifulSoup
import requests
import json


headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
response = requests.get('https://hr.tencent.com/position.php?&start=10#a', headers=headers)

resHtml = response.content
with open('tencent.json', 'w', encoding='utf-8') as output:
    html = BeautifulSoup(resHtml, "lxml")
    result_even = html.select('tr[class="even"]')
    result_odd = html.select('tr[class="odd"]')
    result = result_even + result_odd
    print(len(result))

    for site in result:
        item = {}

        name = site.select('td a')[0].get_text()
        detailLink = site.select('td a')[0].attrs['href']
        catalog = site.select('td')[1].get_text()
        recruitNumber = site.select('td')[2].get_text()
        workLocation = site.select('td')[3].get_text()
        publishTime = site.select('td')[4].get_text()

        print(name, detailLink, catalog, recruitNumber, workLocation, publishTime)
        item['name'] = name
        item['detailLink'] = detailLink
        item['catalog'] = catalog
        item['recruitNumber'] = recruitNumber
        item['publishTime'] = publishTime

        line = json.dumps(item, ensure_ascii=False) + '\n'
        print(line)
        output.write(line)
