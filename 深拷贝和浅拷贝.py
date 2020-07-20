'''
深拷贝（deepcopy）
浅拷贝（copy）

浅/深拷贝
浅拷贝：拷贝表面层，更深的层次引用原来地址的
深拷贝：拷贝所有，内存中开辟新地址
'''
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(d)
print(c)
print(dc)
