# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# 将文件保存为text格式
class SpiderMaoyanPipeline:
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
        title = item['title']
        film_type = item['film_type']
        Release_time = item['Release_time']
        output = f'|{title}|\t|{film_type}|\t|{Release_time}|\n\n'
        with open('./maoyan_movie3.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item

# 将文件保存为csv格式

class SpiderMaoyanPipeline2:
    # def process_item(self, item, spider):
    #     return item

    def __init__(self):
        self.f = open("./maoyan_first10.csv", "w",encoding='utf-8')
        self.writer = csv.writer(self.f)
        self.writer.writerow(['title', 'film_type', 'Release_time'])

    def process_item(self, item, spider):
        maoyan_list =  [item['title'], item['film_type'], item['Release_time']]
        self.writer.writerow(maoyan_list)
        return item
    def close_spider(self, spider):#关闭
        #self.writer.close()
        self.f.close()        
