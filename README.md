# Dia-scrapper

## Idea
Diariamente consulta mediante una lambda function de AWS, una canasta básica de productos. 

Los precios los busca en la web de [dia online](https://diaonline.supermercadosdia.com.ar/), los productos a consultar están definidos en `variantes.csv`. 

Luego de consultarlos, los sube a una tabla de DynamoDB, para su posterior analisis. 

La idea es poder analizar como varían los precios diariamente, semanalmente, mensualmente, etc.

---
