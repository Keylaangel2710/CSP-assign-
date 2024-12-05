def main():
    max_segmnets = 9
    current_loop = 0
    player1_segments = []
    player2_segments = []
    while current_loop < max_segmnets:
        player_number = None
        if current_loop % 2 == 0:
            player_number = 1
        else:
            player_number = 2

        segment = player(player_number)
        while segment > 9 or segment < 1:
            print("please input a vaild segment number")
            segment = player(player_number)

        # Improvement: Check if segment is already taken/filled.
        player_segments = []
        if player_number == 1: 
            player1_segments.append(segment)
            player_segments = player1_segments
        elif player_number ==2:
            player2_segments.append(segment)
            player_segments = player2_segments

        player_won = has_player_won(player_segments)
        if player_won:
            print("Player " + str(player_number) + " has won!")
            break

        current_loop += 1

def player(player_number):
    print("Player " + str(player_number) + " Choose segment from 1 to 9:")
    # Improvement: IF input is not a number, ask again for a valid number.
    segment = int(input())
    return segment

def has_player_won(player_segments):

    # https://stackoverflow.com/questions/20789412/check-if-all-elements-of-one-array-is-in-another-array/20789587#20789587
    player_won = False
    if set([1, 2, 3]).issubset(player_segments):
        player_won = True
    elif set([4,5,6]).issubset(player_segments):
        player_won = True
    elif set([7,8,9]).issubset(player_segments):
        player_won = True
    elif set([1,4,7]).issubset(player_segments):
        player_won = True
    elif set([2,5,8]).issubset(player_segments):
        player_won = True
    elif set([3,6,9]).issubset(player_segments):
        player_won = True
    elif set([1,5,9]).issubset(player_segments):
        player_won = True
    elif set([3,5,7]).issubset(player_segments):
        player_won = True

    return player_won
    
main()
