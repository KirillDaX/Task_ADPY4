

class Contact:
    def __init__(self, name, surname, phone_number, favorite_contact=False, *args, **kwargs):
        additional_information1 = kwargs
        self.full_str = ''
        for key, value in additional_information1.items():  # версия вывода по тз
            end_str = '    {}: {}\n     '.format(key, value)
            self.full_str = self.full_str + end_str

        self.full_str2 = ''
        for key, value in additional_information1.items():  # версия для записи в словарь
            end_str = '{}: {}'.format(key, value)
            self.full_str2 = self.full_str2 + end_str
        self.name = str(name)
        self.surname = str(surname)
        self.phone_number = str(phone_number)
        self.favorite_contact = favorite_contact
        self.user_info = {}

    def data_contact(self):  # формируем словрь из данных, который и будет заносится в книгу
        self.user_info['Имя'] = self.name
        self.user_info['Фамилия'] = self.surname
        self.user_info['Телефон'] = self.phone_number
        self.user_info['В избранных'] = self.favorite_contact
        self.user_info['Дополнительная информация'] = self.full_str2
        return self.user_info

    def __str__(self):  # версия вывода по заданию
        if not self.favorite_contact:
            fav_cont = 'Нет'
        else:
            fav_cont = 'Да'
        str_for_print_name = ('Имя: {}\n'
                              'Фамилия: {}\n'
                              'Телефон: {}\n'
                              'В избранных: {}\n'
                              'Дополнительная информация:\n'
                              '     {}\n'. format(self.name, self.surname, self.phone_number,
                                                  fav_cont, self.full_str))
        return str_for_print_name


class PhoneBook:
    def __init__(self, name_of_book):
        self.name_phonebook = name_of_book
        self.data_phonebook = {}

    def add_new_contact(self, new_contact):  # добавляем словарь данных контакта в словарь книги
        self.data_phonebook[new_contact] = Contact.data_contact(new_contact)
        return self.data_phonebook

    def __str__(self):
        return str('название книги: {}'.format(self.name_phonebook))

    def output_all_contacts(self):
        for item in self.data_phonebook:
            print(item)

    def delete_contact(self, name_contact_for_del):
        del self.data_phonebook[name_contact_for_del]
        return self.data_phonebook

    def delete_contact_by_number_phone(self, number_phone_for_del):
        for item in self.data_phonebook:
            if item.phone_number == number_phone_for_del:
                del self.data_phonebook[item]
                break  # исходя из текста задания.
        return self.data_phonebook

    def favorite_contacts(self):
        for item in self.data_phonebook:
            if item.favorite_contact:
                print(item)

    def search_contact(self, name_sought, surname_sought):
        for item in self.data_phonebook:
            if item.name == name_sought and item.surname == surname_sought:
                print(item)


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    karl = Contact('Karl', 'White', '+79876543212', True, twitter='@karlwhite', email='karlwhite@karmail.com')
    mark = Contact('Mark', 'Woltgringer', '+465464999', True, wingmsg='mark_greg')

    book1 = PhoneBook('book 1')

    book1.add_new_contact(jhon)
    book1.add_new_contact(karl)
    book1.add_new_contact(mark)

    # print(karl)
    # print(book1)
    # book1.delete_contact(karl)  # + удалить контакт
    # book1.delete_contact_by_number_phone('+465464999') # + удалить по номеру телефона
    # book1.output_all_contacts()  # + вывод всех контактов.
    # book1.favorite_contacts()  # + вывод избранных  контактов
    # book1.search_contact('Mark', 'Woltgringer')  # +  поиск по имени и фамилии
