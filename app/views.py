from enum import Enum
from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv
from http import HTTPStatus
from app.request import MoneyApiRequest

router = APIRouter()

class Currency(Enum):
    RUB = "рубль"
    USD = "доллар"
    EUR = "евро"
    GBP = "фунт стерлингов"
    JPY = "японская йена"
    RSD = "сербский динар"
    AED = "дирхам"
    AMD = "драм"
    AUD = "автралийский доллар"
    KZT = "тенге"


@cbv(router)
class MoneyView():

    moneyapi = MoneyApiRequest()

    @router.get("/currency/", tags=["Money"])
    def get_list_currency(self):
        response = self.moneyapi.get_list_currencies()

        if str(response.get("status")) != "200":
            status = HTTPStatus(int(response.get("status")))
            raise HTTPException(status_code=status, detail=response.get("message"))

        data = []
        for value in response.get("data"):
            data.append(f"{value[:3]} - {value[3:]}")

        return {"data": data}


    @router.get("/currency/compare/", tags=["Money"])
    def get_currency(self, first: Currency, second: Currency):
        response = self.moneyapi.get_currency_transfer(first.name, second.name)

        if str(response.get("status")) != "200":
            status = HTTPStatus(int(response.get("status")))
            raise HTTPException(status_code=status, detail=response.get("message"))

        return {"data": response.get("data")}
