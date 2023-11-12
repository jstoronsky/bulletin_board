from rest_framework.test import APITestCase
from rest_framework import status
from bulletin_board.models import Ad, Comment
from users.models import User
# Create your tests here.


class AdTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_ad(self):
        """
        тест создания объявления
        """
        user = User.objects.create(email='duck@test.com', role='User')
        user.set_password('edcrfvtgb')
        user.save()
        data1 = {
            "email": "duck@test.com",
            "password": "edcrfvtgb"
        }
        user_response = self.client.post(
            "/auth/jwt/create/",
            data=data1
        )
        token = user_response.data['access']
        data = {
            "title": "ASDASDASD",
            "price": 15,
            "author": 1,
            "description": "sadasdasd",

        }
        response = self.client.post(
            "/api/ads/",
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Ad.objects.all().count() > 0)

    def test_list_ad(self):
        """
        тест вывода списка объявлений
        """
        user = User.objects.create(email='dadad@test.com', password='edcrfvtgb', role='User')
        Ad.objects.create(title="ASDASDASD", price=15, description="sadasdasd", author=user)
        response = self.client.get(
            '/api/ads/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_ad(self):
        """
        тест обновления объявления
        """
        user = User.objects.create(email='dadada@test.com')
        user.set_password('edcrfvtgb')
        user.save()
        data1 = {
            "email": "dadada@test.com",
            "password": "edcrfvtgb"
        }
        user_response = self.client.post(
            "/auth/jwt/create/",
            data=data1
        )
        token = user_response.data['access']
        Ad.objects.create(title="ASDASDASD", price=15, description="sadasdasd", author=user)

        data = {
            "title": "TFEWFWF",
            "price": 11515,
        }

        response = self.client.patch(
            '/api/ads/3/',
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(
            '/api/ads/3/',
            headers={"Authorization": f"Bearer {token}"}
        )

        queryset = Ad.objects.all()
        self.assertTrue(len(queryset) == 0)

    def tearDown(self):
        User.objects.all().delete()
        Ad.objects.all().delete()
        return super().tearDown()


class CommentTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_comment(self):
        """
        тест создания комментария
        """
        user = User.objects.create(email='dada@test.com', role='User')
        user.set_password('edcrfvtgb')
        user.save()
        data1 = {
            "email": "dada@test.com",
            "password": "edcrfvtgb"
        }
        user_response = self.client.post(
            "/auth/jwt/create/",
            data=data1
        )
        token = user_response.data['access']

        Ad.objects.create(title="ASDASDASD", price=15, description="sadasdasd", author=user)
        data = {
            "text": "ASDASDASD",
        }
        response = self.client.post(
            "/api/ads/4/comments/create/",
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Ad.objects.all().count() > 0)

    def test_list_comment(self):
        """
        тест вывода списка комментариев
        """
        user = User.objects.create(email='sutulaya_sobaka@test.com', password='wdzxczxyty')
        user.set_password('wdzxczxyty')
        user.save()
        data1 = {
            "email": "sutulaya_sobaka@test.com",
            "password": "wdzxczxyty"
        }
        user_response = self.client.post(
            "/auth/jwt/create/",
            data=data1
        )
        token = user_response.data['access']
        ad = Ad.objects.create(title="ASDASDASD", price=15, description="sadasdasd", author=user)
        Comment.objects.create(text="ASDASDASD", ad=ad, author=user)
        response = self.client.get(
            '/api/ads/5/comments/',
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        """
        тест обновления комментария
        """
        user = User.objects.create(email='dadada@test.com', password='edcrfvtgb', role='User')
        user.set_password('edcrfvtgb')
        user.save()
        data1 = {
            "email": "dadada@test.com",
            "password": "edcrfvtgb"
        }
        user_response = self.client.post(
            "/auth/jwt/create/",
            data=data1
        )
        token = user_response.data['access']
        ad = Ad.objects.create(title="ASDASDASD", price=15, description="sadasdasd", author=user)
        Comment.objects.create(text="ASDASDASD", ad=ad, author=user)

        data = {
            "text": "TFEWFWF"
        }

        response = self.client.patch(
            '/api/ads/6/comments/3/upd/',
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(
            '/api/ads/6/comments/3/delete/',
            headers={"Authorization": f"Bearer {token}"}
        )
        queryset = Comment.objects.all()
        self.assertTrue(len(queryset) == 0)

    def tearDown(self):
        User.objects.all().delete()
        Ad.objects.all().delete()
        return super().tearDown()
