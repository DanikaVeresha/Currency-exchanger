import requests


class Course:
    def __init__(self, name, available, available_uah):
        self.name = name
        self.available = available
        self.available_uah = available_uah
        self.privat_course = {}
        self.update_current_course()

    def update_current_course(self):
        response = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").json()
        for item in response:
            self.privat_course[item["ccy"].lower()] = {"buy": float(item["buy"]), "sale": float(item["sale"])}














