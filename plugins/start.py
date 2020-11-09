from pyrogram import Client, filters, emoji


@Client.on_message(filters.command("start"))
def start_command(c, msg):
    c.send_message(
        msg.chat.id,
        '{fleur} Welcome <a href="tg://user?id={id}">{name}</a>!\n'
        "\n"
        "{orange_diamond} With this bot you can generate a random identity based on fake-it API.\n"
        "\n"
        '{tech} <a href="t.me/GodSaveTheBots">Stay Updated</a>'.format(
            id=msg.from_user.id,
            name=msg.from_user.first_name,
            fleur=emoji.FLEUR_DE_LIS,
            orange_diamond=emoji.SMALL_ORANGE_DIAMOND,
            tech=emoji.MAN_TECHNOLOGIST_LIGHT_SKIN_TONE,
        ),
        disable_web_page_preview=True,
    )
