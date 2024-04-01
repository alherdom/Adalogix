from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_registration, name='register'),
    path('list/', views.EmployeeListView.as_view(), name='list'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', views.EmployeeDetailView.as_view(), name='detail')
]
