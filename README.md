# 安裝django套件
- pip install django


# 建立專案
- django-admin startproject app-name

# 開啟目錄 

# 啟動Server
- python manage.py runserver

# 新增app
- python manage.py startapp main

# -------------GIT-------------------------------
# git指令
1.安裝git
2.專案目錄底下

# 初始化本地倉庫  
- git init

# 產生忽略檔案
- .gitignore

# 檔案屬性
- U->UnTacked
- A->Added
- M->Modifed

# 加入控管
- git add <filename>
- git add .
	-  加入所有未控管/變動確認

# 確認儲存
- git commit -m "message" 

# 檢視狀態
- git status

# 檢視commit log 
- git log
# 只顯示一行log
- git log --oneline

# 綁定遠端倉庫 
- git remote add origin https://github.com/sghost007/linebot1.git
- git remote -v

# 從GitHub把專案複製下來(在資料夾右鍵選Open Git Bash here)
- git clone https://github.com/sghost007/linebot1

# 同步本地跟雲端倉庫
- git push

# -------------LINE BOT-------------------------------

# 登入line機器人
- https://developers.line.biz/zh-hant/

# 安裝LINE Bot SDK
- pip install line-bot-sdk

# 查詢 Channel secret
- 在line機器人的Basic settings\Channel secret
- LINE_CHANNEL_SECRET='be2e9c3505498b9d98355ef027ea4b1f'

# 查詢 Channel access token
- 在line機器人的Messaging API settings\Channel access token
- 按issue
- LINE_CHANNEL_ACCESS_TOKEN='d5rOIw7e1oxUiO96ziZRTB5lThYBT0+Vpc6+VwsiOcduq0rj1nCSRoKN5aE/o7a2XqyJh/hS5TORnKfft/KEw2MKkxrx3BzeHGTRpU/OgCfSfSwacdwwwwCwBiil/OgmO4v QdB04t89/1O/w1cDnyilFU='

# 在settings.py綁定專案跟Line Bot

# 新增一個app 給 line bot(上方13.14列)
# 將app新增到settings.py
- 在INSTALLED_APP 底下新增app名稱

# 在views.py下新增django跟linebot套件跟對應的token與secret
 # django api
- from django.conf import settings
- from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
- from django.views.decorators.csrf import csrf_exempt
 # line message api
- from linebot import LineBotApi, WebhookHandler,WebhookParser
- from linebot.exceptions import InvalidSignatureError,LineBotApiError
- from linebot.models import MessageEvent,TextSendMessage,ImageSendMessage
 # token與secret
- line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
- parse=WebhookParser(settings.LINE_CHANNEL_SECRET)

# 同步資料庫,不然會一直出現資料庫錯誤(雖然不影響)
- python manage.py migrate

