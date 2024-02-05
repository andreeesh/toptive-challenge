from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
import requests
import json

class CompetitionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Competition.objects.all().order_by('name')
    serializer_class = CompetitionSerializer

class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer

class TotalPlayersView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, **kw):
        competition_id = Competition.objects.values_list('id', flat=True).get(code = kw['code'])
        players = Player.objects.get(competition = competition_id).count()
        data = [{'total':queryset}]
        return Response(data)

class ImportLeagueView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, **kw):
        payload = {}
        headers = {'X-Auth-Token': 'e3de006d08ef4ea28f8df88a2efec9b4'}

        # Refact --
        url_competitions = "https://api.football-data.org/v2/competitions/" + kw['code']
        resp_competitions = requests.request("GET", url_competitions, headers=headers, data=payload)
        resp_competitions_to_json = json.loads(resp_competitions.text.encode('utf8'));
        # -- Refact

        if 'id' in resp_competitions_to_json:
            Competition(id=resp_competitions_to_json['id'], name=resp_competitions_to_json['name'], code=resp_competitions_to_json['code'], areaname=resp_competitions_to_json['area']['name']).save()

            obj_competition = Competition.objects.get(id = resp_competitions_to_json['id'])

            # Refact --
            url_teams = "https://api.football-data.org/v2/competitions/" + str(resp_competitions_to_json['id']) + "/teams"
            response_teams = requests.request("GET", url_teams, headers=headers, data=payload)
            resp_teams_to_json = json.loads(response_teams.text.encode('utf8'));
            # -- Refact

            if 'teams' in resp_teams_to_json:
                for team in resp_teams_to_json['teams']:
                    Team(id=team['id'], name=team['name'], tla=team['shortName'], areaname=team['area']['name'], email=team['email'], competition=obj_competition).save();

                    obj_team = Team.objects.get(id = team['id'])

                    # Refact --
                    url_squad = "https://api.football-data.org/v2/teams/" + str(team['id'])
                    response_squad = requests.request("GET", url_squad, headers=headers, data=payload)
                    resp_squad_to_json = json.loads(response_squad.text.encode('utf8'))
                    # -- Refact

                    if 'squad' in resp_squad_to_json:
                        for player in resp_squad_to_json['squad']:
                            Player(id=player['id'], name=player['name'], position=player['position'], dateofbirth=player['dateOfBirth'], countryofbirth=player['countryOfBirth'], nationality=player['nationality'], team=obj_team, competition=obj_competition).save();
        else:
            data = [{"error":resp_competitions_to_json['errorCode'], "message":resp_competitions_to_json['message']}]

        return Response(resp_teams_to_json['teams'])
