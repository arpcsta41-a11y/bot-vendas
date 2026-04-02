import telebot
import time
import random
import threading

# 🔑 COLOQUE SEU TOKEN AQUI
TOKEN = "8732867210:AAEzW7NVhlxmf61vmwAxXo7F4UfR6aOtZ6g"

bot = telebot.TeleBot(TOKEN)

print("🔥 Bot de vendas iniciado...")

# 🛍️ PRODUTOS COM LINKS REAIS (EXEMPLO)
produtos = [
    {
        "nome": "🎧 Fone Bluetooth TWS",
        "preco": "🔥 Promoção hoje",
        "link": "https://amzn.to/4toBHwR"
    },
    {
        "nome": "⌚ Smartwatch D20 Fitness",
        "preco": "💰 A partir de R$49",
        "link": "https://s.shopee.com.br/1gELJepKf4"
    },
    {
        "nome": "🔊 Mini Caixa de Som Bluetooth",
        "preco": "🔥 Desconto ativo",
        "link": "https://s.shopee.com.br/1qXlWFhQWB"
    },
    {
        "nome": "📱 Suporte Veicular para Celular",
        "preco": "💰 Barato e útil",
        "link": "https://s.shopee.com.br/1qXlWFhQWB"
    },
    {
        "nome": "🔌 Carregador Turbo USB",
        "preco": "⚡ Carregamento rápido",
        "link": "https://s.shopee.com.br/1LbUvcbvCS"
    }
]

# 🚀 COMANDO START
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "🚀 Bem-vindo!\nVocê vai receber ofertas automaticamente 💰🔥"
    )

# 🔥 COMANDO PROMO
@bot.message_handler(commands=['promo'])
def promo(msg):
    produto = random.choice(produtos)

    mensagem = f"""
🔥 OFERTA IMPERDÍVEL!

🛍️ {produto['nome']}
💰 {produto['preco']}

⚡ Corre antes que acabe!
👉 {produto['link']}
"""

    bot.send_message(msg.chat.id, mensagem)

# 🧪 TESTE
@bot.message_handler(commands=['teste'])
def teste(msg):
    bot.send_message(msg.chat.id, "✅ Bot funcionando perfeitamente!")

# 🔄 LOOP AUTOMÁTICO
def loop_vendas():
    while True:
        try:
            produto = random.choice(produtos)

            mensagem = f"""
🚨 PROMOÇÃO RELÂMPAGO!

🛍️ {produto['nome']}
💰 {produto['preco']}

⏳ Estoque limitado!
👉 {produto['link']}
"""

            bot.send_message(msg.chat.id, mensagem)

            print("✅ Produto enviado!")
            time.sleep(30)  # ⏱️ 30 segundos (TESTE)

        except Exception as e:
            print("❌ Erro:", e)

# 🚀 INICIA LOOP
threading.Thread(target=loop_vendas).start()

# 🤖 BOT ONLINE
bot.infinity_polling()
