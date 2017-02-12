#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#  def main(wf):
#     query=wf.args[0]
#     wf.add_item(title=query+' wys',
#                 subtitle=query+' wys sub',
#                 arg='http://www.baidu.com',
#                 valid=True)
#     wf.send_feedback()

def encode(word):
    str = '<items><item autocomplete="autocompletex" uid="123" arg="wys lear alfred workflow"><title>wys test</title><subtitle>wys test subtitle</subtitle><valid>yes</valid></item></items>'
    print str
