from django.shortcuts import render
from .forms import YearFilterForm
from .models import Movie
# Create your views here.

def index(request):
    form = YearFilterForm(request.GET or None)
    data = Movie.objects.all()

    # 폼의 유효성 확인
    if request.GET and form.is_valid():
        # 검증된 후의 적당한 데이터가 들어 있는 변수가 cleand_data
        year = form.cleaned_data['year']
        if year:
            data = data.filter(연도=year)

    return render(request, 'movies/index.html', {'data': data, 'form': form})