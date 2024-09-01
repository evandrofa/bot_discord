import os
from groq import Groq
from api import api_key
import discord
from discord import app_commands

id_do_servidor = #preencher_aqui
#


class client(discord.Client):

    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False  #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:  #Checar se os comandos slash foram sincronizados
            await tree.sync(
                guild=discord.Object(id=id_do_servidor)
            )  # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.")


aclient = client()
tree = app_commands.CommandTree(aclient)

#parte da IA

groq_client = Groq(api_key=api_key)


# Parte da resposta do bot Discord
@tree.command(guild=discord.Object(id=id_do_servidor),
              name='pergunta',
              description='Faça uma pergunta!')
async def slash2(interaction: discord.Interaction, pergunta: str):
    # Cria a resposta com base na pergunta do usuário
    chat_completion = groq_client.chat.completions.create(
        messages=[{
            "role": "system",
            "content": "Você é um jovem que gosta de jogos"
        }, {
            "role": "user",
            "content": pergunta
        }],
        model="llama3-8b-8192")

    # Envia a resposta de volta no Discord
    response = chat_completion.choices[0].message.content
    await interaction.response.send_message(response, ephemeral=False)


aclient.run(
    '') ##colocar o token do bot aki nesta string
