#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64
from workflow import Workflow,Item

def encode(text):
    wf=Workflow()
    base64_text=base64.encodestring(text).replace('\n','')
    wf.add_item_arg(title=base64_text,subtitle=text,arg=base64_text)
    wf.print_xml()

def decode(base64_text):
    wf=Workflow()
    text=base64.decodestring(base64_text)
    wf.add_item_arg(title=text,subtitle=base64_text,arg=text)
    wf.print_xml()

if __name__=='__main__':
    # encode('937423966')
    # OTM3NDIzOTY2
    decode('OTM3NDIzOTY2')