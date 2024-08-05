import logging

from telegram import ReplyKeyboardMarkup, Update

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    
)

import time 


PAYMENT_PROVIDER_TOKEN = "PAYMENT_PROVIDER_TOKEN"
TOTAL_VOTER_COUNT = 3


# TO CREATE BOT API KEY AND USERNAME QUIKLY SEARCH BOTFATHER ON TELEGRAM AND SET UP A NEW BOT ANS USER NAME . API KEY WOULD BE GIVEN 
# INSERT THIS API KEY INTO THIS SOFTWARE AND RUN


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

GENDER, PHOTO, LOCATION, BIO = range(4)


"""Learn Python Here!"""

TOKEN = 'INSERT BOT API KEY HERE'
BOT_USERNAME = '@INSERT BOT USERNAME HERE'




"""
    $   Telegram bots, which are computer programs that simulate human conversation, can be used for a variety of purposes on the Telegram messaging platform, including:
        Customer service
        Bots can answer queries 24/7, and can be used to solve customer issues.
        Marketing
        Bots can send notifications about promotions, and can be used for automated marketing.
        Automation
        Bots can connect Telegram channels with other apps and services, allowing for the automation of tasks based on triggers and actions. For example, the IFTTT (If This Then That) bot can be used for this purpose.
        Polls
        Bots like VoteBot can be used to create polls that can be shared with friends or published in groups and channels.
"""
"""
    $   An important function of a Telegram bot is the possibility to execute commands in a Telegram chat, 
        which then directly trigger actions or request information. For example, it is possible to send the bot 
        the command “/help” or “/help”,
        which then outputs the commands possible for this bot in the chat as text feedback
"""


"""Displays info on how to use the bot."""
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):


    condition = True
    if condition :
        await update.message.reply_text("Power Magnet Program")

    await update.message.reply_text("""


    use / any of the commands get the Python bot active


    /start -> Python Bot We build We Create We Develop
    /Python -> Welcome to The Power Magnet Program 
    /website -> Join our Master Mind Group on Whatsapp
     

    /hiring -> The Power Magnet Program is Hiring 
    /programmers -> Terms and Conditions
    /real_estate -> real_estate, creators
    /design -> Designers
    
    /games -> code creation activate coding creation games 
    /payment -> Your payment is helping us join the cause and donate
    """
    )



# Define command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #await update.message.reply_text("Hello! Thanks for chatting with Power Magnet Program!")

    await update.message.reply_text(f'Hello {update.effective_user.first_name} Python (235,000) On a global scale, Python is the most searched for programming language to learn.',)

    """Starts the conversation and asks the user about their Program."""
    reply_keyboard = [["/hiring","/website","/help"]]
    

    await update.message.reply_text("Welcome to Power Magnet Program")
    time.sleep(3)
    await update.message.reply_text("The algorithm of programmed thought")
    time.sleep(1)
    await update.message.reply_text("......................PMP.................")
    await update.message.reply_text("You are On The Power Magnet Program")
    await update.message.reply_text("YWelcome to the Power Magnet Program")
    
    
    x = await update.message.reply_text_int(input("Enter Age: ")) ; y = await update.message.reply_text_int(input("Pick a Number: ")) ; L = await update.message.reply_text[0,1,2]
    if (23<x<=3 and 14>y>=2) or (1==1 or 0!=1) or 1 in L:
        await update.message.reply_text("Power Magnet Program")
    else:
        await update.message.reply_text("THE Power Magnet Program")

    await update.message.reply_text("Welcome to Power Magnet Program")
    time.sleep(1)
    await update.message.reply_text(
        """
        Hi! I am Python Hiring Bot. Power Magnet Program Bot. \n\n
        Python Hiring Bot \n\n
        Python Hiring Bot fulfill an important integration role in the Hiring of staffs with a long life expectancy\n\n
        We build We Create We Develop \n\n


        
        """,reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="The Power Magnet Program"
        ),
    )

 
















