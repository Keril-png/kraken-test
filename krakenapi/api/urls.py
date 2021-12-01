from django.urls import path, include
from.views import get_rec


urlpatterns = [
    path('recs/<str:pair_name>/', get_rec, name='get_recs'),
]