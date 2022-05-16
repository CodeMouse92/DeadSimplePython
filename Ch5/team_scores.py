scores_team_1 = [100, 95, 120]
scores_team_2 = [45, 30, 10]
scores_team_3 = [200, 35, 190]

scores = (scores_team_1, scores_team_2, scores_team_3)

scores_team_1[0] = 300
print(scores[0])  # prints [300, 95, 120]

scores[0][0] = 400
print(scores[0])  # prints [400, 95, 120]
