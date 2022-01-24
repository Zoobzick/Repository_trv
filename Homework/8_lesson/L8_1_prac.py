import re


def email_parse(email_adress: str):
    valid_adress = re.compile(r'(?P<Username>[A-Za-z0-9\-]+)@(?P<Domain>[A-Za-z]+\.[a-zA-Z]+)')
    result = valid_adress.finditer(email_adress)
    if valid_adress.match(email_adress):
        for word in result:
            return word.groupdict()
    else:
        raise ValueError("Invalid e-mail address")
