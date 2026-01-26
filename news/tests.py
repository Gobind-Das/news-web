from django.test import TestCase
from django.contrib.auth.models import User
from news.models import Category, Article


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='পশ্চিমবঙ্গ',
            slug='paschimbongo',
            description='পশ্চিমবঙ্গ সম্পর্কিত খবর'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'পশ্চিমবঙ্গ')
        self.assertEqual(self.category.slug, 'paschimbongo')

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), 'পশ্চিমবঙ্গ')


class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testauthor',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='পশ্চিমবঙ্গ',
            slug='paschimbongo'
        )
        self.article = Article.objects.create(
            title='টেস্ট আর্টিকেল',
            slug='test-article',
            category=self.category,
            author=self.user,
            summary='এটি একটি টেস্ট আর্টিকেল',
            content='<p>টেস্ট কন্টেন্ট</p>',
            status='published'
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, 'টেস্ট আর্টিকেল')
        self.assertEqual(self.article.status, 'published')

    def test_article_string_representation(self):
        self.assertEqual(str(self.article), 'টেস্ট আর্টিকেল')

    def test_article_has_correct_author(self):
        self.assertEqual(self.article.author, self.user)
