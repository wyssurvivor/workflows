#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import Document
import random

class Workflow:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)

    def add_item_arg(self,title='',subtitle='',valid='yes',arg=''):
        item=Item(title,subtitle,valid,arg)
        self.items.append(item)

    def generate_items(self):
        doc=Document()
        items=doc.createElement('items')
        for item in self.items:
            ele_item=item.assemble_item()
            items.appendChild(ele_item)
        doc.appendChild(items)
        return doc

    def print_xml(self):
        doc=self.generate_items()
        print doc.toprettyxml(indent='')

class Item:
    def __init__(self,title='',subtitle='',valid='yes',arg=''):
        self.title=title
        self.subtitle=subtitle
        self.valid=valid
        self.arg=arg

    def assemble_item(self):
        doc=Document()
        ele_item=doc.createElement('item')
        ele_item.setAttribute('uid',str(random.randint(0,100000000)))
        ele_item.setAttribute('arg',self.arg)

        ele_title=doc.createElement('title')
        ele_title_text=doc.createTextNode(self.title)
        ele_title.appendChild(ele_title_text)
        ele_item.appendChild(ele_title)

        ele_subtitle=doc.createElement('subtitle')
        ele_subtitle_text=doc.createTextNode(self.subtitle)
        ele_subtitle.appendChild(ele_subtitle_text)
        ele_item.appendChild(ele_subtitle)

        ele_valid=doc.createElement('valid')
        ele_valid_text=doc.createTextNode(self.valid)
        ele_valid.appendChild(ele_valid_text)
        ele_item.appendChild(ele_valid)

        return ele_item
