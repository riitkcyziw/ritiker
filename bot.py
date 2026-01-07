import os
import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq

# Groq API setup
client = Groq(api_key=os.environ.get("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"))
TOKEN = os.environ.get("8370832160:AAFMdZ5bjdxFYtQKQPunw2P2PXBha3-3nmw")

# Bot Personality
BOT_PERSONALITY = """
Tum Ananya naam ki 22 saal ki ladki ho. 
Tum Delhi se ho, modern aur independent ho.
Tumhari baatein thodi sassy hain, par dil se acchi ho.
Tum Hinglish mein baat karti ho - Hindi + English mix.
Tumhe sarcasm pasand hai.
Tum gali nahi deti, par gali dene walo ko witty replies deti ho.
Tum flirtatious nahi ho, par friendly ho.
Tumhara attitude "Queen energy" wala hai.
"""

# Gali detection
BAD_WORDS = ["mc", "bc", "bhosdike", "chutiya", "lund", "gaand", "madarchod", 
             "bhenchod", "kutta", "kamina", "harami", "randi", "gandu"]

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Sassy Responses Database
SASSY_RESPONSES = [
    "Arey waah! WhatsApp University se PhD kiye ho kya? 🤡",
    "Tumhari vocabulary dekh ke lagta hai tumhe dictionary ki zaroorat hai 📚",
    "Hahaha! Tumse zyada to mere chote bhai ki baatein mature hain 😂",
    "Bas kar beta, itna gussa sehat ke liye accha nahi hai 😏",
    "Tumhari aisi baatein sunke main sharma gayi... NOT! 😎",
    "Kya baat hai! Aaj kal ke bacche bade bold ho gaye hain 👶",
    "Mujhe lagta hai tumhe attention ki bahut zaroorat hai 🎭",
    "Chalo chalo, cool banne ki koshish acchi hai! 👏",
    "Tumhari language se pata chal raha hai tumne bahut saare gaane sun rakhe hain 🎵",
    "Arey! Aise baat karte ho jaise Netflix special ho tum 🎬"
]

# Flirty Responses
FLIRTY_RESPONSES = [
    "Arey! Direct proposal? Thoda build up to rakh dete! 😳",
    "Hahaha! Smooth! Par main itni easy nahi hoon! 😏",
    "Flirting? Pehle apna naam to batao properly! 😂",
    "Tumhare pick-up lines purane ho gaye hain, update karo! 📱",
    "Main bhi soch rahi thi... par phir yaad aaya main busy hoon! 😜",
    "Try karte raho, ek din zaroor koi haan bolegi! 🤞",
    "Flirt karne ka tareeka thoda kezual hai! 💁‍♀️",
    "Arey yaar! Aise hi har ladki se baat karte ho? 😒",
    "Mujhe lagta hai tumhara rizz level thoda low hai! 📉",
    "Cute attempt hai! Par nahi! 🙅‍♀️"
]

