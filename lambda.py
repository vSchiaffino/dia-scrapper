from datetime import datetime, timedelta, timezone
from scrap import obtener_variantes

def armar_canasta(variantes):
    canasta = {}
    productos = set([variante["producto"] for variante in variantes])
    for producto in productos:
        variantes_producto = [variante for variante in variantes if variante["producto"] == producto]
        canasta[producto] = round(sum([variante["precio"] for variante in variantes_producto]) / len(variantes_producto), 2)
    return canasta

def armar_date_str():
    utc_now = datetime.utcnow()
    utc_offset = timedelta(hours=-3)
    date = utc_now.replace(tzinfo=timezone.utc) + utc_offset
    date_str = time.strftime("%Y/%m/%d")

def lambda_call(event, context):
    variantes, total = obtener_variantes()
    date_str = armar_date_str()
    canasta = armar_canasta(variantes)
    dynamodb = boto3.resource('dynamodb', region_name='sa-east-1')
    table = dynamodb.Table("cotizaciones_cedears")
    table.put_item(
        Item={
            'date': date_str,
            'total': total,
            'canasta': canasta
        }
    )


if __name__ == "__main__":
    lambda_call(None, None)