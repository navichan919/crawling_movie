from django.db import models

# Create your models here.

class Movie(models.Model):
    연도 = models.IntegerField()
    순위 = models.IntegerField()
    제목 = models.CharField(max_length=50)
    감독 = models.CharField(max_length=10)
    주연1 = models.CharField(max_length=10)
    주연2 = models.CharField(max_length=10)
    개봉일 = models.CharField(max_length=20)
    관객수 = models.IntegerField(null = True)
    장르 = models.CharField(max_length=20)
    수상 = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.연도}/{self.순위}위/{self.제목}"