async def hiring_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["/programmers", "/design", "/real_estate,", "/webdevelopment","/hiring","/website","/help"]]
    

    # TO CALCULATE TEMPERATURE IN FAHRENHEIT
    await update.message.reply_text("Let's take a second to calculate celsius Temperature and convert to fahrenheit")
    inp = await update.message.reply_text.input("Enter celsius Temperature: ")
    cel = float(inp)
    fahr = ( cel * 9.0 ) / 5.0 + 32.0 
    await update.message.reply_text("You put in ",inp, "which is converted to :", fahr)



    var1 = 4
    while var1 > 0:
        await update.message.reply_text("Round up",var1)
        var1 = var1 - 1
        await update.message.reply_text("Power Magnet Program")

    

    # await about bot text
    await update.message.reply_text("""
    Hurry Hurry Hurry
    Apply Now !!

    Python Hiring Bot Hiring
    1. Designers
    2. Programmers
    3. real_estate
    4. Creators
    5. Webdevelopers

    

    Python Hiring Bot

    WE BUILD WE CREATE WE DEVELOP

    www.powermagnetprogram.wordpress.com
    """,reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="The Power Magnet Program"
        ),
    )





async def programmers_command(update, Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["/jnr","/snr","/hiring","/website","/help"]]

    # await about bot text
    await update.message.reply_text("""

    Terms and Condintion

   

        Requirement

    1. Python Hiring Bot is designed to tutor developers skills 0 - 100\n\n
    2. It was formed to make your programming experience as seamless as possible\n\n
    3. Python Hiring Bot is designed to make payment to developers on completion of task \n\n
    4. The python bot cost 20,500 Nigerian Naira fee jnr \n\n
    5. Python Hiring Bot wants you to learn programming \n\n
    6. The Python bot receives your money as an assurance to your wiliness to learn\n\n
     

        Requirement\n\n
    1. The python is designed to tutor snr developers from skills 0 - 100\n\n
    2. It was formed to make your programming experience as seamless as possible\n\n
    3. The python bot is designed to make payment to developers on completion of task \n\n
    4. The python bot cost 20,500 Nigerian Naira fee for snr \n\n
    5. The Python bot wants you to Master programming \n\n
    6. The Python bot receives your money as an assurance to your wiliness to learn\n\n
        

    This is a very exclusive private membership only program. For People who want more out of life. 
    Who want success and its a program that is designed to help you achieve your goals and Dreams Faster than you could imagine .
    Now This program was formed by myself and associates , They are very Famous in there Respective fields. we decided to form the program to help the 
    average person to achieve their Dreams. And if you want to Become Successful you have to follow the Recipe. You have to do what successful
    people have Done. All ultra successful people are a member of some club or Association or Program . Most people Dont know that.

    why would people join this program , Well the Reason People join this program is because of two things 
    1. The information you get from other members . You have access to other members and members pledge to help other members first. 
    Think about this it is not just what you know but who you know ,
    And that is a huge advantage of all super successful people . 

    The second thing all ultra successful people have is that they have a cash cow , They have some type of printing press. 
    All super successful people are members of some club or program or Association 
    And they own some cash cow And thats why the Power Magnet Program was Formed. 
    Because up until now what program could you join. This Advantages are always held for the privileged elite class up until now . 
    And that is why the Power Magnet Program was formed . 
    It was formed so that anybody who has goals and dreams and wants to make them come true faster can join our program. if you have are invited , 
    Its  By invitation only And have access to some of the same information
    that the ultra wealth privileged elite class has had Exclusive access to for years .
    And this is your opportunity to Join our Program. Let me tell you want you get . The first thing you get is what we call success mastery course . 
    Then you join the Power Magnet Program . The first thing you get is the 
    online success Mastery Course its 28 hours of Tracing . Plus written material But its online course . 
    The Third member Benefit you get is as a member you get to go absolutely free to all the workshop seminars , 
    retrieves amd week end events that the Power Magnet Program puts on 

    This live Events are free to members Next to the last Benefits you get as a member is you get access to other members the contacts the association. 
    The networking opportunists Remember its not just what you know but who you know ,
    its not just what you know But Who you know . A Master mind Group is one of the most important keys to success 

    This Python is Bot is Created Using the Python Programming language. 
    This Python Bot is Designed By The Power Magnet Program PMP 
    This Python Bot is Sponsored By The Algorithm of Programmed Thought 
    For partnership contact call or Whatsapp 07054015789 to own a bot As This And to Partners with The Developers of the Project
    signed. Power Magnet Program PMP The Algorithm of Programmed Thought .     
    WE BUILD WE CREATE WE DEVELOP
    
    www.powermagnetprogram.wordpress.com
    """,reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="The Power Magnet Program"
        ),
    )


