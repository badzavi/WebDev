from django.http.response import JsonResponse
from django.http import Http404
from django.db.models import Count

from api.models import Company, Vacancy


def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'companies post request'})


def company_detail(request, company_id):
    if request.method == 'GET':
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': 'product does not exists'})
        return JsonResponse(company.to_json())
    elif request.method == 'POST':
        return JsonResponse({'data': 'company post request'})


def company_vacancy(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
         vacancies = company.vacancy_set.all()
         vacancies_json = [v.to_json() for v in vacancies]
         return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
            return JsonResponse({'data': 'vacancies by company post request'})


def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'vacancies post request'})


def vacancy_detail(request, vacancy_id):
    if request.method == 'GET':
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            return JsonResponse(vacancy.to_json())
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
    elif request.method == 'POST':
        return JsonResponse({'data': 'vacancy post request'})


def top_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.annotate(Count('salary')).order_by('-salary')[:10]
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'error': 'you cannot post here'})
