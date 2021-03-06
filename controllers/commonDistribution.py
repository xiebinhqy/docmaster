#!/usr/bin/env python
# coding: utf-8
from models.Item import *
from libs.utils import *
import web

def assign(post_data):
    type = post_data.get('type', 'project')
    if type == 'project':        
        item_id = '0'        
        item_content = {}
        pid = post_data.get('pid', '99')
        item_list = model_to_object(get_item_list(pid))
        if item_list:
            item_id = post_data.get('item_id', item_list[0].get('id'))
            item_content = get_item_content(item_id)    
        if item_content:
            item_content = item_content[0]
        else:
            item_content = {}
        if not web.config._session.user.get('id', ''):
            item_content['html'] = item_content.get('html', '').replace('编辑</a>', '</a>')
        return {
                'item_list' : model_to_object(item_list), 
                'item_id' : item_id,
                'item_content' : item_content.get('html', ''),
                'title' : item_content.get('title', ''),
                'pid' : pid,
                }            
    else:
        return {}
    