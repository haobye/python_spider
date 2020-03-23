
import datetime
import requests
import json


class ZPspider(object):

    def __init__(self):
        self.headers={
            'Referer': 'http://zhaopin.baidu.com/quanzhi?query=&city=%E4%B8%8A%E6%B5%B7',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        }
        self.fp=open('baiduzhaopin.csv',mode='a',encoding='utf-8')
        self.fp.write('{\n')

    def response_hand(self,url):
        session=requests.session()
        response=session.get(url,headers=self.headers)
        return response

    def parse_response(self,response):
        datas=json.loads(response.text).get('data')
        datas=datas['disp_data']
        print(datas)
        resultlist=[]
        for data in datas:
            dict={}
            try:
                dict['officialname'] = data['officialname']  # 公司名称
            except:
                dict['officialname'] = ''
            dict['spidertime']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')##获取当前系统时间并且转化为字符串
            try:
                dict['employertype'] = data['employertype']#所属类型
            except:
                dict['employertype']=''
            try:
                dict['ori_salary'] = data['ori_salary']#工资
            except:
                dict['ori_salary']=''
            try:
                dict['location'] = data['location']#工作地点
            except:
                dict['location']=''
            try:
                dict['_update_time'] = data['_update_time']#采集时间
            except:
                dict['_update_time']=''
            try:
                dict['ri_type']=data['ri_type']#岗位职责
            except:
                dict['ri_type']=''
            try:
                dict['size'] = data['size']#公司规模
            except:
                dict['size']=''
            try:
                dict['companyaddress'] = data['companyaddress']#公司地址
            except:
                dict['companyaddress']=''
            try:
                dict['ori_welfare'] = data['ori_welfare']#公司福利
            except:
                dict['ori_welfare']=''
            try:
                dict['ori_experience'] = data['ori_experience']#工作经验
            except:
                dict['ori_experience']=''
            try:
                dict['salary'] = data['salary']#工资
            except:
                dict['salary']=''
            try:
                dict['name'] = data['name']#职位
            except:
                dict['name']=''
            try:
                dict['age'] = data['age']#年龄要求
            except:
                dict['age']=''
            try:
                dict['education'] = data['education']#学历要求
            except:
                dict['education']=''
            try:
                dict['requirements'] = data['requirements']#任职要求
            except:
                dict['requirements']=''
            resultlist.append(dict)
            print(dict)
        return resultlist

    def save_to_file(self,item):
        self.fp.write(json.dumps(item,ensure_ascii=False)+'\n')

    def close_spider(self):
        self.fp.write("}\n")
        self.fp.close()

    def main(self, i, city):
        url = 'http://zhaopin.baidu.com/api/qzasync?query=&city={}&is_adq=1&pcmod=1&token=%3D%3DwlSr9pUyNqbpVnWq5lSumnV62ZIiYasVpZTGnmUO5l&pn={}&rn=10'.format(city, i)
        response = self.response_hand(url)
        print(response)
        for item in self.parse_response(response):
            self.save_to_file(item)


if __name__ == '__main__':
    c = ZPspider()
    city = input("请输入城市的名字：")
    for i in range(2, 4):
        print(i)
        c.main(i*10, city)
    c.close_spider()





