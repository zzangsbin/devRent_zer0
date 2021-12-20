from django.db import models

# Create your models here.
class Post(models.Model):
    category_choices = (('choice1', '일상'), ('choice2', '냠냠'), ('choice3', '기타'), ('choice4', '뒷담'))


    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 10, choices = category_choices, default = '') #비어있으므로 첫번째 거가 들어감!
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

        