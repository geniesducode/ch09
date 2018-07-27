def get_rank(score_percentage):
    ranks = [
        [0, "Pas bravo!", "Il fallait le faire."],
        [25, "Y a du boulot...", "C'est mieux que rien."],
        [50, "Pas mal", "Une sur deux, c'est pas encore ça."],
        [75, "Bravo!", "Tu en sais plus que la plupart des gens!"],
        [100, "Impressionnant!", "Wow! Y a de la triche dans l'air."],
    ]

    for rank in ranks:
        if score_percentage <= rank[0]:
            return {'title': rank[1], 'description': rank[2]}

    raise ValueError("Invalid score %s" % score)
