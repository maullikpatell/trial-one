from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
𝐓𝐡𝐢𝐬 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐢𝐬 𝐮𝐬𝐞𝐝 𝐭𝐨 𝐬𝐡𝐨𝐫𝐭 𝐨𝐫 𝐜𝐨𝐧𝐯𝐞𝐫𝐭 𝐥𝐢𝐧𝐤𝐬 𝐟𝐫𝐨𝐦 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐥𝐚𝐬𝐭 𝐩𝐨𝐬𝐭𝐬  
𝐌𝐚𝐤𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐚𝐬 𝐚𝐧 𝐚𝐝𝐦𝐢𝐧 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥  
𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐮𝐬𝐚𝐠𝐞: `/batch [channel id or username]`
𝐄𝐱:`/batch -100xxx`
"""

START_MESSAGE = '''𝐇𝐞𝐥𝐥𝐨, {}
𝐈'𝐦 𝐀𝐓𝐆𝐋𝐈𝐍𝐊𝐒 𝐁𝐨𝐭 𝐭𝐨 𝐒𝐡𝐨𝐫𝐭 𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤𝐬 𝐭𝐨 𝐀𝐓𝐆𝐋𝐈𝐍𝐊𝐒 𝐛𝐲 𝐔𝐬𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐀𝐓𝐆𝐋𝐈𝐍𝐊𝐒 𝐀𝐏𝐈.   
𝐉𝐮𝐬𝐭 𝐒𝐞𝐧𝐝 𝐦𝐞 𝐀𝐧𝐲 𝐏𝐨𝐬𝐭 𝐰𝐢𝐭𝐡 𝐀𝐧𝐲 𝐋𝐢𝐧𝐤𝐬. 𝐈 𝐰𝐢𝐥𝐥 𝐒𝐡𝐨𝐫𝐭 𝐓𝐡𝐨𝐬𝐞 𝐋𝐢𝐧𝐤𝐬 𝐔𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐀𝐏𝐈 𝐚𝐧𝐝 𝐒𝐞𝐧𝐝 𝐭𝐡𝐞𝐦 𝐁𝐚𝐜𝐤 𝐓𝐨 𝐘𝐨𝐮. 𝐈 𝐰𝐨𝐫𝐤 𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐭𝐨𝐨.   
𝐇𝐢𝐭 𝐡𝐞𝐥𝐩 𝐛𝐮𝐭𝐭𝐨𝐧 𝐟𝐨𝐫 𝐦𝐨𝐫𝐞 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐛𝐨𝐮𝐭 𝐭𝐡𝐢𝐬 𝐁𝐨𝐭  
𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐞𝐭𝐡𝐨𝐝 𝐒𝐞𝐥𝐞𝐜𝐭𝐞𝐝: **{}**

'''


HELP_MESSAGE = '''
𝐇𝐞𝐲! 𝐌𝐲 𝐧𝐚𝐦𝐞 𝐢𝐬 {𝐟𝐢𝐫𝐬𝐭𝐧𝐚𝐦𝐞}. 𝐈 𝐚𝐦 𝐚 𝐋𝐢𝐧𝐤 𝐀𝐓𝐆𝐋𝐈𝐍𝐊𝐒 𝐒𝐡𝐨𝐫𝐭𝐞𝐧𝐞𝐫 𝐁𝐨𝐭, 
𝐡𝐞𝐫𝐞 𝐭𝐨 𝐦𝐚𝐤𝐞 𝐲𝐨𝐮𝐫 𝐖𝐨𝐫𝐤 𝐄𝐚𝐬𝐲 𝐚𝐧𝐝 𝐇𝐞𝐥𝐩 𝐲𝐨𝐮 𝐭𝐨 𝐄𝐚𝐫𝐧 𝐦𝐨𝐫𝐞 𝐈 𝐡𝐚𝐯𝐞 𝐥𝐨𝐭𝐬 𝐨𝐟 𝐡𝐚𝐧𝐝𝐲 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬, 𝐬𝐮𝐜𝐡 𝐚𝐬   
- 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐜𝐨𝐧𝐯𝐞𝐫𝐭 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 
- 𝐈𝐧𝐜𝐥𝐮𝐝𝐞 𝐝𝐨𝐦𝐚𝐢𝐧𝐬  
- 𝐄𝐱𝐜𝐥𝐮𝐝𝐞 𝐝𝐨𝐦𝐚𝐢𝐧𝐬 
- 𝐇𝐞𝐚𝐝𝐞𝐫 𝐚𝐧𝐝 𝐅𝐨𝐨𝐭𝐞𝐫 𝐓𝐞𝐱𝐭 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 
- 𝐑𝐞𝐩𝐥𝐚𝐜𝐞 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 
- 𝐁𝐚𝐧𝐧𝐞𝐫 𝐈𝐦𝐚𝐠𝐞

𝐇𝐞𝐥𝐩𝐟𝐮𝐥 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬:
- /start: To Check I am Alive Or Dead
- /batch -100xxx: To short or convert all posts of your channel
𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬:
- /shortener_api
- /mdisk_api
- /header
- /footer
- /username
- /banner_image
- /me

𝐈𝐟 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐚𝐧𝐲 𝐪𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐨𝐧 𝐡𝐨𝐰 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞, 
𝐡𝐚𝐯𝐞 𝐚 𝐥𝐨𝐨𝐤 𝐚𝐭 𝐦𝐲 [𝐓𝐮𝐭𝐨𝐫𝐢𝐚𝐥](𝐡𝐭𝐭𝐩𝐬://𝐲𝐨𝐮𝐭𝐮.𝐛𝐞/𝐙𝐍𝐃𝐊𝐙𝐇𝐠𝐍𝐦𝐝𝐠), 
𝐨𝐫 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐭𝐨 {𝐨𝐰𝐧𝐞𝐫}. 
𝐔𝐬𝐞 𝐭𝐡𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐭𝐨 𝐤𝐧𝐨𝐰 𝐦𝐨𝐫𝐞 𝐚𝐛𝐨𝐮𝐭 𝐭𝐡𝐞 𝐬𝐚𝐦𝐞 𝐁𝐞𝐥𝐨𝐰 𝐚𝐫𝐞 𝐬𝐨𝐦𝐞 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐈 𝐩𝐫𝐨𝐯𝐢𝐝𝐞™'''


ABOUT_TEXT = """
**My Details:**

