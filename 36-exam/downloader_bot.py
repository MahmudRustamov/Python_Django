# import os
# import re
# import asyncio
# from pyrogram import Client, filters
# from pyrogram.errors import FloodWait, MessageIdInvalid, ChannelPrivate, ChatIdInvalid, PeerIdInvalid, UserNotParticipant
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# # --- Configuration ---
# # You need to get these from my.telegram.org
# # API_ID: Go to my.telegram.org/apps, log in, and create a new application.
# # API_HASH: Will be provided along with API_ID.
# API_ID = 1234567  # Replace with your actual API ID
# API_HASH = "your_api_hash_here"  # Replace with your actual API Hash

# # BOT_TOKEN: Get this from @BotFather on Telegram by creating a new bot.
# # If you want to run this as a USER ACCOUNT (self-bot) for "universal" access
# # to private channels you are a member of, you can leave BOT_TOKEN as None or comment it out.
# # If you leave it as None, Pyrogram will prompt you for your phone number and OTP on first run.
# # If you want to run it as an OFFICIAL BOT (limited access to channels where it's an admin),
# # uncomment and provide your BOT_TOKEN.
# BOT_TOKEN = None  # Replace with your actual Bot Token, or leave as None for user account

# # Session name for Pyrogram. This will create a .session file to store your login.
# SESSION_NAME = "media_downloader_session"

# # Directory to save downloaded files
# DOWNLOAD_DIR = "downloads"
# os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# # --- Pyrogram Client Initialization ---
# # Initialize the Pyrogram Client.
# # If BOT_TOKEN is provided, it runs as a bot.
# # If BOT_TOKEN is None, it runs as a user account (self-bot).
# if BOT_TOKEN:
#     app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
#     logger.info("Client initialized as a Bot account.")
# else:
#     app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)
#     logger.info("Client initialized as a User account (Self-Bot).")
#     logger.warning("Using a user account (self-bot) may violate Telegram's Terms of Service. Use with caution and for personal, legitimate purposes only.")


# # --- Helper Function to Parse Telegram Message Links ---
# def parse_telegram_link(link: str):
#     """
#     Parses a Telegram message link to extract chat identifier and message ID.
#     Supports:
#     - https://t.me/c/CHANNEL_ID_PART/MESSAGE_ID (for private channels)
#     - https://t.me/USERNAME/MESSAGE_ID (for public channels)
#     """
#     # Pattern for t.me/c/ID/MSG_ID (private channels)
#     match_c_link = re.match(r"https?://t\.me/c/(\d+)/(\d+)", link)
#     if match_c_link:
#         channel_id_part = match_c_link.group(1)
#         # Telegram's actual chat_id for c/ links is -100 + the ID part
#         chat_id = int(f"-100{channel_id_part}")
#         message_id = int(match_c_link.group(2))
#         logger.info(f"Parsed c/ link: Chat ID = {chat_id}, Message ID = {message_id}")
#         return chat_id, message_id

#     # Pattern for t.me/USERNAME/MSG_ID (public channels)
#     match_username_link = re.match(r"https?://t\.me/([^/]+)/(\d+)", link)
#     if match_username_link:
#         channel_username = match_username_link.group(1)
#         message_id = int(match_username_link.group(2))
#         logger.info(f"Parsed username link: Username = @{channel_username}, Message ID = {message_id}")
#         return f"@{channel_username}", message_id # Pyrogram can resolve usernames
    
#     logger.warning(f"Failed to parse link: {link}")
#     return None, None # Invalid link format

# # --- Message Handler for the /download command ---
# @app.on_message(filters.command("download") & filters.private)
# async def download_command_handler(client, message):
#     """
#     Handles the /download command.
#     Expects a Telegram message link as an argument.
#     """
#     logger.info(f"Received /download command from user {message.from_user.id}")

#     if len(message.command) < 2:
#         await message.reply_text(
#             "Please provide a Telegram message link. "
#             "Example: `/download https://t.me/your_channel_username/123` "
#             "or `/download https://t.me/c/1234567890/123`"
#         )
#         return

#     link = message.command[1]
#     chat_identifier, msg_id = parse_telegram_link(link)

#     if chat_identifier is None:
#         await message.reply_text(
#             "Invalid Telegram message link format. "
#             "Please ensure it's a valid `https://t.me/c/ID/MSG_ID` or `https://t.me/USERNAME/MSG_ID` link."
#         )
#         return

