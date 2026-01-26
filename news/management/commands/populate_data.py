from django.core.management.base import BaseCommand
from news.models import Category, Article
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = 'Create sample categories and demo articles'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            ('পশ্চিমবঙ্গ', 'paschimbongo', 1),
            ('ভারত', 'bharat', 2),
            ('আন্তর্জাতিক', 'antarjatik', 3),
            ('ইতিহাস', 'itihas', 4),
            ('সংস্কৃতি', 'sanskriti', 5),
            ('ধর্ম কথা', 'dharm-kotha', 6),
            ('খেলাধুলো', 'khelhudlo', 7),
            ('এবিভিপি', 'abvp', 8),
            ('সংঘ', 'sangha', 9),
            ('বিনোদন', 'binodan', 10),
            ('বিমর্শ', 'bimosh', 11),
            ('সম্পাদকীয়', 'sampadkio', 12),
        ]

        for name, slug, order in categories_data:
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={'slug': slug, 'order': order}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created category: {name}'))
            else:
                self.stdout.write(f'  Category exists: {name}')

        # Create demo articles if they don't exist
        admin_user = User.objects.filter(is_superuser=True).first()
        if not admin_user:
            self.stdout.write(self.style.ERROR('No superuser found. Please create one first.'))
            return

        demo_articles = [
            {
                'title': 'বাঙালি সংস্কৃতির নতুন মাত্রা',
                'category': Category.objects.get(slug='sanskriti'),
                'summary': 'আধুনিক যুগে বাঙালি সংস্কৃতির সংরক্ষণ এবং বিকাশ নিয়ে একটি গুরুত্বপূর্ণ আলোচনা।',
                'content': '<h2>বাঙালি সংস্কৃতির পরিচয়</h2><p>বাঙালি সংস্কৃতি হল দক্ষিণ এশিয়ার একটি সমৃদ্ধ এবং বৈচিত্র্যময় সংস্কৃতি। এটি হাজার হাজার বছরের ইতিহাস, ঐতিহ্য এবং মূল্যবোধের একটি সংমিশ্রণ।</p><p>আমাদের সংস্কৃতি শিল্প, সাহিত্য, সঙ্গীত এবং নৃত্যে সমৃদ্ধ।</p>',
            },
            {
                'title': 'ভারতীয় খেলাধুলোয় নতুন রেকর্ড',
                'category': Category.objects.get(slug='khelhudlo'),
                'summary': 'ভারতীয় ক্রীড়াবিদরা আন্তর্জাতিক পর্যায়ে নতুন মাইলফলক স্থাপন করেছেন।',
                'content': '<h2>ক্রীড়া বিজয়</h2><p>এই বছর ভারতীয় ক্রীড়াবিদরা বিভিন্ন আন্তর্জাতিক প্রতিযোগিতায় অসাধারণ সাফল্য অর্জন করেছেন।</p>',
            },
            {
                'title': 'শিক্ষা ব্যবস্থায় সংস্কার প্রয়োজন',
                'category': Category.objects.get(slug='sampadkio'),
                'summary': 'সম্পাদকীয়: আমাদের শিক্ষা ব্যবস্থার আধুনিকীকরণ অপরিহার্য।',
                'content': '<h2>শিক্ষা নিয়ে চিন্তা</h2><p>আমাদের শিক্ষা ব্যবস্থা বহুদিন ধরে প্রাচীন পদ্ধতির উপর নির্ভর করছে। এটি পরিবর্তনের সময় এসেছে।</p>',
            },
        ]

        for article_data in demo_articles:
            article, created = Article.objects.get_or_create(
                title=article_data['title'],
                defaults={
                    'slug': article_data['title'].lower().replace(' ', '-'),
                    'category': article_data['category'],
                    'author': admin_user,
                    'summary': article_data['summary'],
                    'content': article_data['content'],
                    'status': 'published',
                    'published_at': timezone.now() - timedelta(days=1),
                    'meta_title': article_data['title'],
                    'meta_description': article_data['summary'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created article: {article_data["title"]}'))
            else:
                self.stdout.write(f'  Article exists: {article_data["title"]}')

        self.stdout.write(self.style.SUCCESS('\n✅ All data created successfully!'))
