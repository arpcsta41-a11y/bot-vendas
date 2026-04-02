import telebot
import time
import random
import threading

# 🔑 COLOQUE SEU TOKEN AQUI
TOKEN = "7906689791:AAHOERU_82iJA7szifzos9HMTpwAoGlr9fk"

bot = telebot.TeleBot(TOKEN)

print("🔥 Bot de vendas iniciado...")

# 🛍️ PRODUTOS
produtos = [
    {"nome": "🎧 Fone Bluetooth TWS", "preco": "🔥 Promoção hoje", "link": "https://amzn.to/4toBHwR"},
    {"nome": "⌚ Smartwatch D20 Fitness", "preco": "💰 A partir de R$49", "link": "https://s.shopee.com.br/1gELJepKf4"},
    {"nome": "🔊 Mini Caixa de Som Bluetooth", "preco": "🔥 Desconto ativo", "link": "https://s.shopee.com.br/1qXlWFhQWB"},
    {"nome": "📱 Suporte Veicular", "preco": "💰 Barato e útil", "link": "https://s.shopee.com.br/1qXlWFhQWB"},
    {"nome": "🔌 Carregador Turbo USB", "preco": "⚡ Carregamento rápido", "link": "https://s.shopee.com.br/1LbUvcbvCS"}
]

# 👇 SEU ID FIXO (IMPORTANTE)
CHAT_ID = 8324676205

# 🚀 START
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "🚀 Bem-vindo!\nVocê vai receber ofertas automaticamente 💰🔥"
    )

# 🔥 PROMO
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

# 🔄 LOOP AUTOMÁTICO (CORRIGIDO)
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

            bot.send_message(CHAT_ID, mensagem)  # ✅ CORRETO

            print("✅ Produto enviado!")
            time.sleep(30)

        except Exception as e:
            print("❌ Erro:", e)

# 🚀 INICIA LOOP
threading.Thread(target=loop_vendas).start()

# 🤖 BOT ONLINE
bot.infinity_polling()
