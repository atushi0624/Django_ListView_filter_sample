from django.conf.urls import url

urlpatterns = [
    url(r'^$', ListView.as_view(), name='listview'),
]