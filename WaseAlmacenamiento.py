'''
------------------------------------------------------------------------------------------------------------------------------------
CONFIGURACIONES:
'''
from datetime import datetime
import telebot
import argparse
import cv2
API_KEY = 'YOUR_TELEGRAM_BOT_API_KEY'
bot = telebot.TeleBot(API_KEY)

'''
------------------------------------------------------------------------------------------------------------------------------------
FUNCIONES:
'''
def guardarStock(stock):
    fichero = open('stock.csv', 'w')
    for elementos in stock:
        fichero.write(f"{elementos['Id']};{elementos['Cantidad']};\n")
    fichero.close()

def cargarStock(stock):
    fichero = open('stock.csv', 'r')
    datos = fichero.readlines()
    for linea in datos:
        campos = linea.split(';')
        nuevo = {'Id':campos[0],'Cantidad':campos[1]}
        stock.append(nuevo)
    fichero.close

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = str(day)+'_'+month+'_'+str(year)
    return messsage

def copiaSeguridaStock(stock):
    now = datetime.now()
    date = current_date_format(now)
    fichero = open(f'copias de seguridad/CS_stock({date}).csv', 'w')
    for elementos in stock:
        fichero.write(f"{elementos['Id']};{elementos['Cantidad']};\n")
    fichero.close()

def cargarModo(modo):
    fichero = open('modo.csv', 'r')
    datos = fichero.readlines()
    for linea in datos:
        campos = linea.split(';')
        modo[campos[0]] = campos[1]
    fichero.close

def guardarModo(modo,message):
    print(f'Se a cambiado a modo de {modo}')
    bot.reply_to(message,f'modo {modo}')
    fichero = open('modo.csv', 'w')
    if modo == 'stock':
        fichero.write("stock;1;\nproductos;0;\nadmin;0;\n")
    elif modo == 'productos':
        fichero.write("stock;0;\nproductos;1;\nadmin;0;\n")
    elif modo == 'admin':
        fichero.write("stock;0;\nproductos;0;\nadmin;1;\n")
    fichero.close()

def guardarCatalogo(catalogo):
    fichero = open('catalogo.csv', 'w')
    for elementos in catalogo:
        fichero.write(f"{elementos['Id']};{elementos['Nombre']};{elementos['Talla']};\n")
    fichero.close()

def cargarCatalogo(catalogo):
    fichero = open('catalogo.csv', 'r')
    datos = fichero.readlines()
    for linea in datos:
        campos = linea.split(';')
        nuevo = {'Id':campos[0],'Nombre':campos[1],'Talla':campos[2]}
        catalogo.append(nuevo)
    fichero.close   

def editarStock(message):
    stock = []
    cargarStock(stock)
    string = message.text
    campos = string.split(' ')
    if campos[1] != '?':
        for elementos in stock:
            ID = elementos['Id']
            if ID == campos[0]:
                bot.reply_to(message,'then = ' + elementos['Cantidad'])
                elementos['Cantidad'] = int(elementos['Cantidad']) + int(campos[1])
                bot.reply_to(message,'now = ' + str(elementos['Cantidad']))
    elif campos[1] == '?':
        for elementos in stock:
            ID = elementos['Id']
            if ID == campos[0]:
                bot.reply_to(message,elementos['Cantidad'])
                break
    print(stock)
    guardarStock(stock)   

def consultarProductos(message):
    chat_id = 5608085328
    catalogo = []
    cargarCatalogo(catalogo)
    string = message.text
    campos = string.split(' ')
    for elementos in catalogo:
        if elementos['Id'] == campos[0]:
            bot.send_photo(chat_id,photo=open(f'catalogo/{campos[0]}.png', 'rb'))
            bot.reply_to(message,f"{elementos['Nombre']} | {elementos['Talla']}")

'''
------------------------------------------------------------------------------------------------------------------------------------
TELEGRAM:
'''

#START
@bot.message_handler(commands=['start','help'])
def start(message):
    print('bot en marcha')
    bot.reply_to(message,'el bot esta lista para empezar (｡◕‿◕｡)')

#MODOS
@bot.message_handler(commands=['modostock'])
def stock(message):
    guardarModo('stock',message)

@bot.message_handler(commands=['modoproductos'])
def productos(message):
    guardarModo('productos',message)

@bot.message_handler(commands=['modoadmin'])
def admin(message):
    guardarModo('admin',message)

#STOCK
@bot.message_handler(commands=['stock'])
def ImprimirStock(message):
    stock = []
    cargarStock(stock)
    stockString = ''
    for elementos in stock:
        stockString = stockString +'\n'+ elementos['Id']+ '-->' + elementos['Cantidad']
    bot.reply_to(message,stockString)

#ANALISIS DE TEXTO
@bot.message_handler(content_types=['text'],)
def ComandoPrincipal(message):
    modo ={}
    cargarModo(modo)
    if modo['stock'] == '1':
        editarStock(message)
    elif modo['productos'] == '1':
        consultarProductos(message)
    elif modo['admin'] == '1':
        bot.reply_to(message,'modo admin')

'''
------------------------------------------------------------------------------------------------------------------------------------
PRUEBAS:
'''

'''
------------------------------------------------------------------------------------------------------------------------------------
MAIN:
'''
now = datetime.now()
date1 = current_date_format(now)
date2 = date1
if __name__ == '__main__':
    print('bot en marcha')
    bot.infinity_polling()
    print('fin')
    #rutina copia de seguridad --> DIARIA
    now = datetime.now()
    date1 = current_date_format(now)
    if date1 != date2:
        stock = []
        cargarStock(stock)
        copiaSeguridaStock(stock)
        date2 = date1

