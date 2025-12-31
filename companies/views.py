from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Company
from .serializers import CompanySerializer

class CompanyPagination(PageNumberPagination):
    page_size = 5

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-created_time')
    serializer_class = CompanySerializer
    pagination_class = CompanyPagination
