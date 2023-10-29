import django_filters
from rest_framework import generics
from passwords.models import Service
from passwords.serializers import ServiceAndPasswordSerializer
from rest_framework.response import Response


class GetPasswordView(generics.RetrieveUpdateAPIView):
    """Представление для отображения конкретного сервиса"""
    serializer_class = ServiceAndPasswordSerializer
    queryset = Service.objects.all()
    lookup_field = 'slug'

    def post(self, request, *args, **kwargs):
        """Метод для обновления или создания пароля"""
        data = request.data
        slug = kwargs.get("slug")
        service = Service.objects.get(slug=slug)
        new_password = data['hashed_password']
        service.hashed_password = new_password
        service.save()
        serializer = ServiceAndPasswordSerializer(service)
        return Response({'data': serializer.data})


class ServiceNameFilter(django_filters.FilterSet):
    """Фильтр для поиска записи по части имени сервиса"""
    service_name = django_filters.CharFilter(
        field_name='service_name', lookup_expr='icontains'
    )

    class Meta:
        model = Service
        fields = ['service_name']


class GetServiceList(generics.ListAPIView):
    """Представление для отображения всех сервисов и поиска сервиса по части имени"""
    serializer_class = ServiceAndPasswordSerializer
    queryset = Service.objects.all()
    filterset_class = ServiceNameFilter


