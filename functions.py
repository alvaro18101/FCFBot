# /start
welcome = ''
with open('files/welcome.txt', 'r', encoding='utf8') as file:
    welcome = file.read()

# /help
help = ''
with open('files/help.txt', 'r', encoding='utf8') as file:
    help = file.read()

import numpy as np
import pandas as pd
# import schedule

# ------------------------------------------------
# /freeroom: Muestra las aulas desocupadas
# ------------------------------------------------
# Código para ordenar la data y obtener las aulas con sus horarios (días y horas) ocupados
path = './files/Bot Telegram - Database General.csv'
df = pd.read_csv(path, header=None)
df_modified = df
header = ['','Plan', 'Semestre', 'Tipo', 'Código', 'Asignatura', 'Sección', 'Tope', 'Aula', 'Docente', 'N° de horas',
          'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
df_modified.columns = header
df_modified = df_modified.drop([''], axis=1)
df_modified = df_modified.drop([0,1], axis=0)
df_modified.index = range(len(df_modified))
# df_string = str(df_modified.iloc[:,[1,4,]])


# Código para determinar las horas libres de cada aula


# Código para obtener la fecha y hora del momento en que se ingresa el comando


# Código para seleccionar las aulas que están libres ese día --> devuelve una lista

# Código para armar la respuesta del bot
freerooms = [113, 153, 214] #Lista que tendrá todas las aulas libres por lo menos 1 hora
rspta1 = ''
for i in freerooms:
    rspta1 += 'Aula ' + str(i) + ', piso ' + str(i)[0] + '\n'
rspta1 = 'Aulas libres ahora:\n' + rspta1




