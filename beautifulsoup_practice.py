html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'lxml')

print(soup)

print(soup.prettify())

# select by tag name
print(soup.select('title'))
# select by class name
print(soup.select('.sister'))
# select by id
print(soup.select('#link1'))
# select by html path
print(soup.select("head > title"))

print(soup.select('p #link1'))

# select by attribute
print(soup.select('a[class="sister"]'))
print(soup.select('a[href="http://example.com/elsie"]'))
print(soup.select('p a[href="http://example.com/elsie"]'))

# get html text by get_text()
print(soup.select('title')[0].get_text())
for title in soup.select('title'):
    print(title.get_text())


# Element.Tag
print(type(soup.select('a')[0]))
# Tag name
print(soup.name)
print(soup.select('a')[0].name)
# Tag attrs
print(soup.select('a')[0].attrs)
print(soup.select('a')[0].attrs['class'])