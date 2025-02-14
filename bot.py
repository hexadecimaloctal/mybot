from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler,filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def echo(update:Update,context: ContextTypes.DEFAULT_TYPE)-> None:
    await update.message.reply_text(update.message.text +" by jaspal ")


app = ApplicationBuilder().token("7656360851:AAGihyPJPGFRkiKZhErUrSj6IU5IaWIYrz4").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
