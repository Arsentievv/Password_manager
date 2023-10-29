from django.test import TestCase
from passwords.models import Service
from django.urls import reverse_lazy, reverse


def create_record(service_name, hashed_password=None):
    if hashed_password:
        return Service.objects.create(
            service_name=service_name, hashed_password=hashed_password
        )
    else:
        return Service.objects.create(
            service_name=service_name
        )


class ServiceAndPasswordTest(TestCase):
    def test_no_records(self):
        """Тест для проверки отсутствия записей в БД"""
        records_count = Service.objects.all()
        self.assertEqual(len(records_count), 0)

    def test_all_service_list(self):
        """Тест для проверки работы service_list эндпоинта"""
        response = self.client.get(reverse_lazy('service_list'))
        self.assertEqual(response.status_code, 200)

    def test_get_certain_record(self):
        """Тест для проверки get_password эндпоинта"""
        record = create_record(service_name='test', hashed_password='12345test')
        response = self.client.get(reverse_lazy('get_password', kwargs={'slug': record.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, record.get_decrypted_password())
        self.assertContains(response, record.service_name)

    def test_password_update(self):
        """Тест для проверки запроса изменения пароля"""
        record = create_record(service_name='test', hashed_password='12345test')
        post_response = self.client.post(
            reverse('get_password', kwargs={'slug': record.slug}),
            {'hashed_password': '12345new'}
        )
        self.assertEqual(post_response.status_code, 200)
        record.refresh_from_db()

        self.assertEqual(record.get_decrypted_password(), '12345new')

    def test_password_create(self):
        """Тест для проверки запроса создания пароля"""
        record = create_record(service_name='test')
        post_response = self.client.post(
            reverse('get_password', kwargs={'slug': record.slug}),
            {'hashed_password': '12345new'}
        )
        self.assertEqual(post_response.status_code, 200)
        record.refresh_from_db()

        self.assertEqual(record.get_decrypted_password(), '12345new')




