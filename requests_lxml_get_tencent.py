from lxml import etree
import requests
import json


headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
response = requests.get('https://hr.tencent.com/position.php?&start=10#a', headers=headers)

resHtml = response.content
with open('tencent.json', 'w', encoding='utf-8') as output:
    html = etree.HTML(resHtml)
    result = html.xpath('//tr[@class="odd"] | //tr[@class="even"]')

    for site in result:
        item = {}

        name = site.xpath('./td[1]/a')[0].text
        detailLink = site.xpath('./td[1]/a')[0].attrib['href']
        catalog = site.xpath('./td[2]')[0].text
        recruitNumber = site.xpath('./td[3]')[0].text
        workLocation = site.xpath('./td[4]')[0].text
        publishTime = site.xpath('./td[5]')[0].text

        print(type(name))
        print(name, detailLink, catalog, recruitNumber, workLocation, publishTime)
        item['name'] = name
        item['detailLink'] = detailLink
        item['catalog'] = catalog
        item['recruitNumber'] = recruitNumber
        item['publishTime'] = publishTime

        line = json.dumps(item, ensure_ascii=False) + '\n'
        print(line)
        output.write(line)
