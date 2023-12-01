from django.core.management import BaseCommand
import csv
from movies.models import Movie

# python manage.py load_csv를 터미널에 입력한다.

class Command(BaseCommand):
    
    def handle(self,*args,**options):
        self.save_to_database('영화 박스오피스(2013-2022).csv')
        
    def save_to_database(self,filename):
        with open(filename, 'r', newline='', encoding='cp949') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # 데이터베이스에 집어넣기
                Movie.objects.create(
                    연도=row['연도'],
                    순위=row['순위'],
                    제목=row['제목'],
                    감독=row['감독'],
                    주연1=row['주연1'],
                    주연2=row['주연2'],
                    개봉일=row['개봉일'],
                    관객수=row['관객수'],
                    장르=row['장르'],
                    수상=row['수상'],
                )
