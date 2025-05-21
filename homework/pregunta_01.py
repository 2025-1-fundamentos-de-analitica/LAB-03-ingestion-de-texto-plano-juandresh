"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01():
    
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.

    """

    with open('files/input/clusters_report.txt','r') as datos:
        count = 0

        columnas = []
        clusterData = []
        cantPalData = []
        porPalData = []
        princPalData = []

        palabras = []

        for line in datos:
            
            i = line.strip()

            if re.search(r'\s{2,}', i):
                res = re.split(r'\s{2,}', i)
            elif re.search(r'-{2,}', i):
                res = re.split(r'-{2,}', i)
            else:
                res = [i]

            if any(elem.strip() != '' for elem in res):
                # print(res)
                count += 1

                if count == 1:
                    for dato in res:
                        columnas.append(dato)
                elif count == 2:
                    columnas[1] = columnas[1]+' '+res[0]
                    columnas[2] = columnas[2]+' '+res[1]

                elif re.search(r'^\s*(1[0-3]|[1-9])\b',res[0]):
                    if len(palabras) != 0:
                        princPalData.append(' '.join(palabras))
                        palabras = []
                    clusterData.append(res[0])
                    cantPalData.append(res[1])
                    porPalData.append(res[2])
                    palabras.append(' '.join(res[3::]))

                else:
                    palabras.append(' '.join(res))

        princPalData.append(' '.join(palabras))

        columnas = [i.lower().replace(' ', '_') for i in columnas]
        clusterData = map(int,clusterData)
        cantPalData = map(int,cantPalData)
        porPalData = [float(i.split(' ')[0].replace(',','.')) for i in porPalData]
        princPalData = [i.rstrip('.') for i in princPalData]

        data = dict(zip(columnas, [clusterData,cantPalData,porPalData,princPalData]))

        df = pd.DataFrame(data)

        return df
    
result = pregunta_01()

# print(result.principales_palabras_clave.to_list()[0])