#     status_message = await message.reply_text(
#         f"Attempting to fetch message `{msg_id}` from `{chat_identifier}`... Please wait."
#     )

#     try:
#         # Retrieve the message object from the specified chat and message ID
#         target_message = await client.get_messages(chat_id=chat_identifier, message_ids=msg_id)

#         if not target_message:
#             await status_message.edit_text(
#                 "Could not find the specified message. "
#                 "Ensure the link is correct and the bot/user account has access to the channel/chat."
#             )
#             return

#         if target_message.media:
#             await status_message.edit_text("Media found! Starting download...")
#             try:
#                 # Construct a safe file name
#                 file_name_prefix = f"{target_message.chat.id}_{target_message.id}"
                
#                 # Pyrogram automatically handles file extensions based on media type
#                 # We just provide the directory and a base name.
#                 file_path = await target_message.download(
#                     file_name=os.path.join(DOWNLOAD_DIR, file_name_prefix),
#                     progress=download_progress, # Optional: show download progress
#                     progress_args=(status_message,) # Pass the status message to update progress
#                 )
                
#                 await status_message.edit_text(f"Download complete! Sending file...")
#                 logger.info(f"Downloaded file: {file_path}")

#                 # Send the downloaded file back to the user
#                 # Pyrogram automatically detects file type for send_document, send_video, etc.
#                 # For simplicity, we'll use send_document which handles most types.
#                 await message.reply_document(
#                     document=file_path,
#                     caption=f"Downloaded from: `{link}`\n\nOriginal caption: {target_message.caption or 'N/A'}",
#                     quote=True # Reply to the user's command
#                 )
#                 logger.info(f"Sent file back to user {message.from_user.id}")

#                 # Clean up the downloaded file locally after sending
#                 os.remove(file_path)
#                 logger.info(f"Deleted local file: {file_path}")
#                 await status_message.delete() # Delete the progress message
                
#             except FloodWait as e:
#                 await status_message.edit_text(f"Telegram is limiting requests. Please try again in {e.value} seconds.")
#                 logger.error(f"FloodWait error: {e}")
#             except Exception as download_error:
#                 await status_message.edit_text(f"Failed to download media: `{download_error}`")
#                 logger.error(f"Error during media download for link {link}: {download_error}", exc_info=True)
#         else:
#             await status_message.edit_text("No media (photo, video, document, etc.) found in the specified message.")

#     except MessageIdInvalid:
#         await status_message.edit_text("The message ID provided is invalid or the message does not exist.")
#         logger.error(f"MessageIdInvalid for link {link}")
#     except (ChannelPrivate, ChatIdInvalid, PeerIdInvalid, UserNotParticipant):
#         await status_message.edit_text(
#             "Access Denied: The bot/user account does not have permission to access this channel/chat, "
#             "or you are not a member of this private channel. "
#             "If this is a private channel, ensure you are running a user account (self-bot) "
#             "and are a member of the channel. If it's a public channel, ensure the bot is an admin."
#         )
#         logger.error(f"Access Denied for link {link}")
#     except FloodWait as e:
#         await status_message.edit_text(f"Telegram is limiting requests. Please try again in {e.value} seconds.")
#         logger.error(f"FloodWait error: {e}")
#     except Exception as e:
#         await status_message.edit_text(f"An unexpected error occurred: `{e}`")
#         logger.error(f"Unexpected error for link {link}: {e}", exc_info=True)

# # --- Optional: Download Progress Callback ---
# async def download_progress(current, total, status_message):
#     """
#     Callback function to update the download progress message.
#     """
#     try:
#         percentage = f"{current * 100 / total:.1f}%"
#         await status_message.edit_text(f"Downloading: {percentage}")
#     except Exception as e:
#         logger.warning(f"Could not update download progress message: {e}")


# # --- Main function to run the bot ---
# async def main():
#     """
#     Starts the Pyrogram client and keeps it running.
#     """
#     logger.info("Starting Telegram Media Downloader...")
#     await app.start()
#     user_info = await app.get_me()
#     logger.info(f"Client logged in as: {user_info.first_name} (@{user_info.username})")
#     logger.info("Bot is ready! Send a /download command with a Telegram message link in private chat.")
    
#     # Keep the bot running indefinitely
#     await asyncio.Event().wait()

# if __name__ == "__main__":
#     asyncio.run(main())
