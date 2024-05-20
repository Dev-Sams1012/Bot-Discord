import discord
from discord.ext import commands
import asyncio
import random as ra
import time


permissoes = discord.Intents.default()
permissoes.members = True
permissoes.message_content = True

bot = commands.Bot(intents=permissoes, command_prefix=".")


@bot.command(name='oi', help='Lhe cumprimenta e diz qual canal está.')
async def oi(ctx: commands.Context):
    usuario = ctx.author
    canal = ctx.channel
    await ctx.reply(
        f"oi {usuario.display_name}\nVocê está no canal {canal.name}")


@bot.command(name='forca', help='Inicia o jogo da forca.')
async def forca(ctx):

    def aleatorias():
        lista = [
            "banana", "abacaxi", "uva", "laranja", "morango", "maca", "limao",
            "pera", "manga", "melancia", "cenoura", "beterraba", "tomate",
            "cebola", "alface", "pimentao", "couve", "batata", "beterraba",
            "abobora", "computador", "celular", "teclado", "mouse", "monitor",
            "impressora", "tablet", "notebook", "carregador", "fone",
            "cadeira", "mesa", "sofa", "cama", "guarda-roupa", "estante",
            "armario", "rack", "pente", "escova", "shampoo", "condicionador",
            "sabonete", "toalha", "creme", "espelho", "perfume", "sabao",
            "detergente", "escova", "vassoura", "martelo", "serrote",
            "chave de fenda", "chave de boca", "parafuso", "prego", "pregador",
            "alicate", "furadeira", "seringa", "tesoura", "tesoura", "regua",
            "lapis", "caneta", "borracha", "caderno", "livro", "revista",
            "jornal", "copo", "prato", "talheres", "panela", "frigideira",
            "colher", "garfo", "faca", "esponja", "balde", "mangueira",
            "tinta", "pincel", "quadro", "porta", "janela", "telhado",
            "calcada", "portao", "cerca", "grampo", "linha", "agulha", "botao",
            "fivela", "ziper", "corrente", "relogio", "anel", "pulseira",
            "brinco", "colar", "oculos", "bone", "chapeu"
        ]

        aleatorio = ra.choice(lista)

        return aleatorio

    def mostrar_palavra_formatada(palavra, letras_corretas):
        resultado = ""
        for letra in palavra:
            if letra in letras_corretas:
                resultado += letra + " "  # Destaca letras corretas em negrito
                corretas.append(letra)
            else:
                resultado += '- '  # Letras desconhecidas são mostradas como "__" (sublinhadas)
        return resultado.strip()

    palavra = aleatorias()
    letras_corretas = []
    tentativas = 6
    corretas = []

    mensagem = f'**Jogo da Forca**\n\nPalavra: {mostrar_palavra_formatada(palavra, letras_corretas)}\nTentativas restantes: {tentativas}'
    await ctx.send(mensagem)

    while tentativas > 0:
        try:
            mensagem = await bot.wait_for(
                'message',
                check=lambda m: m.author == ctx.author and m.content.isalpha(),
                timeout=60)
            letra = mensagem.content.lower()

            if letra in corretas:
                await ctx.send("Você já escolheu essa letra!")
            elif letra in palavra:
                letras_corretas.append(letra)
                palavra_mostrada = mostrar_palavra_formatada(
                    palavra, letras_corretas)
                mensagem = f'Palavra: {palavra_mostrada}\nTentativas restantes: {tentativas}'
                await ctx.send("Letra correta!")
                await ctx.send(mensagem)
            elif letra not in corretas and letra not in palavra:
                tentativas -= 1
                mensagem = f'Tentativas restantes: {tentativas}'
                await ctx.send("Você errou.")
                await ctx.send(mensagem)

            if "-" not in mostrar_palavra_formatada(palavra, letras_corretas):
                await ctx.send("Parabéns! Você acertou a palavra.")
                break

        except asyncio.TimeoutError:
            await ctx.send('Tempo esgotado. O jogo da forca foi encerrado.')
            return

    if tentativas == 0:
        await ctx.send(f"Perdeu, a palavra era {palavra}.")


@bot.command()
async def enviar_embed(ctx):
    embed = discord.Embed(
        title="Título do Embed",
        description="Descrição do Embed",
        color=discord.Color.from_str("#2B2014"))

    logo_arquivo = discord.File("PyBot.png", filename="PyBot.png")
    embed.set_image(url = "attachment://PyBot.png")

    embed.set_author(name="Samuca :)", url="https://www.instagram.com/samuel.au.ab/")

    await ctx.send(files=[logo_arquivo],embed=embed)


@bot.event
async def membronovo(membro: discord.Member):
    canal = bot.get_channel(1240418803574243358)
    embed = discord.Embed(
        title=f"Seja bem-vindo, {membro.display_name}!!",
        description="Aproveite o servidor!",
        color=discord.Color.from_str("#2B2014"))

    logo_arquivo = discord.File("PyBot.png", filename="PyBot.png")
    embed.set_image(url = "attachment://PyBot.png")

    embed.set_author(name="Samuca :)", url="https://www.instagram.com/samuel.au.ab/")

    await canal.send(files=[logo_arquivo],embed=embed)

@bot.event
async def on_ready():
    print("To pronto.")


bot.run(
    "token aqui")

while True:
    time.sleep(3600)
