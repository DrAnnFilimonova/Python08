file_contacts = '\Phone_book.txt'
def ask_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronym = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, patronym, phone_number

def save_to_file(data: tuple, file, mode='a'):
    data_str = ' '.join(map(str, data))
    with open(file, mode, encoding='utf-8') as fd:
        fd.write(f'{data_str}\n')

def read_file(file):
    with open(file_contacts, 'r', encoding='utf-8') as fd:
      lines = fd.readlines()
      headers = ['фамилия', 'имя', 'отчество', 'номер телефона']
      list_contacts = []
      for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))
      return list_contacts

def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'фамилия', '2': 'имя', '3': 'номер телефона'}
    found_contacts = []
    for contact in list_contacts:
        if contact[param_dict[param]] == what:
            found_contacts.append(contact)
    return found_contacts

def ask_search():
    print('Выберите параметр для поиска')
    search_param = input('1 - по фамилии, 2 - по имени, 3 - по номеру телефона: ')
    what = None
    if search_param == '1':
        what = input('Введите фамилию для поиска: ')
    elif search_param == '2':
        what = input('Введите имя для поиска: ')
    elif search_param == '3':
        what = input('Введите номер для поиска: ')
    return search_param, what

def main_menu():
    while True:
        user_action = input('1 - добавить новый контакт,\n2 - найти контакт,\n3 - посмотреть весь справочник,\n4 - выйти\n')
        if user_action == '1':
            save_to_file(ask_user(), file_contacts)
        elif user_action == '2':
            lst_contacts = read_file(file_contacts)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)
        elif user_action == '3':
            print(read_file(file_contacts))
        elif user_action == '4':
            print('Завершение работы. До новых встреч!')
            break

if __name__ == '__main__':
  main_menu()