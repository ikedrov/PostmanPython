'''
1. Отправить метод DELETE,  с помощью которого удалить 2-й и 4-й place_id из текстового файла, полученного в результате выполнения предыдущего задания (удалить значит не стереть, это значит что в файле по прежнему 5  значений, но 2-я и 4-я локация не существуют)

2. Отправить метод Get который будет читать place_id из текстового файла, и сделает отбор на существующие и несуществующие локации

3. Создать новый файл и поместить в него 3 существующих локации (place_id), которые были отобраны в результате метода GET
'''

import requests


class NewLocation:

    def create_new_location(self):

        with open('5_10.txt', 'a+') as file:
            for i in range(5):
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

        with open('5_10.txt', 'r') as f:
            for line in f:
                get_resource = '/maps/api/place/get/json'
                get_url = base_url + get_resource + key + '&place_id=' + line.rstrip()
                get_result = requests.get(get_url)
                print(get_result.text)

                print(f'Get status code: {str(get_result.status_code)}')
                assert get_result.status_code == 200
                print('Get status code ok')

        with open('5_10.txt', 'r') as f:
            delete_resource = '/maps/api/place/delete/json'
            delete_url = base_url + delete_resource + key
            counter = 0
            for i in f:
                counter += 1
                if counter == 2 or counter == 4:
                    json_to_delete_new_location = {
                        "place_id": i.rstrip()
                    }

                    delete_result = requests.delete(delete_url, json=json_to_delete_new_location)
                    print(delete_result.text)

                    print(f'Status code: {str(delete_result.status_code)}')
                    assert delete_result.status_code == 200
                    print('Status code is correct')

                    delete_address = delete_result.json()
                    delete_address_value = delete_address.get('status')
                    print(f'Message: {delete_address_value}')
                    assert delete_address_value == 'OK'
                    print('Address is deleted')

            with open('5_10.txt', 'r') as f:
                for j in f:
                    get_resource = '/maps/api/place/get/json'
                    get_url = base_url + get_resource + key + '&place_id=' + j.rstrip()
                    get_result = requests.get(get_url)
                    print(get_result.text)
                    print(f'Get status code: {str(get_result.status_code)}')
                    if get_result.status_code == 200:
                        with open('5_10_1.txt', 'a+') as file:
                            file.writelines(j)


new_place = NewLocation()
new_place.create_new_location()