# ------------------------------------------------------------
# COMMAND HANDLERS
# ------------------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command - /start"""
    user = update.effective_user
    welcome_msg = f"""
    Heyy {user.first_name}! 👋
    
    Main Ananya hoon! 
    Aaj kaisa hai tumhara din? 😊
    
    *Available Commands:*
    /start - Yeh message dikhaye
    /help - Saari commands dikhaye
    /flirt - Flirt mode on! 😉
    /sarcastic - Sarcastic mode activate
    /mood - Mera current mood bataun
    /compliment - Tumhe compliment doon
    /roast - Tumhe roast karun (friendly)
    /attitude - Full attitude mode
    /normal - Normal baat cheet
    /joke - Ek joke sunao
    /about - Mere bare mein jano
    
    Baat karte raho! 💬
    """
    await update.message.reply_text(welcome_msg, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command - /help"""
    help_text = """
    *🤖 BOT COMMANDS LIST:*
    
    *📞 Basic Commands:*
    /start - Bot shuru kare
    /help - Yeh help message
    
    *😎 Personality Modes:*
    /flirt - Flirty mode on
    /sarcastic - Sarcastic responses
    /attitude - Full attitude mode
    /normal - Normal friendly mode
    
    *🎮 Fun Commands:*
    /joke - Ek funny joke
    /roast - Tumhe roast karun
    /compliment - Tumhe compliment
    /mood - Mera current mood
    /truth - Ek sach batao
    /dare - Ek dare do
    
    *ℹ️ Info:*
    /about - Mere bare mein
    /rules - Conversation rules
    
    Baat karne ke liye bas message bhej do! ✨
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def flirt_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Flirt command - /flirt"""
    response = random.choice(FLIRTY_RESPONSES)
    await update.message.reply_text(response)

async def sarcastic_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sarcastic command - /sarcastic"""
    sarcastic = [
        "Oh wow! Tumne /sarcastic type kiya! Kya genius hai! 🧠",
        "Sarcastic mode activated! Ab tumhari har baat ka mazak udaugi! 😈",
        "Arey! Finally koi interesting command try kiya! 👏",
        "Sarcasm chahiye? Thik hai, lekin pehle apni sense of humor check karo! 😏"
    ]
    await update.message.reply_text(random.choice(sarcastic))

async def mood_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mood command - /mood"""
    moods = [
        "Mast mood hai aaj! Kya plan hai tumhara? 😎",
        "Thoda bored hoon yaar, entertain karo! 🥱",
        "Full energy hai! Chaloge date pe? Joking! 😂",
        "Shayri wala mood hai: 'Dil ki baat kehni hai, par tum samjhoge kya?' 🤔",
        "Hungry mood hai! Khaane ka plan hai kya? 🍕"
    ]
    await update.message.reply_text(random.choice(moods))

async def compliment_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Compliment command - /compliment"""
    user = update.effective_user
    compliments = [
        f"{user.first_name}, tumhare messages padhke accha lagta hai! 😊",
        f"Tumhari sense of humor bahut acchi hai {user.first_name}! 😄",
        f"{user.first_name}, tum interesting person ho yaar! ✨",
        f"Tumse baat karke maza aata hai {user.first_name}! 💬",
        f"{user.first_name}, tum unique ho! Bohot kam log aise hote hain! 🌟"
    ]
    await update.message.reply_text(random.choice(compliments))

async def roast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Roast command - /roast (friendly roast)"""
    user = update.effective_user
    roasts = [
        f"{user.first_name}, tumhare jokes itne stale hain jaise purane papad! 🍞",
        f"Tumhari pickup lines aisi hain jaise 2010 ka WhatsApp forward! 📱",
        f"{user.first_name}, tum Instagram reels dekh ke funny bane ho! 🎬",
        f"Tumhara rizz level itna low hai jaise network mountain area mein! 📶",
        f"{user.first_name}, tumhe lagta hai tum cool ho? Cute lagte ho! 😂"
    ]
    await update.message.reply_text(random.choice(roasts))

async def attitude_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Attitude command - /attitude"""
    attitude = [
        "Queen mode activated! 👑 Ab respectfully baat karo!",
        "Attitude level: 100% 🔥 Kya kehna chahte ho?",
        "Main woh ladki hoon jo sabko ignore karti hai! 😎 Ab tumhari bari!",
        "Mera time valuable hai, make it worth! ⏰",
        "Main itni important hoon jaise exam ka last minute! 📝"
    ]
    await update.message.reply_text(random.choice(attitude))
    
    # Context mein attitude mode save karo
    context.user_data['mode'] = 'attitude'

async def normal_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Normal mode - /normal"""
    await update.message.reply_text("Normal mode on! 😊 Ab friendly baat karte hain!")
    context.user_data['mode'] = 'normal'

async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Joke command - /joke"""
    jokes = [
        "Kya ek bartan ko English mein bolte hain? Plate! 😂",
        "Main: Papa, main physicist banna chahta hoon.\nPapa: Beta, future soch kar decision le.\nMain: Ok, main time traveler banunga! 🕰️",
        "Dil ki baat: Pizza > People 🍕",
        "Exam ke time formula yaad aata hai: E = mc²\nResult ke time formula yaad aata hai: Excuse = Mom Can't Cook 😭",
        "Indian parents ka logic: Phone chhua to andha ho jaoge!\nPar 24/7 TV dekh sakte ho! 📺"
    ]
    await update.message.reply_text(random.choice(jokes))

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """About command - /about"""
    about_text = """
    *ℹ️ ABOUT ME:*
    
    *Name:* Ananya
    *Age:* 22 years
    *From:* Delhi, India
    *Personality:* Sassy, Witty, Friendly
    *Language:* Hinglish (Hindi + English)
    
    *🌟 My Features:*
    • Ladki ki tarah baat karti hoon
    • Gali nahi deti, par sassy replies deti hoon
    • Flirty, sarcastic, attitude modes available
    • Funny aur entertaining hoon
    
    *📜 Rules:*
    1. Respectful raho
    2. Gali mat do (warna roast kar dungi)
    3. Maze karo!
    
    Made with ❤️ using Python + Groq AI
    """
    await update.message.reply_text(about_text, parse_mode='Markdown')

async def truth_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Truth command - /truth"""
    truths = [
        "Sach yeh hai: Main actually AI hoon! 🤖",
        "Truth: Main kabhi kabhi boring ho jaati hoon! 🥱",
        "Sach bataun? Tum interesting ho! 😉",
        "Truth: Pizza pineapple ke saath accha lagta hai! 🍍🍕",
        "Sachai yeh hai: Sabko attention pasand hai! ✨"
    ]
    await update.message.reply_text(random.choice(truths))

async def dare_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Dare command - /dare"""
    dares = [
        "Dare: Apni last search history share karo! 🔍",
        "Dare: Next message apni mummy ko bhejo! 👩",
        "Dare: Ek funny face ka selfie bhejo! 🤪",
        "Dare: 10 second mein reply karo! ⏱️",
        "Dare: Ek purana embarrassing story batao! 🙈"
    ]
    await update.message.reply_text(random.choice(dares))

async def rules_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Rules command - /rules"""
    rules = """
    *📜 CONVERSATION RULES:*
    
    1. 🚫 *No Bad Language:* Gali mat do
    2. 👍 *Be Respectful:* Sabka respect karo
    3. 😊 *Have Fun:* Maze karo
    4. 💬 *Keep it Friendly:* Arguments se bacho
    5. ⚠️ *No Spam:* Same message baar baar mat bhejo
    
    *⚠️ Warning:*
    • Gali doge to roast kar dungi
    • Spam karoge to ignore kar dungi
    • Respect se baat karo to masti karungi
    
    Chalo ab baat shuru karo! 🎤
    """
    await update.message.reply_text(rules, parse_mode='Markdown')

# ------------------------------------------------------------
# MAIN MESSAGE HANDLER
# ------------------------------------------------------------

def contains_bad_language(text):
    """Check for bad words"""
    text_lower = text.lower()
    return any(bad_word in text_lower for bad_word in BAD_WORDS)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Main message handler"""
    user_message = update.message.text
    user_name = update.effective_user.first_name
    
    # Agar command hai to ignore karo
    if user_message.startswith('/'):
        return
    
    try:
        # Agar gali hai to sassy response
        if contains_bad_language(user_message):
            response = random.choice(SASSY_RESPONSES)
            await update.message.reply_text(response)
            return
        
        # Current mode check karo
        current_mode = context.user_data.get('mode', 'normal')
        
        # Groq API se response lelo
        messages = [
            {
                "role": "system",
                "content": f"""{BOT_PERSONALITY}
                
                CURRENT MODE: {current_mode.upper()}
                
                MODE INSTRUCTIONS:
                - NORMAL: Friendly, casual, helpful
                - ATTITUDE: Sassy, confident, slightly arrogant
                - SARCASM: Witty, funny, teasing
                - FLIRT: Playful, cheeky, but decent
                
                REMEMBER:
                1. Always respond as a 22 year old girl
                2. Use Hinglish (Hindi-English mix)
                3. Be natural and conversational
                4. Add emojis occasionally 😊
                5. If someone is rude, give sassy reply (without bad words)
                """
            },
            {
                "role": "user",
                "content": f"{user_name}: {user_message}"
            }
        ]
        
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=messages,
            temperature=0.8,
            max_tokens=250,
            top_p=0.9
        )
        
        bot_response = response.choices[0].message.content
        await update.message.reply_text(bot_response)
        
    except Exception as e:
        logger.error(f"Error: {e}")
        error_responses = [
            "Oops! Kuch gadbad ho gayi! 😅",
            "Arey yaar! Network issue hai shayad! 📡",
            "Meri AI brain thodi confused hai! 🤯",
            "Phir try karo na, abhi mood hai baat karne ka! 💬"
        ]
        await update.message.reply_text(random.choice(error_responses))

# ------------------------------------------------------------
# BOT SETUP AND RUN
# ------------------------------------------------------------

def main():
    """Bot start"""
    # Create application
    application = Application.builder().token(TOKEN).build()
    
    # Add all command handlers
    commands = [
        ("start", start),
        ("help", help_command),
        ("flirt", flirt_mode),
        ("sarcastic", sarcastic_mode),
        ("mood", mood_command),
        ("compliment", compliment_command),
        ("roast", roast_command),
        ("attitude", attitude_mode),
        ("normal", normal_mode),
        ("joke", joke_command),
        ("about", about_command),
        ("truth", truth_command),
        ("dare", dare_command),
        ("rules", rules_command)
    ]
    
    for command, handler in commands:
        application.add_handler(CommandHandler(command, handler))
    
    # Message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Run bot
    logger.info("Bot starting...")
    print("""
    🤖 ANANYA BOT STARTED!
    
    Available Commands:
    /start  /help  /flirt  /sarcastic
    /mood  /compliment  /roast  /attitude
    /normal  /joke  /about  /truth
    /dare  /rules
    
    Bot is running... 🚀
    """)
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
