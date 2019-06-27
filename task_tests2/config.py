
API_KEY = ''  # ключи тут: https://yandex.ru/dev/translate/doc/dg/concepts/api-keys-docpage/
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

full_text = 'Привет'

params = {
        'key': API_KEY,
        'text': full_text,
        # 'lang': '{}-{}'.format(from_lang, to_lang)
        'lang': 'ru-en'
        }
output_file = 'output_translate.txt'
