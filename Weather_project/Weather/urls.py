from django.urls import path

from Weather import views
urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:c_id>/', views.delete, name='delete'),

]