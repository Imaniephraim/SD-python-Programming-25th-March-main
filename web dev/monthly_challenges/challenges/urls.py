from django.urls import path
from challenges import views


# urlpatterns = [
#     path('january', views.january),
#      path('february', views.february),
#      path('march', views.march),
#      path('april', views.april),
# ]

urlpatterns = [
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge)
]
