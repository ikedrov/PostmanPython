import requests


class NewJoke:

    def __int__(self):
        pass

    def create_new_random_joke(self):
        url = 'https://api.chucknorris.io/jokes/random'
        result = requests.get(url)
        print(f'Статус код: {str(result.status_code)}')
        assert result.status_code == 200
        print('Status code ok')
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_cat = check.get('categories')
        assert check_cat == []
        print('Category ok')
        check_chuck = check.get('value')
        assert 'Chuck' in check_chuck
        print('This joke is about Chuck Norris')

    def create_new_random_category_joke(self):
        category = 'spor'
        url = f'https://api.chucknorris.io/jokes/random?category={category}'
        result = requests.get(url)
        print(f'Статус код: {str(result.status_code)}')
        assert result.status_code == 404
        print('Status code ok')
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_cat = check.get('categories')
        assert check_cat == ['sport']
        print('Category ok')


random_joke = NewJoke()
random_joke.create_new_random_joke()

sport_joke = NewJoke()
sport_joke.create_new_random_category_joke()
