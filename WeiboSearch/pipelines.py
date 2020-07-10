# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import datetime
import re
import time

import pymongo
from pymongo.errors import DuplicateKeyError

from WeiboSearch.items import *
from WeiboSearch.settings import LOCAL_MONGO_HOST, LOCAL_MONGO_PORT, DB_NAME, WEIBO_COLLECTION, USER_COLLECTION


# items中加入时间戳
class TimePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, TweetsItem) or isinstance(item, InformationItem):
            now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            item['crawled_at'] = now
        return item


# 清洗时间
class WeiboSpiderPipeline(object):
    def parse_time(self, date):
        if re.match('刚刚', date):
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        if re.match('\d+分钟前', date):
            minute = re.match('(\d+)', date).group(1)
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - float(minute) * 60))
        if re.match('\d+小时前', date):
            hour = re.match('(\d+)', date).group(1)
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - float(hour) * 60 * 60))
        if re.match('昨天.*', date):
            date = re.match('昨天(.*)', date).group(1).strip()
            date = time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60)) + ' ' + date
        if re.match('\d{2}月\d{2}日', date):
            now_time = datetime.datetime.now()
            date = date.replace('月', '-').replace('日', '')
            date = str(now_time.year) + '-' + date
        if re.match('今天.*', date):
            date = re.match('今天(.*)', date).group(1).strip()
            date = time.strftime('%Y-%m-%d', time.localtime(time.time())) + ' ' + date
        return date

    def process_item(self, item, spider):
        if isinstance(item, TweetsItem):
            if item.get('created_at'):
                item['created_at'] = item['created_at'].strip()
                item['created_at'] = self.parse_time(item.get('created_at'))
            if item.get('pictures'):
                item['pictures'] = [pic.get('url') for pic in item.get('pictures')]
        return item


class MongoPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)
        # 数据库名
        db = client[DB_NAME]
        # 数据库的 集合 名
        self.Information = db[USER_COLLECTION]
        self.Tweets = db[WEIBO_COLLECTION]

    def process_item(self, item, spider):

        if isinstance(item, TweetsItem):
            self.insert_item(self.Tweets, item)
        elif isinstance(item, InformationItem):
            self.insert_item(self.Information, item)

        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            """
            说明有重复数据
            """
            collection.update_one({'id_str': item['id_str']}, {'$set': dict(item)}, upsert=True)
            return
            # pass
