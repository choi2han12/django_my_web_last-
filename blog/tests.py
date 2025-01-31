from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.utils import timezone
from .models import Post, Category
from django.contrib.auth.models import User

def create_category(name='life', description=''):
    category, is_created = Category.objects.get_or_create(
        name=name,
        description=description
    )
    return category


def create_post(title, content, author, category=None):
    blog_post = Post.objects.create(
        title=title,
        content=content,
        created=timezone.now(),
        author=author,
        category=category,
    )
    return blog_post


class TestModel(TestCase):
    def setUp(self):
        self.client=Client()
        self.author_000=User.objects.create(username='smith', password='nopassword')

    def test_category(self):
        category = create_category()
        post_000 = create_post(
            title='The first',
            content='Hello',
            author=self.author_000,
            category=category,
        )
        self.assertEqual(category.post_set.count(),1)


    def test_post(self):
        category =create_category()
        post_000 = create_post(
            title='The first',
            content='Hello',
            author=self.author_000,
            category=category,
        )



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



    def check_navbar(self,soup):
        navbar=soup.find('div',id='navbar')
        self.assertIn('English-HomeWork',navbar.text)


    def test_post_detail(self):
        post_000 = create_post(
            title='The first',
            content='Hello',
            author=self.author_000,
        )

        self.assertGreater(Post.objects.count(), 0)
        post_000_url = post_000.get_absolute_url()

        self.assertEqual(post_000_url, '/blog/{}/'.format(post_000.pk))

        response=self.client.get(post_000_url)
        self.assertEqual(response.status_code,200)
        soup=BeautifulSoup(response.content,'html.parser')
        title=soup.title
        body=soup.body
        post_000_read_more_btn = body.find('a', id='read-more-post-{}'.format(post_000.pk))
        # 왜 값이 안찾아지는지??

        print(post_000_read_more_btn)
        main_div=body.find('div', id='main_div')
        self.assertIn(post_000.title, main_div.text)
        self.assertIn(post_000.author.username, main_div.text)
        # self.assertIn(post_000.author.username, main_div.text)
        category_card=body.find('div',id='category-card')
        self.assertIn('미분류',category_card.txt)
