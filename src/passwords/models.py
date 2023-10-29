from django.db import models
from django.template.defaultfilters import slugify
from cryptography.fernet import Fernet

import src.settings


class Service(models.Model):
    service_name = models.CharField(
        max_length=100,
        verbose_name='название сервиса'
    )
    hashed_password = models.CharField(
        max_length=300,
        verbose_name='Зашифрованный пароль',
        blank=True,
        null=True
    )
    slug = models.SlugField(
        null=False,
        unique=True
    )

    class Meta:
        verbose_name = 'сервис и пароль'
        verbose_name_plural = 'сервисы и пароли'

    def save(self, *args, **kwargs):
        """Метод для сохранения объекта сервиса,
         при котором шифруется пароль и определяется поле slug"""
        if self.hashed_password:
            key = src.settings.FRENT_KEY
            fernet = Fernet(key)
            encrypted_password = fernet.encrypt(self.hashed_password.encode())
            self.hashed_password = encrypted_password.decode()
        if not self.slug:
            self.slug = slugify(self.service_name)
        return super().save(*args, **kwargs)

    def get_decrypted_password(self):
        """Метод для расшифровки пароля"""
        key = src.settings.FRENT_KEY
        fernet = Fernet(key)
        encoded_password = self.hashed_password.encode()
        return fernet.decrypt(encoded_password).decode()

