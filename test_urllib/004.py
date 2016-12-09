#coding:utf-8
import urllib2
import urllib

output = open("lagou.json", "w")
page = 1

# POST 请求要传送的数据
formdata = "first=false&pn=" + str(page) + "&kd=python"

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# POST /jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&district=%E6%B5%B7%E6%B7%80%E5%8C%BA&bizArea=%E4%B8%AD%E5%85%B3%E6%9D%91&needAddtionalResult=false HTTP/1.1
# city=北京
# district=海淀区
# bizArea=中关村
request = urllib2.Request("http://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false", headers=headers)

# 通过request.add_data() 将 data数据传进入request内
request.add_data(formdata)
#print request.get_data()

response = urllib2.urlopen(request)
print response.code
output.write(response.read())
output.close()