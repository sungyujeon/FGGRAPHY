from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('top-ranked/', views.get_top_ranked_users),
    
    # admin
    path('calc-ranking/', views.calc_ranking),
]