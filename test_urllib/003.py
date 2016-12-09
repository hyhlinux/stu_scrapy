#coding:utf-8
import config
import urllib2
import urllib

url = config.MyURL.BAIDU
print url

request = urllib2.Request(url)
world = dict(wd="python")
world = urllib.urlencode(world)
print world





# In [3]: urllib.urlencode({"wd":"python"})
# Out[3]: 'wd=python'

# In [4]: urllib.urlencode({"wd":"北京"})
# Out[4]: 'wd=%E5%8C%97%E4%BA%AC'

# In [5]: 
