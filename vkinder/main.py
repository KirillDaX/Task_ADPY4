# -*- coding: utf-8 -*-
import function_module
import config
import db_module

""" Описание:

запись происходит в файл result.json"""


if __name__ == '__main__':
    # ===  RUN ===
    # полукчение данных
    common_data = function_module.get_common_friends(config.target_id,
                                                     function_module.search_module(config.count_find))
    common_groups_dct = function_module.common_groups(config.target_id, common_data)
    # --------нормализация данных ------------
    function_module.update_data_groups_info(common_data, common_groups_dct)
    # проверка интересов и прочего
    function_module.get_common_interests(config.target_id, common_data)
    # function_module.get_common_music(config.target_id, common_data)
    # ----------------------------------
    function_module.prepare_to_db(common_data)  # переобразование данных в конечный вид
    # добавление всего в базу
    for item in common_data:
        db_module.add_in_db(db_module.vk_collection, item)

    db_module.sort_rating_and_write_to_json_file()  # соритровка по рейтнигу  и внесение в JSON 10 топовых
