import unittest
import main
import config


class TestYandexTranslate(unittest.TestCase):

    def test_code(self):
        """проверям получение ответов от API"""
        self.answer = main.translate_it(config.output_file)['code']
        self.assertEqual(self.answer, 200, 'не получен положительный ответ от API')
        self.assertNotEqual(self.answer, 501, 'Заданное направление перевода не поддерживается')
        self.assertNotEqual(self.answer, 404, 'Превышено суточное ограничение на объем переведенного текста')

    def test_text(self):
        """тест правильности перевода слова 'привет' """
        self.answer = main.translate_it(config.output_file)['text']
        self.equal_data = ['Hi']
        self.assertEqual(self.answer, self.equal_data, 'проблемы с переводом')
        self.assertIsNot(self.answer, self.equal_data, 'один и тот же объект')

    def test_answer_is_not_empty(self):
        """тест наличия ответа"""
        self.answer = main.translate_it(config.output_file)
        self.assertIsNotNone(self.answer)

    def test_api_key(self):
        """проверям что мы не получаем коды  проблем с API-ключами"""
        self.answer = main.translate_it(config.output_file)['code']
        self.assertNotEqual(self.answer, 401, 'не верный ключ API')
        self.assertNotEqual(self.answer, 402, 'API-ключ заблокирован')


if __name__ == '__main__':
    unittest.main()
