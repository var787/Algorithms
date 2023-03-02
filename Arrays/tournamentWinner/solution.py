# set a variable to the value in results that declares the home team as the winner # noqa
HOME_TEAM_WON = 1


# O(n) time | O(k) space
def tournamentWinner(competions, results):
    # initialize the beast team as an empty string
    bestTeam = ""
    # initialize a dictionary with the empty string key "bestTeam" and value 0
    scores = {bestTeam: 0}

    # enumerate over competitions to access games and find out winner using results array # noqa
    for idx, competition in enumerate(competions):
        result = results[idx]
        # python shorcut to assign lop variables to elements in list
        homeTeam, awayTeam = competition

        # pick winner between games from the result available in results array
        winning_team = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScore(winning_team, 3, scores)

        # check to see if recently updated team has a higher score than previous best team # noqa 
        if scores[winning_team] > scores[bestTeam]:
            bestTeam = winning_team
    return bestTeam


# helper function to assign and update points in scores dictionary # noqa
def updateScore(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points
