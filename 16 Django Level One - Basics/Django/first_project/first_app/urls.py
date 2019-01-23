from django.conf.urls import url
from first_app import views

urlpatterns = [
    # url(r'^', views.t_index, name='t_index'),
    url(r'^help/', views.help, name='help'),

]