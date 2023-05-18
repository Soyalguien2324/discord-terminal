from discord_webhook import DiscordWebhook
url = input('Escribe la url de tu bot')
content = input('¿Que quieres poner')
webhook = DiscordWebhook(url=url, content=content)
response = webhook.execute()
