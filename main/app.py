from fastapi import FastAPI
from scraper import scrape

app = FastAPI()
url = "https://nigerianprice.com/prices-of-commodities-in-nigeria/"


@app.get("/prices")
def prices():
    prices = scrape(url=url)
    res = {}
    for p, v in prices.items():
        ps = []
        for d in v:
            t = d.split(" == ")
            if len(t) == 1:
                continue
            else:
                ps.append(int(t[1].replace("N", '').replace(",",'').replace(' – ', '')))

        res[p] = round(sum(ps) / len(ps), 2)
    return res