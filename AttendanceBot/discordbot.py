from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
URL = 'https://discord.com/api/webhooks/774702675114983466/ToCCEVBBr6R5deNpixqkSbIFM_Z_VAXeBDqP57c-iYumLVIiucrv9I4-BA-Dj8GqVoI2'
def send_start_details(SUBJECT,NAME):
    webhook = DiscordWebhook(url = URL)
    embed = DiscordEmbed(title ='CLASS DETAILS',color = 3800832,description='Class Successfully Started')
    embed.add_embed_field(name='SUBJECT', value=NAME)
    embed.add_embed_field(name='DATE', value=SUBJECT['date'])
    embed.add_embed_field(name='DAY', value=SUBJECT['day'])
    embed.add_embed_field(name='START TIME:', value=SUBJECT['start'])
    embed.add_embed_field(name='LINK', value=SUBJECT['URL'])
    webhook.add_embed(embed)
    response = webhook.execute()

def send_end_details(SUBJECT,NAME):
    webhook = DiscordWebhook(url=URL)
    embed = DiscordEmbed(title='CLASS DETAILS', color=3801087, description='Class Successfully Ended')
    embed.add_embed_field(name='SUBJECT', value=NAME.upper())
    embed.add_embed_field(name='DATE', value=SUBJECT['date'])
    embed.add_embed_field(name='DAY', value=SUBJECT['day'])
    embed.add_embed_field(name='END TIME', value=SUBJECT['end'])
    embed.add_embed_field(name='LINK', value=SUBJECT['URL'])
    webhook.add_embed(embed)
    response = webhook.execute()

def send_start_error_details(SUBJECT,NAME):
    webhook = DiscordWebhook(url=URL)
    embed = DiscordEmbed(title='CLASS DETAILS', color=3801087, description='ERROR JOINING CLASS!!!!')
    embed.add_embed_field(name='SUBJECT', value=NAME.upper())
    embed.add_embed_field(name='DATE', value=SUBJECT['date'])
    embed.add_embed_field(name='DAY', value=SUBJECT['day'])
    embed.add_embed_field(name='END TIME', value=SUBJECT['end'])
    embed.add_embed_field(name='LINK', value=SUBJECT['URL'])
    webhook.add_embed(embed)
    response = webhook.execute()

def send_end_error_details(SUBJECT,NAME):
    webhook = DiscordWebhook(url=URL)
    embed = DiscordEmbed(title='CLASS DETAILS' , color=3801087, description='ERROR LEAVING CLASS!!!!')
    embed.add_embed_field(name='SUBJECT', value=NAME)
    embed.add_embed_field(name='DATE', value=SUBJECT['date'])
    embed.add_embed_field(name='DAY', value=SUBJECT['day'])
    embed.add_embed_field(name='END TIME:', value=SUBJECT['end'])
    embed.add_embed_field(name='LINK', value=SUBJECT['URL'])
    webhook.add_embed(embed)
    response = webhook.execute()







