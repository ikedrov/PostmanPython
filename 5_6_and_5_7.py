import requests


class NewLocation:

    def create_new_location(self):

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
        print(f'Place ID {place_id}')

        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        get_result = requests.get(get_url)
        print(get_result.text)

        print(f'Get status code: {str(get_result.status_code)}')
        assert get_result.status_code == 200
        print('Get status code ok')

        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        json_to_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        put_result = requests.put(put_url, json=json_to_update_new_location)
        print(put_result.text)

        print(f'Put status code: {str(put_result.status_code)}')
        assert put_result.status_code == 200
        print('Put status code ok')

        put_check = put_result.json()
        put_check_value = put_check.get('msg')
        print(f'Message: {put_check_value}')
        assert put_check_value == 'Address successfully updated'
        print('Put status value is correct')

        get_result = requests.get(get_url)
        print(get_result.text)

        print(f'Status code: {str(get_result.status_code)}')
        assert get_result.status_code == 200
        print('Address successfully updated')

        check_address = get_result.json()
        check_address_value = check_address.get('address')
        print(f'Address: {check_address_value}')
        assert check_address_value == json_to_update_new_location.get('address')
        print('Address is correct')

        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        json_to_delete_new_location = {
            "place_id": place_id
        }

        delete_result = requests.delete(delete_url, json=json_to_delete_new_location)
        print(delete_result.text)

        print(f'Status code: {str(get_result.status_code)}')
        assert get_result.status_code == 200
        print('Status code is correct')

        delete_address = delete_result.json()
        delete_address_value = delete_address.get('status')
        print(f'Message: {delete_address_value}')
        assert delete_address_value == 'OK'
        print('Address is deleted')

        get_result = requests.get(get_url)
        print(get_result.text)
        print(f'Status code: {str(get_result.status_code)}')
        assert get_result.status_code == 404
        print('Address successfully deleted')
        check_msg = get_result.json()
        check_msg_value = check_msg.get('msg')
        print(f'Address: {check_msg_value}')
        assert check_msg_value == "Get operation failed, looks like place_id  doesn't exists"
        print("Address doesn't exist")


new_place = NewLocation()
new_place.create_new_location()