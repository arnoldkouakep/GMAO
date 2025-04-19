from app.modules.equipe.add_team_form import AddTeamForm
from app.modules.equipe.list_teams_form import ListTeamsForm


class TeamController:
    def __init__(self, root, connection):
        self.root = root
        self.connection = connection

    def show_add_team_form(self):
        AddTeamForm(self.root, self.connection)

    def show_list_teams_form(self):
        ListTeamsForm(self.root, self.connection)
