class Player:
    def __init__(self, name, points, penalty, state):
        self.name = name
        self.points = points
        self.penalty = penalty
        self.state = state
        self.classification = None
        self.total = None
        self.team = None

    def __str__(self):
        return f"{self.name} - {self.classification} - {self.points} - {self.penalty} - {self.state} - {self.total} - {self.team}"

    def getAllInformations(self):
        """Return a list of all informations about the player"""
        return [self.name, self.classification, int(self.points), int(self.penalty), self.state, self.classification, self.total, self.team]

    def calculateTotal(self, multiplier):
        """Calculate the total points of the player
        {multiplier} -> int"""
        self.total = int(self.points) * int(multiplier) + int(self.penalty)

    def set(self, type, value):
        """Edit the value of a type of information
        {type} -> str
        {value} -> str/int/object"""
        match type:
            case "name":
                self.name = value
            case "points":
                self.points = value
            case "penalty":
                self.penalty = value
            case "state":
                self.state = value
            case "classification":
                self.classification = value
            case "team":
                self.team = value

    def get(self, type):
        """Return the value of a type of information
        {type} -> str"""
        match type:
            case "name":
                return self.name
            case "points":
                return self.points
            case "penalty":
                return self.penalty
            case "state":
                return self.state
            case "classification":
                return self.classification
            case "total":
                return self.total
            case "team":
                return self.team

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def editName(self, name):
        """Edit the name of the team
        {name} -> str"""
        self.name = name

    def get(self, type, value=None):
        """Return the value of a type of information
        {type} -> str"""
        match type:
            case "name":
                return self.name
            case "player":
                if value != None:
                    for player in self.players:
                        if player.get("name") == value:
                            return player
                return None
            case "listPlayers":
                return self.players
            case "listPlayersName":
                listePlayers = []
                for player in self.players:
                    listePlayers.append(player.get("name"))
                return listePlayers

    def addPlayerInTeam(self, Player):
        """Add a player to the team
        {Player} - Object"""
        if Player.get("team") == None:
            Player.set("team", self)
            self.players.append(Player)
            return Player
        else:
            return False

    def removePlayerInTeam(self, Player):
        """Remove a player from the team
        {Player} - Object"""
        if Player in self.players:
            self.players.remove(Player)
            return True
        else:
            return False

class Contest:
    def __init__(self):
        self.classement = []
        self.teams = []
        self.rules = None

    def sortClassement(self):
        """Sort the classement list by total points"""
        for i in self.classement:
            i.calculateTotal(self.rules)

        self.classement.sort(key=lambda a: a.get("total"))
        for i in range(len(self.classement)):
            self.classement[i].classification = i+1

    def editRules(self, pointsPerSeconds):
        """Edit the rules of the contest
        {pointsPerSeconds} -> int"""
        self.rules = int(pointsPerSeconds)
        return True

    def addPlayer(self, Player):
        """Add a player to a team
        {Player} -> object"""
        for i in self.classement:
            if i.get('name') == Player.get('name'):
                return False
        self.classement.append(Player)
        return True

    def removePlayer(self, playerName):
        """Remove a player from the contest
        {Player} -> Player object"""
        for player in self.classement:
            if player.get('name') == playerName:
                self.classement.remove(player)
                return True
        return False

    def addTeam(self, Team):
        """Add a team to the contest
        {Team} -> object"""
        if Team not in self.teams:
            self.teams.append(Team)
            return True
        else:
            return False

    def removeTeam(self, Team):
        """Remove a team from the contest
        {Team} -> object"""
        if Team in self.teams:
            self.teams.remove(Team)
            for player in Team.get("listPlayers"):
                self.removePlayer(player)
            return True
        else:
            return False


contest = Contest()