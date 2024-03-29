import time
import boto3
from datetime import datetime, timedelta, timezone
from scrap import obtener_variantes
from decimal import Decimal

def armar_canasta(variantes):
    canasta = {}
    productos = set([variante["producto"] for variante in variantes])
    for producto in productos:
        variantes_producto = [variante for variante in variantes if variante["producto"] == producto]
        canasta[producto] = Decimal(str(round(sum([variante["precio"] for variante in variantes_producto]) / len(variantes_producto), 2)))
    return canasta

def armar_date_str():
    utc_now = datetime.utcnow()
    utc_offset = timedelta(hours=-3)
    date = utc_now.replace(tzinfo=timezone.utc) + utc_offset
    return time.strftime("%Y/%m/%d")

def lambda_call(event, context):
    variantes, total = obtener_variantes()
    date_str = armar_date_str()
    print(date_str)
    canasta = armar_canasta(variantes)
    dynamodb = boto3.resource('dynamodb', region_name='sa-east-1')
    table = dynamodb.Table("variacion_canasta")
    table.put_item(
        Item={
            "id": date_str,
            'date': date_str,
            'total': Decimal(str(total)),
            'canasta': canasta
        }
    )


if __name__ == "__main__":
    lambda_call(None, None)
