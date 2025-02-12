
def main():
    scores = {'Player 1':0,'Player 2':0}
    print(scores['Player 1'])
    scores['Player 1'] += 1
    print_scores(scores)

def print_scores(scores):
    print(f"Player 1 score: {scores['Player 1']}\n\
Player 2 score: {scores['Player 2']}")

main()
