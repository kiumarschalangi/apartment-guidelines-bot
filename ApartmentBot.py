from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext


# Function to handle /start command
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("General Rules", callback_data="general")],
        [InlineKeyboardButton("Kitchen Rules", callback_data="kitchen")],
        [InlineKeyboardButton("Bathroom Rules", callback_data="bathroom")],
        [InlineKeyboardButton("Cleaning Schedule", callback_data="cleaning")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click a button to see the rules:", reply_markup=reply_markup)

# Function to handle button clicks


async def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    rule_text = RULES.get(query.data, "No rule found.")
    await query.message.reply_text(rule_text)

# Main function to run the bot


def main():
    TOKEN = "YOUR_BOT_API_TOKEN"  # Replace with your actual bot token

    # Create Application instance (New method for version 20+)
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    # Start the bot
    print("Bot is running...")
    app.run_polling()


# Run the bot
if __name__ == "__main__":
    main()


# ---------*RULES*---------

RULES = {
    "general": """🏠 *General Rules*:
    
✨We are excited to have you as a roommate and to share this space with you\! 

📖 To ensure that we all live comfortably and maintain a clean and pleasant environment, please follow these rules:

1\. 📌 *Clean Up After Yourself*:
   \- *Kitchen*: After cooking or using any appliances, clean up immediately \(wipe surfaces, put away utensils, keep the area tidy\)\.
   \- *Bathroom*: Leave the shower and sink clean after use, ensuring no water, hair, or residue is left behind\.
   \- *Toilet & Bidet*: Always clean the seat and ensure no waste or residue is left\.
   \- *Handwashing/Shaving*: Clean and dry the sink after use, removing shaving cream or hair\.

2\. 🏠 *Respect Shared Spaces*:
   \- Keep common areas tidy for everyone\.
   \- Clean up after using shared equipment\.

3\. ⏰ *Quiet Hours*:
   \- Keep noise levels low after *11 PM*\.
   \- Cooking or washing is allowed but should be as quiet as possible\.

⛔ *Failure to Comply & Reporting*:
1\. ❌ *Consequences*:
   \- Repeated failure to follow these rules will result in a report to DoveVivo\.
   \- If needed, a professional cleaning crew will be sent, and the responsible tenant will bear the cost\.

2\. ❗ *Reporting Issues*:
   \- If something is dirty or not in accordance with these rules, take a photo and send it to the group\.
   \- The responsible person must clean it immediately\.

Let's all work together to keep our apartment clean and comfortable\! 🏡""",

    "kitchen": """🍽 *Kitchen Rules*:

1\. 🥣 *Wash Your Dishes Immediately*:
   \- Never leave dirty dishes in the sink\.
   \- If you can't wash them immediately, take them to your room\.
   \- An empty sink ensures smooth use for everyone\.

2\. 🧊 *Keep the Fridge Clean*:
   \- Do not leave spoiled food in the fridge\.
   \- Store food properly in sealed containers\.
   \- Dispose of expired items immediately\.

3\. 🗑 *Trash Bins*:
   \- Always keep the kitchen trash bins clean\.
   \- Follow the *Trash Disposal Schedule*\.

🗑 *Trash and Waste Disposal*:
1\. *Kitchen Trash Bins*:
   \- *Left Bin \(Under Sink\)*: Papers and cartons\.
   \- *Right Bin \(Under Sink\)*: Plastic items\.
   \- *Green Bin \(Next to Sink\)*: Bio & food residue\.

2\. *Trash Disposal Schedule*:
   \- *Trash is taken out every Thursday\.*
   \- The responsibility rotates weekly\.
   \- Even if bins are half full, they must be emptied\.

3\. 🚮 *Personal Trash Bins*:
   \- Each person should have a trash bin in their room\.
   \- Plastic bottles, jars, and glasses should go in *personal* trash bins, not the kitchen bins\.""",

    "bathroom": """🚿 *Bathroom Rules*:

1\. *Clean the Bath After Showering*:
   \- Wipe down excess water\.
   \- Remove any soap or residue\.
   \- Keep the area fresh for the next person\.

2\. *Clean the Toilet After Use*:
   \- Wipe the seat and ensure cleanliness\.
   \- Maintain hygiene for everyone\.

3\. *Clean Up Hair After Shaving or Washing*:
   \- Remove any hair from the sink\.
   \- Keep the bathroom tidy and free of mess\.""",

    "cleaning": """🧹 *Weekly Cleaning Schedule & Responsibilities*:

1\. 🧼 *Cleaning Schedule*:
   \- *Every Saturday or Sunday* \(based on roommate preference\)\.
   \- *Two roommates clean each week* \(rotating schedule\)\.
   \- If everyone follows daily rules, this will be quick and easy\.

2\. *Cleaning Responsibilities*:
   \- *One person* cleans the *bathroom & toilet*\.
   \- *One person* cleans the *kitchen & corridor*\.

3\. *Cleaning Tasks*:
   \- *Floors*: Sweep or vacuum, then mop\.
   \- *Kitchen*: Clean the sink, stove, refrigerator, table, and oven\.
   \- *Bathroom*: Clean the sink, toilet, bath, water hoses, and valves\.

Let's keep our home clean and organized together\! 🏡"""
}
