from pyrogram import Client, Filters

from FakeIt import allowed_countries, FakeIt

f = FakeIt()


def makereadable(d: dict) -> str:
    result = ""
    for key in d:
        result += "<b>{key}</b>: <code>{value}</code>\n".format(
            key=key,
            value=d[key]
        )
    return result


@Client.on_message(Filters.regex(r"^\/fakeit_[a-z]{2,3}$"))
def fakeit_country(c, msg):
    country = msg.text[8:]
    if country in allowed_countries:
        msg.reply(makereadable(getattr(f, country)()))
    else:
        msg.reply("Country not supported!")
