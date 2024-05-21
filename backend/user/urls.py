from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_registration, name='register'),
    path('list/', views.EmployeeListView.as_view(), name='list'),
    path('list/available/', views.AvailableEmployeeListView.as_view(), name='available_list'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', views.EmployeeDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('delete/multiple/', views.UserMultipleDelete.as_view(), name='user_multiple_delete'),
    path('reset/password/', views.reset_password, name='reset_password'),
]
