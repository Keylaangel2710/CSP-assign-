def main():
    # max_segmnets = 9
    max_segmnets = 2
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

        if player_number == 1: 
            player1_segments.append(segment)
        elif player_number ==2:
            player2_segments.append(segment)
        current_loop += 1 
    # player_number = 1
    # segment = player(player_number) 
    # print(segment)

def player(player_number):
    print("Player " + str(player_number) + " Choose segment from 1 to 9:")
    segment = int(input())
    return segment

def has_player_won(player1_segment, player2_segment):
    pass 
    
main()
