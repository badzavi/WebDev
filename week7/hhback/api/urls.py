
from django.urls import path

from api.views import company_list, company_detail, company_vacancy, vacancy_list, vacancy_detail, top_vacancies

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies/', company_vacancy),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', top_vacancies)
]