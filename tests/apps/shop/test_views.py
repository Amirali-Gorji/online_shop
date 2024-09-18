import pytest

from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from apps.shop.models import City, CustomUser

pytestmark = pytest.mark.django_db
client = APIClient()


class TestCategoryAPI:
    def test_create_category_api(self):
        url = reverse('create-categories')
        data = {
            'name': 'test_category',
        }
        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        response_data = response.json()
        assert response_data['name'] == 'test_category'
    

    def test_list_category_api(self):
        NUM = 3
        # Create some categories
        for num in range(NUM):
            create_url = reverse('create-categories')
            data = {
                'name': f'test_category_{num}',
            }
            client.post(create_url, data, format='json')

        url = reverse('list-categories')
        
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        response_data = response.json()
        assert len(response_data['results']) == NUM


# class TestAddressAPI:
#     def test_create_address_api(self):
#         url = reverse('create-address')
#         test_user = CustomUser.objects.create(username='test_user', password='123')
#         test_city = City.objects.create(name_fa='تهران', name_en='tehran')
#         data = {
#             'user': test_user.id,
#             'city': test_city.id,
#             'main_avenue': 'سید جمال الدین', 
#             'stree': 'جهان آرا',
#             'other_desc': None
#         }
#         response = client.post(url, data, format='json')

#         assert response.status_code == status.HTTP_201_CREATED
#         response_data = response.json()
#         assert response_data['main_avenue'] == 'سید جمال الدین'
    


