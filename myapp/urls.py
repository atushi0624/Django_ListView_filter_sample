from django.conf.urls import url
from .views import FoodListView

urlpatterns = [
    url(r'^$', FoodListView.as_view(), name='list'),
]