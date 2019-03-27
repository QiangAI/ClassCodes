import random
import time
from urllib import parse

url = "https://www.lagou.com/jobs/list_%s?labelWords=&fromSearch=true&suginput=" % ('python开发工程师')
print(url)
per_url = parse.quote(url)
print(per_url)
print(parse.unquote(per_url))

r = int(random.uniform(10, 30))
print(r)

result = time.strptime('2018-11-12 09:46:44', '%Y-%m-%d %H:%M:%S')
print(result)
