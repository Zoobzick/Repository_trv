import requests
import datetime


def splitter(sentence, tag):
    """Выбираем текст из необходимого нам тэга (<tag> TEXT </tag>)"""
    first_split = sentence.split("</" + tag + ">")[0]
    value = float(first_split.split(("<") + tag + ">")[-1].replace(",","."))
    return (value)



def currency_rates(currency_code=""):
    currency_code = str(currency_code)
    currency_code = currency_code.upper()
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = resp.content.decode(encoding=resp.encoding)
    currency_rate = 0
    date = content.split('"')[5]
    date = datetime.datetime.strptime(date, "%d.%m.%Y")
    date = date.date()
    if currency_code in content:
        for el in content.split('<Valute'):
            if currency_code in el:
                if int(splitter(el, "Nominal")) == 1:
                    currency_rate = round(splitter(el, "Value"), 2)
                    return (f"{currency_rate}, {date}")
                else:
                    nominal = splitter(el, "Nominal")
                    value = splitter(el, "Value")
                    currency_rate = round(nominal / value, 2)
                    return (f"{currency_rate}, {date}")
    return None

