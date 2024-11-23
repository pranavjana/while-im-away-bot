import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
from textblob import TextBlob
from messages import MESSAGE_CATEGORIES, START_MESSAGE, THANK_YOU_RESPONSE, NEUTRAL_RESPONSE

# Load environment variables
load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcoming message when the command /start is issued."""
    await update.message.reply_text(START_MESSAGE)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button presses from the inline keyboard."""
    query = update.callback_query
    await query.answer()

    category = query.data
    try:
        if category in MESSAGE_CATEGORIES and MESSAGE_CATEGORIES[category]:
            message = random.choice(MESSAGE_CATEGORIES[category])
            await query.message.reply_text(message)
        else:
            await query.message.reply_text("Sorry, no messages available in this category.")
    except Exception as e:
        await query.message.reply_text("An error occurred. Please try again later.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming text messages and perform sentiment analysis."""
    text = update.message.text.lower()
    
    # Check for thank you messages
    if any(phrase in text for phrase in ["thank you", "thanks", "ty"]):
        keyboard = get_category_keyboard()
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(THANK_YOU_RESPONSE, reply_markup=reply_markup)
        return
    
    # Regular sentiment analysis for other messages
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # Choose response based on sentiment
    if polarity < -0.2:
        message = random.choice(MESSAGE_CATEGORIES["supportive"])
        await update.message.reply_text(message)
    elif polarity > 0.2:
        message = random.choice(MESSAGE_CATEGORIES["motivational"])
        await update.message.reply_text(message)
    else:
        keyboard = get_category_keyboard()
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(NEUTRAL_RESPONSE, reply_markup=reply_markup)

def get_category_keyboard():
    """Helper function to create the category keyboard."""
    return [
        [
            InlineKeyboardButton("🌟 Supportive", callback_data="supportive"),
            InlineKeyboardButton("💪 Motivational", callback_data="motivational"),
        ],
        [
            InlineKeyboardButton("😂 Funny", callback_data="funny"),
            InlineKeyboardButton("❤️ Romantic", callback_data="romantic"),
        ],
    ]

def main():
    """Start the bot."""
    application = Application.builder().token(os.getenv('BOT_TOKEN')).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
