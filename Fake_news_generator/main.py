import random

subjects = [
    "raju the failed engineering topper",
    "pappu who still thinks 5G spreads corona",
    "sharma ji ka beta",
    "a goat wearing sunglasses",
    "prime minister of panipuri association",
    "baba who sells WiFi data as prasad",
    "a dog who failed UPSC 7 times",
    "gupta ji ki aunty with 3 powerbanks",
    "the great khali ordering chai",
    "uncle who forwards good morning messages",
    "rickshaw driver who only accepts bitcoin",
    "the last benched coder from India"
]

actions = [
    "caught dancing with",
    "eating 200 plates of",
    "sleeping inside",
    "throwing chappals at",
    "riding without helmet on",
    "launching startup of",
    "playing kabaddi with",
    "fighting 3 hours about",
    "crying loudly for",
    "proposing to",
    "leaking exam paper of",
    "doing yoga with",
    "arguing on whatsapp about"
]

indian_places_or_things = [
    "burnt samosa",
    "broken cricket bat",
    "2-rupee Maggi",
    "dustbin full of chai",
    "donkey with gold chain",
    "traffic police whistle",
    "expired ketchup bottle",
    "tandoori momo with extra mayonnaise",
    "railway announcement speaker",
    "panipuri water tanker",
    "Modi’s 56-inch kurta",
    "Ambani’s jio sim card",
    "government job rejection letter",
    "engineering backlog paper"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    indian_places_or_thing = random.choice(indian_places_or_things)

    headline = f"{subject} {action} {indian_places_or_thing}"

    print("\n🤣 Today's morning Headlines are as follows:", headline)

    n = input("\nDo you want to read another headline? (yes/no): ").strip().lower()
    if n == "no":
        break

