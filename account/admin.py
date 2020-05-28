from django.contrib import admin

# Register your models here.
from account.models import Todo

admin.site.register(Todo)
