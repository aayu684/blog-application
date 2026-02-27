import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from blog.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
print("Does admin exist?", User.objects.filter(username="admin").exists())

form = CustomUserCreationForm({
    'username': 'admin',
    'email': 'admin2@test.com',
    'password_1': 'adminpass',
    'password_2': 'adminpass'
})
print("Is valid?", form.is_valid())
print("Errors:", form.errors)
