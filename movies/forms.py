from django import forms
from .models import Movie

class YearFilterForm(forms.Form):
    year = forms.ChoiceField(label='연도', choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 연도를 선택해서 조회
        year_choices = [(year, year) for year in Movie.objects.values_list('연도', flat=True).distinct()]
        self.fields['year'].choices = [('', '전체')] + year_choices
