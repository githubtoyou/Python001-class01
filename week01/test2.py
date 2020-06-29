import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd

def get_usr_name(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    header = {
        'Cookie':'__mta=244258490.1593344042929.1593348768125.1593399421001.33; uuid_n_v=v1; uuid=4739EA70B93311EA8B56A5EC695B0A7314BB41875ACB454C868E7611495AB463; _csrf=ba80e30b3ad07f036889d45d8be70ba04abe947fe464ff24cd7491f210b80349; mojo-uuid=c08518ef802d8e159bdeee6411233621; _lxsdk_cuid=172fab4a684c8-09506609a8bbfb-f7d123e-1fa400-172fab4a684c8; _lxsdk=4739EA70B93311EA8B56A5EC695B0A7314BB41875ACB454C868E7611495AB463; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593344043,1593344053,1593344072,1593344265; mojo-session-id={"id":"aa5ae68ac5952401a6d88debb2c73f5f","time":1593401478661}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593401479; __mta=244258490.1593344042929.1593399421001.1593401478840.34; _lxsdk_s=172fe2035a5-f0-cdd-61a%7C%7C3',
        'Host': 'maoyan.com',
        'user-agent':user_agent
        }
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')
    #print(response.text)
    #print(f'返回码是：{response.status_code}')
    #url_s = []
    for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'})[:10]:
        film_name = tags.find('div').find('span',).text
        print(f'电影名称: {film_name}')
        film_type = tags.find_all('div', attrs={'class': 'movie-hover-title'})[1].text[4:].strip()
        print(f'电影类型: {film_type}')
        Release_time = tags.find_all('div', attrs={'class': 'movie-hover-title'})[3].text[6:].strip()
        print(f'上映时间：{Release_time}')
        print("####################")

        mylist = [film_name, film_type, Release_time]
        list1 = []
        list1.append(mylist)
        movie1 = pd.DataFrame(list1)
        movie1.to_csv('./venv1/test/movie_maoyan1.csv',mode = 'a',encoding='utf_8_sig', index=False, header=False)


    print(f'返回码是：{response.status_code}')



    # mylist = [film_name, plan_date, rating]
    # list1 = []
    # list1.append(mylist)
    # movie1 = pd.DataFrame(list1)
    # movie1.to_csv('./venv1/test/movie1.csv',mode = 'a',encoding='utf_8_sig', index=False, header=False)



#urls = tuple(f'https://maoyan.com/films?showType={ page * 3 }' for page in range(1,2) if page > 0 )
urls = ("https://maoyan.com/films?showType=3",)
print(urls)



for page in urls:
    get_usr_name(page)