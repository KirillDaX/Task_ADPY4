import requests
import config


def translate_it(output_file):
    """переводит слово 'привет' с русского на английский"""
    response = requests.get(config.URL, params=config.params)
    json_data = response.json()

    with open(output_file, 'w') as f:
        f.write(str(json_data['text']))

    return json_data


translate_it(config.output_file)
