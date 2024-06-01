from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import logging
from pytube import YouTube
from io import BytesIO
from pydub import AudioSegment

# Replace with your bot token and channel username
BOT_TOKEN = "your token"
CHANNEL_USERNAME = "@infoviral_ku"

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    
    welcome_message = (
        "Hello, welcome to @mydownloadyoutubebot bot.\n"
        "Please join the following channel first:\n"
        f"{CHANNEL_USERNAME}\n\n"
        "If you have joined, click the Refresh button to continue."
    )
    
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("Refresh", callback_data='refresh')]
    ]
    
    with open('my.png', 'rb') as photo:
        update.message.reply_photo(photo=photo, caption=welcome_message, reply_markup=InlineKeyboardMarkup(keyboard))

# Check membership
def check_membership(user_id, context: CallbackContext) -> bool:
    try:
        chat_member = context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return chat_member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        logger.error(f"Error checking membership: {e}")
        return False

# Handle button presses
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id

    if query.data == 'refresh':
        if check_membership(user_id, context):
            query.edit_message_caption(caption="Thank you for joining! Please select the menu below.", reply_markup=main_menu())
        else:
            query.edit_message_caption(caption=f"You have not joined the channel {CHANNEL_USERNAME}. Please join first.", reply_markup=refresh_menu())
    elif query.data in ['download_mp3', 'download_mp4']:
        handle_action(update, context)

def refresh_menu():
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("Refresh", callback_data='refresh')]
    ]
    return InlineKeyboardMarkup(keyboard)

def main_menu():
    keyboard = [
        [InlineKeyboardButton("Download MP3", callback_data='download_mp3')],
        [InlineKeyboardButton("Download MP4", callback_data='download_mp4')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Handle actions for downloads
def handle_action(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    action = query.data
    
    if action == 'download_mp3':
        context.bot.send_message(chat_id=user_id, text="Please enter the YouTube link to download MP3.")
        context.user_data['action'] = 'download_mp3'
    elif action == 'download_mp4':
        context.bot.send_message(chat_id=user_id, text="Please enter the YouTube link to download MP4.")
        context.user_data['action'] = 'download_mp4'

def download_youtube_video(url, file_format):
    yt = YouTube(url)
    buffer = BytesIO()
    
    if file_format == 'mp3':
        stream = yt.streams.filter(only_audio=True).first()
        audio_file = BytesIO()
        stream.stream_to_buffer(audio_file)
        audio_file.seek(0)
        audio = AudioSegment.from_file(audio_file)
        audio.export(buffer, format="mp3")
        buffer.seek(0)
        return buffer, yt.title + '.mp3'
    elif file_format == 'mp4':
        stream = yt.streams.get_highest_resolution()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)
        return buffer, yt.title + '.mp4'

def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    text = update.message.text

    if 'action' in context.user_data:
        action = context.user_data['action']
        context.bot.send_message(chat_id=user_id, text="Your request is being processed...")
        
        try:
            if action == 'download_mp3':
                buffer, filename = download_youtube_video(text, 'mp3')
                context.bot.send_audio(chat_id=user_id, audio=buffer, filename=filename)
            elif action == 'download_mp4':
                buffer, filename = download_youtube_video(text, 'mp4')
                context.bot.send_video(chat_id=user_id, video=buffer, filename=filename)
            context.bot.send_message(chat_id=user_id, text="Do you want to use the bot again? Please choose the following menu:", reply_markup=main_menu())
        except Exception as e:
            context.bot.send_message(chat_id=user_id, text=f"An error occurred: {e}")
        
        del context.user_data['action']
    else:
        if text.lower() == 'halo':
            context.bot.send_message(chat_id=user_id, text="Hello! How can I assist you?")

# Function to handle errors (optional but useful for debugging)
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f"Update {update} caused error {context.error}")

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handlers for commands and messages
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Register the error handler
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
