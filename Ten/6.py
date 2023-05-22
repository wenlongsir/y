#<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
import re
str='<div class="nam">中国</div>'
res=re.findall(r'<div class=".*">(.*?)</div>',str)
print(res)