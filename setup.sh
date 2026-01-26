#!/usr/bin/env bash
# Setup script for Bengali News Portal

echo "🎨 বাঙা বিদ্যার্থী নিউজ পোর্টাল সেটআপ"
echo "======================================"

# Create virtual environment
echo "✅ ভার্চুয়াল পরিবেশ তৈরি করছি..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "✅ প্যাকেজ ইনস্টল করছি..."
pip install -r requirements.txt

# Run migrations
echo "✅ ডাটাবেস মাইগ্রেট করছি..."
python manage.py migrate

# Create superuser
echo "✅ সুপারইউজার তৈরি করছি..."
echo "নিম্নলিখিত তথ্য সরবরাহ করুন:"
python manage.py createsuperuser

# Create initial categories
echo "✅ প্রাথমিক বিভাগ তৈরি করছি..."
python manage.py shell << EOF
from news.models import Category

categories = [
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

for name, slug, order in categories:
    Category.objects.get_or_create(
        name=name,
        defaults={'slug': slug, 'order': order}
    )
    print(f"✓ {name}")

print("\n✅ সব বিভাগ তৈরি হয়েছে!")
EOF

echo ""
echo "🎉 সেটআপ সম্পূর্ণ!"
echo ""
echo "ডেভেলপমেন্ট সার্ভার চালু করতে:"
echo "  python manage.py runserver"
echo ""
echo "অ্যাডমিন প্যানেল অ্যাক্সেস করতে:"
echo "  http://localhost:8000/admin/"
echo ""
