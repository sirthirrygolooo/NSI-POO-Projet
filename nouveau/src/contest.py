class Car:
    def __init__(self, name, points, penality, state):
        self.name = name
        self.points = points
        self.penality = penality
        self.state = state
        self.classification = None
        self.total = None
        self.team = None

    def getAllInformations(self):
        """Return a list of all informations about the car """
        return [self.name, self.classification, int(self.points), int(self.penality), self.state, self.team]

    def calculateTotal(self, multiplier):
        """Calculate the total points of the car
        {multiplier} -> int"""
        self.total = int(self.points * multiplier + self.penality) 

    def set(self, type, value):
        """Edit the value of a type of information
        {type} -> str
        {value} -> str/int/object"""
        match type:
            case "name":
                self.name = value
            case "points":
                self.points = value
            case "penality":
                self.penality = value
            case "state":
                self.state = value
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
            case "penality":
                return self.penality
            case "total":
                return self.total
            case "state":
                return self.state
            case "team":
                return self.team

class Team:
    def __init__(self, name):
        self.name = name
        self.cars = None

    def get(self, type, value=None):
        """Return the value of a type of information
        {type} -> str"""
        match type:
            case "name":
                return self.name
            case "car":
                if value != None:
                    for car in self.cars:
                        if car.get("name") == value:
                            return car
                return None
            case "listCars":
                return self.cars
            case "listCarsName":
                listeCars = []
                for car in self.cars:
                    listeCars.append(car.getName())
                return listeCars

    def addCar(self, Car):
        """Add a car to the team
        {Car} - Object"""
        if Car.get("team") == None:
            Car.set("team", self)
            self.cars.append(Car)
            return True
        else:
            return False

    def removeCar(self, Car):
        """Remove a car from the team
        {Car} - Object"""
        if Car in self.cars:
            self.cars.remove(Car)
            return True
        else:
            return False

    def editName(self, name):
        """Edit the name of the team
        {name} -> str"""
        self.name = name

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
        self.rules = pointsPerSeconds
        return True

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
            for car in Team.get("listCars"):
                self.removeCar(car)
            return True
        else:
            return False

    def addCar(self, Car, Team=None):
        """Add a car to a team
        {Car} -> object
        {Team} -> object"""
        if Team in self.teams:
            Team.addCar(Car)
        else:
            self.addTeam(Team)
        self.classement.append(Car)

    def removeCar(self, Car):
        """Remove a car from the contest
        {Car} -> Car object"""
        if Car in self.classement:
            self.classement.remove(Car)
            return True
        else:
            return None

