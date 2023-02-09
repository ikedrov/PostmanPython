'''
1. Отправить метод POST

2. Создать текстовый файл в котором хранить 5 шт place_id полученных из 1 пункта (не писать портянку вызывая 5 раз метод, сделать красиво)

3. Отправить метод Get который будет читать place_id из текстового файла (из него, не их переменной первого запроса) и убедиться что данные place_id существуют
'''

import requests


class NewLocation:

    def create_new_location(self):

        for i in range(5):
            with open('5_9.txt', 'a+') as file:
                base_url = 'https://rahulshettyacademy.com'
                key = '?key=qaclick123'
                post_resource = '/maps/api/place/add/json'
                post_url = base_url + post_resource + key
                json_to_create_new_location = {
                    "location": {
                        "lat": -38.383494,
                        "lng": 33.427362
                    }, "accuracy": 50,
                    "name": "Frontline house",
                    "phone_number": "(+91) 983 893 3937",
                    "address": "29, side layout, cohen 09",
                    "types": [
                        "shoe park",
                        "shop"
                    ],
                    "website": "http://google.com",
                    "language": "French-IN"
                }

                post_result = requests.post(post_url, json=json_to_create_new_location)
                print(post_result.text)

                print(f'Post status code: {str(post_result.status_code)}')
                assert post_result.status_code == 200
                print('Post status code ok')

                post_check = post_result.json()
                post_check_value = post_check.get('status')
                print(f'Post status code value: {post_check_value}')
                assert post_check_value == 'OK'
                print('Post status value is correct')

                place_id = post_check.get('place_id')
                file.writelines(f'{place_id}\n')

        with open('5_9.txt', 'r') as f:
            for line in f:
                get_resource = '/maps/api/place/get/json'
                get_url = base_url + get_resource + key + '&place_id=' + line.rstrip()
                get_result = requests.get(get_url)
                print(get_result.text)

                print(f'Get status code: {str(get_result.status_code)}')
                assert get_result.status_code == 200
                print('Get status code ok')


new_place = NewLocation()
new_place.create_new_location()