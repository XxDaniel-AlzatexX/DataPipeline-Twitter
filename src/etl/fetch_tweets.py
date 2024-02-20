import os
import asyncio
from dotenv import load_dotenv

from twscrape import API, gather

async def fetch_tweets(api, query, limit=100):
    # Esta función asincrónica extrae tweets usando la API de twscrape.
    tweets = await gather(api.search(query, limit=limit))
    return tweets

async def main():
    load_dotenv()  # Carga las variables de entorno desde un archivo .env

    # Estas líneas obtienen las credenciales de X desde las variables de entorno
    username = os.getenv('X_USERNAME')
    password = os.getenv('X_PASSWORD')
    email = os.getenv('X_EMAIL')
    email_password = os.getenv('X_EMAIL_PASSWORD')

    # Inicializa y configura la API de twscrape con las credenciales de usuario
    api = API()
    await api.pool.add_account(username, password, email, email_password)
    await api.pool.login_all()

    # Términos de búsqueda para políticos latinoamericanos
    politicians = ['Gustavo Petro', 'Nayib Bukele', 'Javier Milei']

    # Búsqueda de tweets para cada político
    for politician in politicians:
        tweets = await fetch_tweets(api, politician, limit=100)

        # Imprime los tweets para el político actual
        print(f"Tweets para {politician}:\n")
        for tweet in tweets:
            print(f"{tweet.id}\t{tweet.rawContent}\n")
        print("\n" + "="*100 + "\n")  # Separador entre políticos

if __name__ == "__main__":
    asyncio.run(main())
