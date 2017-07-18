start_input = input("You're on a walk with your dog when he randomly begins to bark at a bush about 15 feet away that sits at the start of a forest trail. You ignore it but as you pass by the bush, you hear rustling... do you walk towards the bush? (Y or N) ")

if start_input == "Y" or start_input == "y":
    Yes_input = input("Your dog gets loose from you and runs down into the forest trail. Do you: 1) follow him in and try to get him or 2) wait at the bush for him to return?")
    if Yes_input == "1":
        print("You walked in and tried shouting his name to call him back to you. You awoke a monster living in the forest and you were killed. GAME OVER.")
    if Yes_input == "2":
        print("Your dog eventually came back about 10 minutes later but he was wounded. You selfishly chose your safety over his. Game over!")

if start_input == "N" or start_input == "n":
    No_input = input("As you walk away, you look back to see a masked man running towards you. You can either: A) run away and try to make it home safely or B) go towards the man and confront him. ")
    if No_input == "A" or No_input == "a":
        print("As you were running, you tripped over your dog's leash and fell. The man caught up to you while you were down and killed you. GAME OVER.")
    if No_input == "B" or No_input == "b":
        print("Your dog has been trained ever since he was a puppy to guard his owners. He can sense danger and was cued to bite the man. You're free!")
