from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    Title = models.CharField('TITLE',max_length=50)
    Content = models.TextField('CONTENT')

class DjangoBoard(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    created_date = models.DateField(null=True, blank=True)
    mail = models.CharField(max_length=50, blank=True)
    memo = models.CharField(max_length=200, blank=True)
    hits = models.IntegerField(null=True, blank=True)

class Post(models.Model):  # models.Model: Post(클래스첫자는 대문자)가 장고 모델(=객체)임을 나타낸다. 이 코드 덕에 장고는 Post가 DB에 저장된다 알게 됨.
    author = models.ForeignKey('auth.User')  # 다른 모델에 대한 링크
    title = models.CharField(max_length=200)  # 글자수가 제한된 텍스트
    text = models.TextField()  # 글자수에 제한 없는 텍스트
    created_date = models.DateTimeField(default=timezone.now)  # 날짜와 시간
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):  # 메서드. 이름은 소문자로 시작.
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #얘를 호출하면 Post모델의 title을 얻음
        return self.title