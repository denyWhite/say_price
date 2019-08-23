import num2text
import translit
import os


# One of list: alyss ermil jane oksana omazh zahar
voice = 'alyss'

# One of list: neutral good
emotion = 'good'

path = 'voices/{}_{}/'.format(voice, emotion)
ext = ".ogg"

def say_price(price):
    files = num2text.decimal2text(price, 2, (('рубль', 'рубля', 'рублей'),'m'),
                                  (('копейка', 'копейки', 'копеек'), 'f')).split()
    files = list(map(lambda x: os.path.abspath(path + translit.translit(x) + ext), files))
    return files


print(say_price('123.80'))