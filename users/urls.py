from django.urls import path, include
from users import views


urlpatterns = [
    path('signup/', views.UserView.as_view(), name ='user_view'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login_view'),
    path('logout/', views.LogoutView.as_view(), name='logout_view'),
    path('follow/<int:user_id>/', views.FollowView.as_view(), name='follow_view'),
    path('profile/', views.ProfileView.as_view(), name='profileview'),
]
