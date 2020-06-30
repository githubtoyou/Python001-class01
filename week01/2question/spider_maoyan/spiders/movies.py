# -*- coding: utf-8 -*-
import scrapy
#from bs4 import BeautifulSoup
from spider_maoyan.items import SpiderMaoyanItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']
    # def parse(self, response):
    #     pass
    def start_requests(self):
        # url = 'https://maoyan.com/films?showType=3'
        # yield scrapy.Request(url=url, callback=self.parse)

        for page in range(0, 1):
            if page == 0:
                page = 1
                url = f'https://maoyan.com/films?showType={ page * 3 }'
                #print(urls)
                yield scrapy.Request(url=url, callback=self.parse)
            else:
                url = f'https://maoyan.com/films?showType={ page * 30 }'
                #print(urls)
                yield scrapy.Request(url=url, callback=self.parse)
    # 解析函数
    def parse(self, response):
        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_list = soup.find_all('div', attrs={'class': 'movie-hover-info'})[:10]
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        # for i in title_list:
        #     # 在items.py定义
        #     item = SpiderMaoyanItem()
        #     title = i.find('div').find('span',).text
        #     film_type = i.find_all('div', attrs={'class': 'movie-hover-title'})[1].text[4:].strip()
        #     Release_time = i.find_all('div', attrs={'class': 'movie-hover-title'})[3].text[6:].strip()
        #     item['title'] = title
        #     item['film_type'] = film_type
        #     item['Release_time'] = Release_time
        #     #yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
        #     yield item
        for movie in movies[:10]:
        #     title = i.find('a').find('span',).text
        #     link = i.find('a').get('href')
            # 路径使用 / .  .. 不同的含义　
            title = movie.xpath('./div[1]/span/text()')
            film_type = movie.xpath('./div[2]/text()')
            Release_time = movie.xpath('./div[4]/text()')
            print('##############')
            print(title.extract()[0])
            print(film_type.extract()[1].strip())
            print(Release_time.extract()[1].strip())
            item = SpiderMaoyanItem()
            item['title'] = "电影名称：" + title.extract()[0]
            item['film_type'] = "电影类型：" +  film_type.extract()[1].strip()
            item['Release_time'] = "上映时间：" +  Release_time.extract()[1].strip()  
            yield item          
       


