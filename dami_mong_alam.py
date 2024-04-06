import random

def get_player_names():
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            if num_players <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")

    players = []
    for i in range(num_players):
        player_name = input(f"Enter player {i + 1} name: ")
        players.append(player_name)
    
    return players

def conduct_round(players, odd_player_out):
    winners = []
    print("\nStarting a new round:")
    automatically_advanced_player = None

    # Determine the odd player out and handle the "twice to beat" situation
    if not odd_player_out and len(players) % 2 != 0:
        odd_player_out = random.choice(players)
        players.remove(odd_player_out)
        print(f"{odd_player_out} is the odd player out and will need to win twice in their next match.")
    elif odd_player_out:
        print(f"{odd_player_out} needs to win twice in this round.")
        opponent = random.choice(players)
        players.remove(opponent)
        if conduct_twice_to_beat_match(odd_player_out, opponent):
            winners.append(odd_player_out)
        else:
            winners.append(opponent)
        odd_player_out = None  # Reset for the next round

    # Conduct matches for the remaining players
    while len(players) > 1:
        player1, player2 = players.pop(0), players.pop(0)
        print(f"Match: {player1} vs {player2}")
        winner = input(f"Enter the winner ({player1} or {player2}): ")
        while winner not in [player1, player2]:
            print("Invalid input. Please enter the name of the winner exactly as shown.")
            winner = input(f"Enter the winner ({player1} or {player2}): ")
        winners.append(winner)

    if len(players) == 1:
        # If there's an unpaired player, they automatically advance
        automatically_advanced_player = players[0]
        winners.append(players[0])

    # Only return the new odd player out for the next round
    return winners, odd_player_out

    winners = []
    print("\nStarting a new round:")
    automatically_advanced_player = None

    # Determine the odd player out and handle the "twice to beat" situation
    if not odd_player_out and len(players) % 2 != 0:
        odd_player_out = random.choice(players)
        players.remove(odd_player_out)
        print(f"{odd_player_out} is the odd player out and will need to win twice in their next match.")
    elif odd_player_out:
        print(f"{odd_player_out} needs to win twice in this round.")
        opponent = random.choice(players)
        players.remove(opponent)
        if conduct_twice_to_beat_match(odd_player_out, opponent):
            winners.append(odd_player_out)
        else:
            winners.append(opponent)
        odd_player_out = None  # Reset for the next round

    # Conduct matches for the remaining players
    while len(players) > 1:
        player1, player2 = players.pop(0), players.pop(0)
        print(f"Match: {player1} vs {player2}")
        winner = input(f"Enter the winner ({player1} or {player2}): ")
        while winner not in [player1, player2]:
            print("Invalid input. Please enter the name of the winner exactly as shown.")
            winner = input(f"Enter the winner ({player1} or {player2}): ")
        winners.append(winner)

    if len(players) == 1:
        # If there's an unpaired player, they automatically advance
        automatically_advanced_player = players[0]
        winners.append(players[0])

    return winners, odd_player_out, automatically_advanced_player


def conduct_twice_to_beat_match(player, opponent):
    for _ in range(2):
        winner = input(f"Enter the winner ({player} or {opponent}): ")
        if winner != player:
            print(f"{opponent} wins the match against the 'twice to beat' player.")
            return False
    print(f"{player} wins twice and advances.")
    return True


def main():
    players = get_player_names()
    random.shuffle(players)
    round_number = 1
    odd_player_out = None

    while len(players) > 1 or odd_player_out:
        print(f"\n--- Round {round_number} ---")
        if odd_player_out:
            print(f"{odd_player_out} advances automatically and will need to win twice in the next match.")

        players, new_odd_player_out = conduct_round(players, odd_player_out)

        # If the odd player out has not won their "twice to beat" match, carry them forward
        odd_player_out = new_odd_player_out if new_odd_player_out else None
        round_number += 1

    # Handle the final round
    if len(players) == 1 and odd_player_out:
        print(f"\nFinal Round: {odd_player_out} must win twice against {players[0]}")
        if not conduct_twice_to_beat_match(odd_player_out, players[0]):
            print(f"The champion is: {players[0]}")
        else:
            print(f"The champion is: {odd_player_out}")
    elif len(players) == 1:
        print(f"\nFinal Round: {players[0]} is the last player standing and is the champion.")
    else:
        # If the loop ended because there's no one left to challenge the odd player out
        print(f"\nFinal Round: {odd_player_out} is the last player standing and is the champion.")

if __name__ == "__main__":
    main()

