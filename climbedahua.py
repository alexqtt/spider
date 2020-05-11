import requests
from bs4 import BeautifulSoup
import xlwt


list = []
list2 = []
list3 = []
def getxh(st,end):
    a = 1
    st =st
    for i in range(st,end):
        url = 'https://www.dahuatech.com/product/lists/9.html?area=%d'%i
        url1 = "https://www.dahuatech.com/product/lists/9.html?area=1170"
        response_i = requests.get(url)
        html_i = response_i.content.decode('utf-8')
        soup_i = BeautifulSoup(html_i, "lxml")
        print("第%d页数据"%a)
        print (st)
        dp = (soup_i.find_all('h3'))
        dp_name = soup_i.find_all("p",attrs={"class":"font"})
        #lx_name = soup_i.find("div",attrs={"class":"now"}).children

        a += 1
        st +=1

        for i in dp_name:
            xh_name = (i.get('data-font'))
            #print(xh_name)
            list2.append(xh_name)


        for i in dp:
            xh = (i.get('data-title'))
            #print(xh)
            list.append(xh)


def savexh():
    myxls = xlwt.Workbook()
    sheet1 = myxls.add_sheet(u'top10', cell_overwrite_ok=True)
    for i in range(0, len(list)):

        sheet1.write(i, 0, i + 1)
        sheet1.write(i, 1, list[i])
        sheet1.write(i,2,list2[i])
    myxls.save('HDxh.xls')
    print("写入成功")



if __name__=="__main__":

    getxh(1000, 1205)
    getxh(1340,1599)
    getxh(1207,1319)
    getxh(36,200)
    getxh(1400,1613)
    getxh(896, 1107)
    savexh()





