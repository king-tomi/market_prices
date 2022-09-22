from decimal import Decimal
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from scraper import scrape
from decimal import Decimal
from typing import Any, Union

from googlesearch import search

app = FastAPI()
url = "https://nigerianprice.com/prices-of-commodities-in-nigeria/"


class Product(BaseModel):
    name: str
    price: Decimal
    image: Union[Any,None] = None



@app.get("/prices")
def prices():
    prices = scrape(url=url)
    res = {}
    for p, v in prices.items():
        temp = []
        for d in v:
            t = d.split(" == ")
            if len(t) == 1:
                continue
            else:
                name = t[0]
                price = t[1].replace("N", '').replace(",",'')
                temp.append(Product(name=name, price=price))
        res[p] = temp
    return res