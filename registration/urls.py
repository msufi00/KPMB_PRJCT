
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('regprogramme/', views.regprogramme, name="regprogramme"),

    # default
    path("new_course", views.new_course, name="new_course"),
    path("course/", views.course, name="course"),

    # for update
    path('update/<str:coursecode>', views.update, name='update'),
    path('update/updatedata/<str:coursecode>/', views.updatedata, name='updatedata'),
    # path('delete/<str:coursecode>/', views.delete, name='delete'),
    # path('viewdelete/<str:coursecode>/', views.viewdelete, name='viewdelete'),
    # path('viewdelete/delete/<str:coursecode>',views.delete,name = 'delete'),
    path('searchpage/', views.searchpage, name="searchpage"),
]

