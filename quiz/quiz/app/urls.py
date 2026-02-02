from django.urls import path
from . import views

urlpatterns = [
    path('kerdesek/<int:question_id>', views.view_question, name='hello')
]
