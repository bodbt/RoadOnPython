from lxml import etree
text = '''
<div>
  <ul>
       <li class="item-0"><a href="link1.html">first item</a></li>
       <li class="item-1"><a href="link2.html">second item</a></li>
       <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
       <li class="item-1"><a href="link4.html">fourth item</a></li>
       <li class="item-0"><a href="link5.html">fifth item</a>
   </ul>
</div>
'''
#Parses an HTML document from a string
html = etree.HTML(text)
#Serialize an element to an encoded string representation of its XML tree
result = etree.tostring(html)
print(result)

print(type(html))
result = html.xpath('//li')
print(result)
print(len(result))
print(type(result))
print(type(result[0]))