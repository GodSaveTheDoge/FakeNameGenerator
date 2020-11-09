import logging

import requests
from bs4 import BeautifulSoup

allowed_countries = [
    "ar",
    "am",
    "au",
    "at",
    "bd",
    "be",
    "ba",
    "br",
    "bg",
    "ca",
    "cn",
    "hr",
    "cy",
    "cz",
    "dk",
    "eg",
    "ee",
    "fi",
    "fr",
    "ge",
    "de",
    "gb",
    "gr",
    "hk",
    "hu",
    "is",
    "in",
    "id",
    "ir",
    "il",
    "it",
    "jp",
    "jo",
    "kz",
    "lv",
    "lt",
    "my",
    "mx",
    "md",
    "mn",
    "me",
    "np",
    "nl",
    "nz",
    "ng",
    "no",
    "pe",
    "ph",
    "pl",
    "pt",
    "ro",
    "ru",
    "sa",
    "rs",
    "sg",
    "sk",
    "si",
    "za",
    "kr",
    "es",
    "se",
    "ch",
    "tw",
    "th",
    "tr",
    "us",
    "ug",
    "ua",
    "ve",
    "vn",
]


def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)

    for i in range(2, len(e) - 1, 2):
        de += chr(int(e[i : i + 2], 16) ^ k)

    return de


def getdata(country):
    r = requests.get("https://fake-it.ws/{}".format(country))

    if not r.ok:
        logging.error('Country "{}" is not valid'.format(country))
        return {"Error": "An error occured"}

    soup = BeautifulSoup(r.text, "lxml")

    data = []
    for d in soup.select(".copy span"):
        text = d.text

        if text == "[email\xa0protected]":
            text = decodeEmail(d.findChild("a").get_attribute_list("data-cfemail")[0])
        data.append(text)

    keys = []
    for k in soup.select("th"):
        text = k.text

        if text == "\xa0":
            continue
        if not text:
            continue

        keys.append(text)

    if not len(data) == len(keys):
        logging.error("Data and keys are different lenghts!")
        return {"Error": "An error occured"}

    result = {}
    for i in range(len(keys)):
        result[keys[i]] = data[i]

    return result


class FakeIt:
    def __init__(self):
        for country in allowed_countries:
            setattr(self, country, lambda country=country: getdata(country))
