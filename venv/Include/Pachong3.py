from lxml import etree
import requests



htmlText = requests.get("https://www.cnbeta.com/")
text = htmlText.text.encode('ISO-8859-1')
# print (etree)
select = etree.HTML(text, etree.HTMLParser())
xpath = select.xpath('//*[@id="J_all_item_852813"]/dl/dt/a/text()')
print(xpath[0])


