from django.conf.urls import  url
from provinsi import views

urlpatterns = [
    url(r'^test$', views.TestView.as_view(), name='test'),
    url(r'^view$', views.ListProvinceView.as_view(), name='view'),
    url(r'^save$', views.SaveProvinceView.as_view(), name='save'),
    url(r'^edit/(?P<id>\d+)$', views.EditProvinceView.as_view(), name='edit'),
    url(r'^update$', views.UpdateProvinceView.as_view(), name='update'),
    url(r'^delete/(?P<id>\d+)$', views.DeleteProvinceView.as_view(), name='delete'),
]