def winner(names, scores):
    nom_best = []
    for i in range(len(scores)-1):
        nom_best.append(i)
        if scores[i+1] > scores[i]:
            nom_best.append(i+1)
    win = max(nom_best)
    winn = ""
    for j in range(len(names)):
        if j == win:
            winn = names[j]
    return winn


if __name__=="__main__":
    names = ["Аня", "Боря", "Вика"]
    scores = [7.0,   9.0,    9.0]
    print(winner(names, scores))
