from telegram.ext import Application, CommandHandler

async def start(update, context):
    await update.message.reply_text("مرحبًا!")

app = Application.builder().token("7719084399:AAE3iia3g3KHUaXgng5cy6qaxcOpMS9R__8").build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()