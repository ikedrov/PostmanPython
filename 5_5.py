'''
1.Запросить у пользователя категорию, на которую он хочет получить шутку (не сами сохранить в переменную, а через input() и ввести в терминале

2.Отправить запрос для получения всех категорий

3.убедиться что данная категория (из пункта 1) есть в ответе запроса (отправленного в пункте 2)

4.Отправить запрос для получения шутки, которую запросил пользователь
'''

import requests


class JokeCategories:

    def __int__(self):
        pass

    def get_new_category_joke(self, cat):
        category_url = 'https://api.chucknorris.io/jokes/categories'
        categories = requests.get(category_url)
        categories_list = categories.text.replace('["', '').replace('"]', '').split('","')

        if cat in categories_list:
            url = f'https://api.chucknorris.io/jokes/random?category={cat}'
            print(url)
            result = requests.get(url)
            print(f'Статус код: {str(result.status_code)}')
            assert result.status_code == 200
            print('Status code ok')
            result.encoding = 'utf-8'
            print(result.text)
            check = result.json()
            check_cat = check.get('categories')
            assert check_cat == [cat]
            print('Category ok')
            check_chuck = check.get('value')
            assert 'Chuck' in check_chuck
            print('This joke is about Chuck Norris')
        else:
            print(f'Category is not in the list. Select category from: {categories_list}')


user_category = input('Input category, if you want to stop type "q": ')
while user_category != 'q':
    joke = JokeCategories()
    joke.get_new_category_joke(user_category)
    user_category = input('Input category, if you want to stop type "q": ')
