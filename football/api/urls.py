from django.urls import include, path
from rest_framework import routers
from . import views
from .views import ImportLeagueView, TotalPlayersView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'competitions', views.CompetitionViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'players', views.PlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('import-league/<code>', ImportLeagueView.as_view()),
    path('total-players/<code>', TotalPlayersView.as_view()),
]
