from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField('Question', max_length=250, unique=True)
    option_a = models.CharField('Option A', max_length=150)
    option_b = models.CharField('Option B', max_length=150)
    option_c = models.CharField('Option C', max_length=150)
    option_d = models.CharField('Option D', max_length=150)
    answer = models.CharField('Correct answer', choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')), max_length=1)

    def __str__(self):
        return self.text