`🤖 Name:` ** {} **
    
`📝 Language:` [Python 3](https://www.python.org/)
`🧰 Framework:` [Pyrogram](https://github.com/pyrogram/pyrogram)
`👨‍💻 Developer:` [Admin](t.me/ATGLinksQuery_Bot)
`📢 Support:` [ATG BOT](https://t.me/ATGLinksQuery_Bot)
"""


METHOD_MESSAGE = """
Current Method: {method}
    
Methods Available:

> `mdlink` - Change all the links of the post to your MDisk account first and then short to ATGLINKS.

> `shortener` - Short all the links of the post to ATGLINKS directly.
To change method, choose it from the following options:

"""

    


CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""


CHANNELS_LIST_MESSAGE = """
List of channels that have access to this Bot:

{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Methods', callback_data=f'method_command'),
        InlineKeyboardButton('Batch', callback_data=f'cbatch_command'),
        
    ],

    [

        InlineKeyboardButton('Admins', callback_data=f'admins_list'),    
    ],

    [
        
        InlineKeyboardButton('Channels', callback_data=f'channels_list'),
        InlineKeyboardButton('Home', callback_data='start_command')
        
    ],


])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Home', callback_data=f'start_command'),
        InlineKeyboardButton('Help', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('Close', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Help', callback_data=f'help_command'),
        InlineKeyboardButton('About', callback_data='about_command')
    ],
        [
        InlineKeyboardButton('Method', callback_data=f'method_command'),
        InlineKeyboardButton('Close', callback_data='delete')
    ],

])

METHOD_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('MDLINK', callback_data=f'change_method#mdlink'),
        InlineKeyboardButton('Shortener', callback_data='change_method#shortener'),
        
    ],
        [
        InlineKeyboardButton('Back', callback_data=f'help_command'),
        InlineKeyboardButton('Close', callback_data='delete')
    ],

])

BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """


- Method: {method}

- API: {shortener_api}

- Mdisk API: {mdisk_api}

- Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


MDISK_API_MESSAGE = """To add or update your Mdisk API, \n`/mdisk_api mdisk_api`
            
Ex: `/mdisk_api oPrFaMs3aPyqiPSt6LJn`
            
Others Mdisk Links will be automatically changed to the API of this Mdisk account

Get your Mdisk API from @VideoToolMoneyTreebot

Current Mdisk API: `{}`"""

SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/shortener_api [api]`
            
Ex: `/shortener_api acccdf4778c9453ea9f193655bde0af2af01cb9e`
Current Shortener API: `{shortener_api}`"""



HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \\n

To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """Reply to the Footer Text You Want

This Text will be added to the bottom of every message caption or text

For adding line break use \\n

To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """Current Username: {username}

Usage: `/username your_username` (without @)

This username will be automatically replaced with other usernames in the post

To remove this username, `/username remove`"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://te.legra.ph/file/15abe2b2e161eebdc1595.jpg`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
