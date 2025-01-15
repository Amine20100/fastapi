from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler
from dotenv import load_dotenv
import os
import requests

# تحميل القيم من ملف .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# إعداد البوت
bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot, None, use_context=True)

# إنشاء تطبيق FastAPI
app = FastAPI()

# تعريف أمر /start
def start(update, context):
    update.message.reply_text("مرحبًا! أنا بوت تيليجرام.")

dispatcher.add_handler(CommandHandler("start", start))

# نقطة استقبال Webhook
@app.post("/webhook")
async def webhook(request: Request):
    json_update = await request.json()
    update = Update.de_json(json_update, bot)
    dispatcher.process_update(update)
    return {"status": "ok"}

# نقطة اختبار
@app.get("/")
def home():
    return {"message": "البوت يعمل!"}

# إعداد Webhook عند بدء التشغيل
@app.on_event("startup")
def set_webhook():
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}")