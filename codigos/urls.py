from django.urls import path

from codigos.views import RegisterView

urlpatterns = [
    path('codigos/<str:d_codigo>', RegisterView.as_view(), name='registros_list')
]
