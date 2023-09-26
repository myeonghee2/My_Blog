from django.urls import path, include
from users import views


urlpatterns = [
    path('signup/', views.UserView.as_view(), name ='user_view'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login_view'),
]
