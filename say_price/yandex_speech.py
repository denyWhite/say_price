import requests
import translit

"""
 ermil
"""

token = "CggaATEVAgAAABKABJ__b9x8jOjsQGvgCTNeKLPZ_RAIOuj4kOahz0Iek7JAu7VV_p1-0cybLJ6gjFmo-5L87aU6K5rsibXnpfDuwkDW4LTQZ3k_epmfSDf8WOZ8YrFlP65rRunPDU56zPj6FquVWfHVZBtlN8pOCLLFh_RdBLd3h0AT5gL0vX5Vgu3hN2a0jI-70Ge8laH4vV5Z38wWaNkEN46L5ur0_U993aqHdCVSCN-g6JRo_u9vb5JdowepXpVZd9jXJJpwMtV_K33GN-MgnW4NmcxUoX70x9OW3j1sWvvA-iVi9IdbaJ-fkVFIxsaBCTU5_waR6vRxjKoowZy-NMk732zr1mZl3M0LYGWXB_npzHjqjusxon2wq0Nk6fGZify7Vz-VQTnHXzKU4dt9QFxWOU4uyKwnsmXHIYvfQvJurzEE4yKuTQFaghEnKfFpk8yx6drLi5Zs_QqO4alwmL7RAR8KGNOw_2OHvuXnJuPhSFu9PSt7E7tYOKXrhZWhsec-1g825T9bAmvXhNFtWVOw10J3CSkHXLV87xTgrHbrBtYaUhNFkb00noqyRZyuI2EccEvFHxmuCinhgFLAu2jjhrKcDZE3_udmRmlc7Yx5bF55f0GXn3yhVi_GGcirreM0UfyDvCbz0mguuAnnUI-f6bS8cWT0urZbTByh_Mzow9GsECZAcz3LGmMKIDc3ZjA5NDIzOGVhNzQyOTE5YmUxOWIwYTI0MzhkMjczEJah_uoFGNbygOsFIiEKFGFqZXM1dW1ucDBtampyNmhvczhvEglkZW4tYmVsb3ZaADACOAFKCBoBMRUCAAAAUAEg8gQ"
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