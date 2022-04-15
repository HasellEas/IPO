from urllib.request import Request, urlopen

headers_ = {'User-Agent': 'Mozilla/5.0'}

req = Request('http://lectureswww.readthedocs.org', headers=headers_)
webpage = urlopen(req).getcode()

req2 = Request('https://www.youtube.com/user/guru99com', headers=headers_)
webpage2 = urlopen(req2).read()

print(webpage)
print(webpage2)