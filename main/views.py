from django.shortcuts import render
from datetime import datetime
import json
import random
from django.conf import settings
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookHandler,WebhookParser
from linebot.exceptions import InvalidSignatureError,LineBotApiError
from linebot.models import MessageEvent,TextSendMessage,ImageSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parse=WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt    
def callback(request):
    if request.method=='POST':
        signature=request.META['HTTP_X_LINE_SIGNATURE']
        body=request.body.decode('utf-8')
        try:
            events=parse.parse(body,signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        for event in events:
            if isinstance(event,MessageEvent):
                    # event.message.text 代表取得使用者輸入的文字
                    message=event.message.text
                    # 將message 設為一個物件，判斷回傳的資料是文字還是圖片
                    massage_object=None
                    if message=="你好":
                        # TextSendMessage 只能放字串
                        massage_object=TextSendMessage(text="你也好!")
                    elif "樂透" in message:
                        reply_message="預測號碼為：\n"+get_lottory_numbers()        
                        massage_object=TextSendMessage(text=reply_message)                
                    elif "捷運" in message:
                        if "台中" in message:
                            image_url="https://www.jiuh-horng.com/ckfinder/userfiles/images/2018_04_09-%E6%96%B0%E8%81%9E4.jpg"
                        elif "高雄" in message:
                            image_url="https://khh.travel/content/images/static/kmrt-map-l.jpg"
                        else :
                            image_url="https://assets.piliapp.com/s3pxy/mrt_taiwan/taipei/20230214_zh.png"
                        # ImageSendMessage 只能放圖片
                        massage_object=ImageSendMessage(original_content_url=image_url,preview_image_url=image_url)
                    else:
                        massage_object=TextSendMessage(text="我不懂你的意思!")

                    
                    line_bot_api.reply_message(
                        event.reply_token,
                        massage_object
                    )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


# Create your views here.
def index(request):
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"<h1>現在時刻:{now}</h1>")

def get_books(request):
    mybook={
        1:"java-book",
        2:"python-book",
        3:"c-book"
    }
    return HttpResponse(json.dumps(mybook))

def get_lottory_numbers():
    numbers=sorted(random.sample(range(1,50),6))
    x=random.randint(1,50)
    number_str=" ".join(map(str,numbers))+f" 特別號:{x}"
    return number_str

def get_lottory2(request):
    numbers = sorted(random.sample(range(1, 50), 6))
    x = random.randint(1, 50)
    number_str = " ".join(map(str, numbers))
    return render(request, "lottory.html", {"numbers": number_str, "x": x})

def get_lottorys(request):
    numbers=sorted(random.sample(range(1,50),6))
    print(numbers)
    x=random.randint(1,50)
    number_str=" ".join(map(str,numbers))+f" 特別號:{x}"
    return HttpResponse("<h1>本期預測號碼：</h1>"+"<h2>"+number_str+"</h2>")