#__coding:utf-8__
#!/usr/bin/python
# File Name: aaa.py
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2016年03月06日 星期日 07时33分42秒
#########################################################################
import os
#print os.path.dirname(os.path.dirname(__file__))
base_dir = os.path.dirname(os.path.abspath(__file__))
print os.path.join(base_dir,'static/').replace('\\','/')
print base_dir
