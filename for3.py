school_7 = [{'school_class': '4а', 'scores': [3, 3, 3, 3, 3]},
            {'school_class': '4б', 'scores': [4, 4, 4, 4]},
            {'school_class': '4в', 'scores': [5, 5, 5, 5, 5, 5]}]
total_score_mean_sum = 0
for school_class in school_7:
    score_sum = 0
    for score in school_class['scores']:
        score_sum = score_sum + score
    score_mean = score_sum / len(school_class['scores'])
    print(score_mean)
    total_score_mean_sum = total_score_mean_sum + score_mean
total_score_mean = total_score_mean_sum / len(school_7)
print(total_score_mean)