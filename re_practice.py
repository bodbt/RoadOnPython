import re

mactchObj = re.search(r"\\", r"ab123bb\c")
print(mactchObj.group())

mactchObj = re.search(r"\d", r"ab123bb\c")
print(mactchObj.group())


line = "Cats are smarter than dogs"
matchObj = re.match(r"(.*) are (.*?) .*", line, re.M|re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!")

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
# re.search匹配整个字符串，直到找到一个匹配。
matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!")

searchObj = re.search(r'dogs', line, re.M|re.I)
if searchObj:
   print("search --> searchObj.group() : ", searchObj.group())
else:
   print("Nothing found!")


pattern = r"\w+"
target = "hello world\nWORLD HELLO"
ret = re.findall(pattern, target)
#['hello', 'world', 'WORLD', 'HELLO']
print(ret)


# re.I(re.IGNORECASE)	使匹配对大小写不敏感
ret = re.findall("world", target,re.I)
#['world', 'WORLD']
print(ret)

# re.S(DOTALL)	使 . 匹配包括换行在内的所有字符
ret = re.findall("world.WORLD", target,re.S)
#["world\nworld"]
print(ret)

ret = re.findall("hello.*WORLD", target,re.S)
#['hello world\nWORLD']
print(ret)

# re.M(MULTILINE)	多行匹配，影响 ^ 和 $
re.findall("^WORLD",target,re.M)
#["WORLD"]
print(ret)

# re.X(VERBOSE)	正则表达式可以是多行，忽略空白字符，并可以加入注释
reStr = r'''\d{3}   #区号
        -\d{8}'''   #号码
ret = re.findall(reStr,"010-12345678",re.X)
#["010-12345678"]
print(ret)


# re模块提供了re.sub用于替换字符串中的匹配项
url = "http://hr.tencent.com/position.php?&start=10"
page = re.search(r'start=(\d+)', url).group(1)

nexturl = re.sub(r'start=(\d+)', 'start='+str(int(page)+10), url)
print("Next Url : ", nexturl)
