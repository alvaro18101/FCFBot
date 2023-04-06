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
from datetime import datetime

path = './files/Bot Telegram - Database General.csv'
df = pd.read_csv(path, header=None)
df_modified = df
header = ['','Plan', 'Semestre', 'Tipo', 'Código', 'Asignatura', 'Sección', 'Tope', 'Aula', 'Docente', 'N° de horas',
          'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
df_modified.columns = header
df_modified = df_modified.drop([''], axis=1)
df_modified = df_modified.drop([0,1], axis=0)

df_modified = df_modified.replace('?', np.NaN)
aulas_totales = len(df_modified)
df_modified = df_modified.dropna(subset=['Aula'], axis=0)
aulas_definidas = len(df_modified)

# ------------------------------------------------
# /list: Muestra las aulas
# ------------------------------------------------
aulas_fcf = df_modified['Aula']
aulas_fcf = list(aulas_fcf)
aulas_fcf.sort()
aulas_fcf.remove('virtual')
lista_aulas = []
for i in aulas_fcf:
    if not(i in lista_aulas):
        lista_aulas.append(i)

# ------------------------------------------------
# /freeroom: Muestra las aulas desocupadas
# ------------------------------------------------
# Código para ordenar la data y obtener las aulas con sus horarios (días y horas) ocupados
df_modified = df_modified.iloc[:,[7, 10, 11, 12, 13, 14, 15]]


# a = [1,2,3,2]
# a.remove(2)
# a.remove(2)
# print(a)


# Código para determinar las horas libres de cada aula
# for i in df_modified.columns:
#     print(i)

# Código para obtener la fecha y hora del momento en que se ingresa el comando
days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
today = days[datetime.today().weekday()]



# Código para armar la respuesta del bot
freeroom_text = ''
freerooms = [113, 153, 214] #Lista que tendrá todas las aulas libres por lo menos 1 hora
freeroom_aulas = ''
for i in freerooms:
    freeroom_aulas += 'Aula ' + str(i) + ', piso ' + str(i)[0] + '\n'
freeroom_aulas = 'Aulas libres ahora:\n' + freeroom_aulas
freeroom_text = freeroom_text + freeroom_aulas + 'Recuerda que un aula se considera disponible si cuenta con al menos una hora de tiempo libre.\n'
freeroom_obs = 'ADVERTENCIA: Cursos sin aula definida: {}' .format(aulas_totales - aulas_definidas)
freeroom_text += freeroom_obs