from django.urls import path

from codigos.views import RegisterView

urlpatterns = [
    path('zipcode/<str:d_codigo>', RegisterView.as_view(), name='registros_list')
]
