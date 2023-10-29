from rest_framework import serializers
from passwords.models import Service


class ServiceAndPasswordSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели сервиса"""
    decrypted_password = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ["service_name", "decrypted_password"]

    def get_decrypted_password(self, obj):
        """Метод для получения расшифрованного пароля при сериализации данных"""
        if obj.hashed_password:
            return obj.get_decrypted_password()
        else:
            return 'No password added'

