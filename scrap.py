import csv
import time
from concurrent.futures import ThreadPoolExecutor

from methods import scrap_dia_kg


def get_variantes():
    file_path = 'variantes.csv'
    variantes = []
    with open(file_path, newline='',  encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            variante = {
                'producto': row['producto'],
                'link': row['link'],
                'metodo': row['metodo']
            }
            variantes.append(variante)
    return variantes


def obtener_precio(variante):
    precio = scrap_dia_kg(variante["link"])
    producto = variante["producto"]
    print(f"Precio para {producto}: {precio}")
    return {'producto': producto, 'precio': precio}


def obtener_variantes():
    variantes = get_variantes()
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        precios = list(executor.map(obtener_precio, variantes))
    end_time = time.time()
    total_time = end_time - start_time
    for variante, precio in zip(variantes, precios):
        variante['precio'] = precio['precio']
    print(f"[{total_time} s]")
    return variantes, round(sum([variante["precio"] for variante in variantes]), 2)


if __name__ == "__main__":
    variantes, suma = obtener_variantes()
    print(f"canasta = {suma}")