# oo_tt_sim.py
# Ryan Neubauer

from random import random

class Player:

    def __init__(self, prob):
        self.prob = prob
        self.games_won = 0
        self.score = 0

    def reset_score(self):
        self.score = 0

    def wins_serve(self):
        return random() < self.prob

    def award_point(self):
        self.score += 1

    def award_game(self):
        self.games_won += 1

    def get_score(self):
        return self.score

    def get_games_won(self):
        return self.games_won


class Game:

    def __init__(self, first_server, first_reciever):
        self.server = first_server
        self.reciever = first_reciever

    def play(self):
        self.reset_scores()
        while not self.game_over():
            if self.server.wins_serve():
                self.server.award_point()
            else:
                self.reciever.award_point()
            self.check_service_change()

    def reset_scores(self):
        self.server.reset_score()
        self.reciever.reset_score()

    def award_rally_point(self):
        if self.server.wins_serve():
            self.server.award_point()
        else:
            self.reciever.award_point()
        self.check_service_change()

    def game_over(self):
        a = self.server.get_score()
        b = self.reciever.get_score()
        return (a >= 11 or b >= 11) and abs(a-b) >= 2

    def check_service_change(self):
        total_points = self.server.get_score() + self.reciever.get_score()
        if total_points % 2 == 0 or total_points >= 20:
            self.swap_service()

    def swap_service(self):
        # change self.server and self.reciever
        self.server, self.reciever = self.reciever, self.server


class Match:

    def __init__(self, num_games, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.need_to_win = num_games // 2 + 1

    def play(self):
        # play the match to completion
        self.playerA.games_won = 0
        self.playerB.games_won = 0
        counter = 1
        while not self.match_over():
            self.create_game(counter)
            counter += 1
    
    def create_game(self, game_number):
        # odd games, player A is first server
        # even games, player B is first server
        # return an appropriate game
        if game_number % 2 == 0:
            game = Game(self.playerA, self.playerB)
        else:
            game = Game(self.playerB, self.playerA)
        game.play()
        self.award_game_to_winner()

    def award_game_to_winner(self):
        # determine which player won and award them the game
        a = self.playerA.get_score()
        b = self.playerB.get_score()
        if a > b:
            self.playerA.award_game()
        else:
            self.playerB.award_game()

    def get_results(self):
        # Return the number of games won by PlayerA and PlayerB
        return self.playerA.get_games_won(), self.playerB.get_games_won()

    def match_over(self):
        # Return a bool indicating whether the match is over
        a = self.playerA.get_games_won()
        b = self.playerB.get_games_won()
        return a == self.need_to_win or b == self.need_to_win


def get_inputs():
    probA = float(input("Enter probability player A wins serve: "))
    probB = float(input("Enter probability player B wins serve: "))
    gpm = int(input("How many games per match? "))
    n = int(input("How matches should I simulate? "))
    return probA, probB, gpm, n

def printIntro():
    print("This program simulates matches of table tennis.")
    print("")

def main():
    printIntro()
    probA, probB, gpm, n = get_inputs()
    matches_a = 0
    matches_b = 0
    for i in range(n):
        match = Match(gpm, probA, probB)
        match.play()
        a_wins, b_wins = match.get_results()
        if a_wins > b_wins:
            matches_a += 1
        else:
            matches_b += 1

    print("Player A won", matches_a, "Player B won", matches_b)
    input("Press <Enter> to quit")


if __name__ == "__main__":
    main()