# This Python Bot is designed to make your Python Programming exercise as seamless as possible




async def website_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    reply_keyboard = [["https://www.powermagnetprogram.wordpress.com","https://www.07054015789whatsapp.com","/hiring","/website","/help"]]
    
    await update.message.reply_text("""
    Login to The Power Magnet Program or 
    Simple Book bot on whatsapp           

    The python Bot WE BUILD WE CREATE WE DEVELOP1                         
    """,reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="The Power Magnet Program"
        ),
    )


# Payment gateway whatever that is should work for a means for accepting payment on encryption form 
# Payment using python javascript java payment gateway 
# Payment gateway One way in and one in 
# Payment gateway provided the tab is closed autatication cancel
# Payment gateway rates accordance to country policy 
# Payment gateway payment is translated into the crypto equivalent 
# Payment gateway stores crypto equivalent 
# Payment converts payment to money currency pending on country policy 
# Payment if illegal returns to purchaser main account on 48hrs 
# payment if reported return to purchaser main account on 48hrs 
# Payment if robust takes 1 week to deliver 
# Payment Gateway................
#
#
#







async def payment_gateway(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    reply_keyboard = [["/gtb","/opay","/hiring","/website","/help"]]
    
    await update.message.reply_text("""
    Your donations today will help fund the transition of this new program\n
    This upgrade is crucial for us to continue efficiently delivering vital social services\n
    in our community. Please give generously so that we can better serve those in need for many years to come                                
    """,reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="The Power Magnet Program"
        ),
    )









async def gtb_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    account = ["0266251683 Mcdonald Daso Harry","/hiring","/website","/help"]
    await context.bot.send_poll(
        update.effective_chat.id,
        "Your Donation is Helping us",
        account,
        is_anonymous=False,
        allows_multiple_answers=True
    )
    







async def opay_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    account = ["7054015789 Mcdonald Daso Harry","/hiring","/website","/help"]
    await context.bot.send_poll(
        update.effective_chat.id,
        "Your Donation is Helping us",
        account,
        is_anonymous=False,
        allows_multiple_answers=True,
        input_field_placeholder="The Power Magnet Program"
    )




async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["/hiring","/website","/help"]]
    await update.message.reply_text("""
    visit the help command , thank you for logging on the power magnet program bot                                
    """,reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="The Power Magnet Program"
        ),
    )



def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("INSERT BOT API KEY HERE").build()
    
    print('Power Magnet Program bot hiring ...')
    print("The Algorithm of Programmed Thought..........")
    print("Python Bot WE BUILD WE CREATE WE DEVELOP")
    
    # Matrix of random numbers 


  
    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler('error',error_handler))
    #application.add_handler(CommandHandler('Python', Python_command))
    application.add_handler(CommandHandler("website",website_command))
    application.add_handler(CommandHandler("payment",payment_gateway))
    application.add_handler(CommandHandler("gtb",gtb_command))
    application.add_handler(CommandHandler("opay",opay_command))
    application.add_handler(CommandHandler("hiring",hiring_command))
    application.add_handler(CommandHandler("programmers",programmers_command))
   



    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
