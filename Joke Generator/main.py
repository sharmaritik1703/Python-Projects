from random import choice

jokes = ["Sarcasm,because Murder is illegal", "I use sarcasm as defense against Stupidity",
         "Life is a race so be a racist",
         "As I get older, I remember all the people I lost along the way. Maybe my budding career as a tour guide was "
         "not the right choice",
         "What does my dad have in common with Nemo? They both can’t be found",
         " My wife is mad that I have no sense of direction. So I packed up my stuff and right",
         "What's red and bad for your teeth? A brick",
         "I have many jokes about unemployed people—sadly none of them work",
         " I threw a boomerang a few years ago. I now live in constant fear",
         "I made a website for orphans. It doesn’t have a home page",
         "“I’m sorry” and “I apologize” mean the same thing. Except at a funeral",
         "My grandma has the heart of a lion and a lifetime ban from the zoo",
         "Today was the worst day of my life. My ex got hit by a school bus, and I lost my job as a bus driver",
         "The cemetery is so crowded. People are just dying to get in",
         "Cremation. My final hope for a smoking’ hot body!"]

print("Welcome to Joke Generator: ")

mode_is_on = True

while mode_is_on:
    joke = choice(jokes)
    print(joke)

    prompt = input("Do you want to generate joke again? (y/n): ")

    if prompt == "n":
        mode_is_on = False
    elif prompt == "y":
        pass
    else:
        raise ValueError("Enter a valid prompt!")
