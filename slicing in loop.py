my_players = ['mbappe', 'neymar', 'dimaria', 'ronaldo']
my_friendplayers = my_players[:]
my_players.append("cavani")
my_friendplayers.append("sualez")
print("my favorite players are:")
for player in my_players:
    print("\t\t\t" + player)
print(my_players)
print("\n")
print("my friend's favorite players are:")
for friend_p in my_friendplayers:
    print("\t\t\t" + friend_p)
print(my_friendplayers)
