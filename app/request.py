import requests

class MoneyApiRequest:

    key = "3238aa7baeca420318e80724429e0261"
    url = "https://currate.ru/api/"

    def get_list_currencies(self):
        response = requests.get(
            self.url,
            params={
                "get": "currency_list",
                "key": self.key
            }
        )

        return response.json()
    
    def get_currency_transfer(self, first_currensy, second_currency):
        response = requests.get(
            self.url,
            params={
                "get": "rates",
                "pairs": f"{first_currensy+second_currency},{second_currency+first_currensy}",
                "key": self.key
            }
        )

        return response.json()