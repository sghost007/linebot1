import requests
from bs4 import BeautifulSoup

def get_soup(url,post_data=None):
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'  
    }
    try:
        if post_data is not None:
            resp=requests.post(url,post_data,headers=headers)
        else:
            resp=requests.get(url,headers=headers)            
        resp.encoding='utf-8'
        if resp.status_code==200:
            soup=BeautifulSoup(resp.text,'lxml')
            return soup
        else:
            print('網頁取得失敗',resp.status_code)
    except Exception as e:
        print('網址錯誤',e)
        
    # 失敗則回傳None
    return None

# 爬找發票
def get_invoice_numbers():
    numbers=[]
    try:
        url='https://invoice.etax.nat.gov.tw/'
        soup=get_soup(url)
        trs=soup.find('table',class_="etw-table-bgbox etw-tbig").find_all('tr')
        datas=[[td.text.strip() for td in tr.find_all('td')]for tr in trs[1:4]]
        for data in datas:
            numbers+=data[1].split()[:-1]
    except Exception as e:
        print(e)

    return numbers

# invoice_num=使用者輸入的號碼,numbers=爬蟲的串列
def search_invoice_bingo(invoice_num,numbers):
    bingo=False
    for i in range(len(numbers)):
        if numbers[i][5:] == invoice_num[len(invoice_num)-3:]:
            bingo=True
            break

    message=''    
    if bingo:
        if i==0:
            message=f'有機會中特別獎1,000萬元(8個號碼)'
        elif i==1:
            message=f'有機會中特獎200萬元(8個號碼)'
        else:
            message=f'有機會中頭獎20萬(3個號碼中200元)'
        
        message+=f'\n請繼續對號碼==>{numbers[i]}'
    else:
        message='@@沒有中獎!!'

    return message


if __name__=='__main__':
    numbers=get_invoice_numbers()
    print(numbers)
    print(search_invoice_bingo('09505837',numbers))
    print(search_invoice_bingo('897',numbers))
