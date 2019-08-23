import requests
import translit

"""
 ermil
"""

token = ""
words = {'одна', 'восемьдесят', 'пятьдесят', 'пятьсот', 'семь', 'тысяч', 'семнадцать', 'миллионов', 'миллиона', 'триста', 'тысяча', 'десять', 'восемнадцать', 'четырнадцать', 'копейка', 'девятнадцать', 'две', 'тысячи', 'два', 'шестнадцать', 'шестьсот', 'пятнадцать', 'восемьсот', 'двенадцать', 'копейки', 'рубля', 'четыреста', 'тридцать', 'тринадцать', 'одиннадцать', 'рублей', 'девяносто', 'семьсот', 'девять', 'семьдесят', 'один', 'три', 'копеек', 'ноль', 'девятьсот', 'двести', 'сорок', 'сто', 'двадцать', 'восемь', 'шесть', 'рубль', 'шестьдесят', 'четыре', 'миллион', 'пять'}


def synthesize(text):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    fn = translit.translit(text)
    headers = {
        'Authorization': 'Bearer ' + token,
    }

    data = {
        'text': text,
        'lang': 'ru-RU',
        'voice': 'ermil',
        'emotion': 'neutral',
        'format': 'oggopus',
        'folderId': 'b1guj5vdmpu4ksrjfdrm'
    }

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))
        out_file = open("{}.ogg".format(fn), "wb")  # open for [w]riting as [b]inary
        out_file.write(resp.content)
        out_file.close()


if __name__ == "__main__":
    for word in words:
        synthesize(word)
