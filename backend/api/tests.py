from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
# Create your tests here.
class AuthTestCase(TestCase):
    def setUp(self) -> None:
        self.PASSWORD = "qwerty12345678" 
        self.foo = User.objects.create_user(username="Foo",
                                            password=self.PASSWORD)
        Profile.objects.create(user=self.foo)

    def test_register(self):
        c = Client()
        get_response    = c.get(reverse("register"))
        post_response   = c.post(reverse("register"), {"username": "testing",
                                                       "password": "qwerty123",
                                                       "password2": "qwerty123"}) 
        
        self.assertEqual(get_response.status_code, 405)
        self.assertEqual(post_response.status_code, 200)
        
    def test_login(self):
        c = Client()
        get_response = c.get(reverse("login"))
        post_response = c.post(reverse("login"),{"username": self.foo.username,
                                                 "password": self.PASSWORD})

        self.assertEqual(get_response.status_code, 405)
        self.assertEqual(post_response.status_code, 200)



class GameTestCase(TestCase):
    def setUp(self) -> None:
        self.PASSWORD = "qwerty12345678" 
        self.foo = User.objects.create_user(username="Foo",
                                            password=self.PASSWORD)
        Profile.objects.create(user=self.foo)

    def test_get_game(self):
        c = Client()
        login = c.login(username="Foo", password=self.PASSWORD)
        self.assertEqual(login, True)
        response = c.get(reverse("game"))
        self.assertEqual(response.status_code, 200)