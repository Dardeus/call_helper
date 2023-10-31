from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers.api import users as user_s

User = get_user_model()

@extend_schema_view(
    post=extend_schema(summary='Регистарция пользователя',
                       tags=['Аутентификация & Авторицзация']),
)
class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = user_s.RegistrationSerializer