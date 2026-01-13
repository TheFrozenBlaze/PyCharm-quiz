from django.contrib import admin

# Register your models here.
from quiz.app.models import Question

admin.site.register(Question)