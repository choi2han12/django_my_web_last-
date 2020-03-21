from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User


class Testview(TestCase):
    def setUp(self):
        self.client = Client()
        self.author_000 = User.objects.create(username='smith', password='nopassword')

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title
        self.assertEqual(title.text, '컴퓨터-수업공부')

        navbar = soup.find('div', id="navbar")
        self.assertIn('Themes', navbar.text)
        self.assertIn('영어독해', navbar.text)

        self.assertEqual(Post.objects.count(), 0)
        self.assertIn('아직 게시물이 없습니다', soup.body.text)
        post_000 = Post.objects.create(
            title='The first',
            content='Hello',
            created=timezone.now(),
            author=self.author_000,
         )
        self.assertGreater(Post.objects.count(), 0)
        response = self.client.get('/blog/')

        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        body=soup.body
        self.assertNotIn('아직 게시물이 없습니다', body.text)
        self.assertIn(post_000.title,body.text)

    def test_post_detail(self):
        self.assertGreater(Post.objects.count(),0)