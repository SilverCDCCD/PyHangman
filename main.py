import random


auto_show = ["-", "'", ":"]
guessed_letters = []
lives = 7
secret_word = ""
used_words = []
word_repository = [
	# Animals
	"Bullfrog", "Cat", "Chicken", "Cow", "Dog", "Eagle", "Falcon", "Ferret", "Hippopotamus", "Kangaroo", "Koala", "Lion", "Rhinoceros", "Shark", "Tiger", "Tortoise", "Turtle", "Wallaby", "Whale",
	
	# Anime
	"Attack on Titan", "Black Butler", "Black Clover", "Bleach", "Death Note", "Demon Slayer", "Dragon Ball Z", "Fairy Tail", "Food Wars", "Gundam Wing", "Hajime No Ippo", "Inuyasha", "Jojo's Bizarre Adventure", "Kill La Kill", "My Hero Academia", "Naruto", "One Piece", "Parasyte", "Promised Neverland", "Soul Eater", "Yu Yu Hakusho",
	
	# Careers
	"Athlete", "Baker", "Blacksmith", "Butler", "Chef", "Developer", "Doctor", "Exterminator", "Fisherman", "Firefighter", "Innkeeper", "Janitor", "Musician", "Nurse", "Police", "Programmer", "Shopkeeper", "Streamer", "Surgeon", "Trainer",
	
	# Card Games
	"Blackjack", "Fifty-Two Card Pickup", "Go Fish", "Old Maid", "Poker", "Spades", "Uno", "War",
	
	# Cartoon Network
	"Foster's Home For Imaginary Friends", "Mucha Lucha", "Teen Titans",
	
	# Cities
	"Albuquerque", "Amsterdam", "Atlanta", "Berlin", "Cancun", "Kyoto", "Las Vegas", "London", "Los Angeles", "Memphis", "Miami", "New York City", "Okinawa", "Orlando", "Paris", "Quebec", "Tokyo", "Toronto",
	
	# Countries
	"Britain", "China", "France", "Germany", "Ireland", "Japan", "Poland", "Sweden", "Switzerland", "The United Kingdom", "The United States", "Wales",
	
	# DC Comics
	"Aquaman", "Bane", "Batman", "Bruce Wayne", "Clark Kent", "Diana Prince", "Harley Quinn", "Jason Todd", "Martian Manhunter", "Mr. Freeze", "Robin", "Stephanie Brown", "Superman", "The Flash", "The Justice League", "The Joker", "Tim Drake", "Victor Fries", "Wally West", "Wonder Woman",
	
	# Dinosaurs
	"Ankylosaurus", "Brontosaurus", "Dinosaur", "Pterodactyl", "Spinosaurus", "Triceratops", "Tyrannosaurus", "Velociraptor",
	
	# Disney
	"American Dragon: Jake Long", "Hannah Montana", "Kim Possible", "The Suite Life of Zack and Cody",
	
	# Fantasy Animals
	"Dragon", "Fairy", "Griffin", "Leviathan", "Manticore", "Phoenix", "Pegasus", "Pixie", "Quirin", "Unicorn", "Wyvern",
	
	# Foods
	"Apple", "Banana", "Beef", "Blackberry", "Blueberry", "Butter", "Buttermilk", "Cheese", "Coffee", "Milk", "Orange", "Pear", "Pizza", "Potato", "Roast Beef", "Strawberry", "Sweet Potato", "Toast", "Tomato", "Wine", "Yams",
	
	# Literature
	"Frankenstein", "Harry Potter", "Journey to the West", "Lord of the Rings", "Pride and Prejudice", "Sherlock Holmes", "Smaug", "The Hobbit", "Twilight", "War and Peace",
	
	# Marvel
	"Charles Xavier", "Cyclops", "Dark Phoenix", "Gambit", "Havoc", "Jane Foster", "Jean Grey", "Jubilee", "Pietro Maximoff", "Quicksilver", "Rogue", "Scarlet Witch", "Scott Summers", "Spiderman", "Venom", "Wanda Maximoff", "Wolverine", "X-Men",
	
	# Movies
	"Citizen Kane", "Jaws", "Jurassic Park", "Kung Fu Panda", "Shrek", "Star Trek", "Star Wars", "The Shining",
	
	# Mythology/Theology
	"Amaterasu", "Anubis", "Bast", "Hades", "Hercules", "Isis", "Loki", "Odin", "Osiris", "Poseidon", "Sun Wukong", "Thor", "Zeus",
	
	# Nickelodeon
	"Ren and Stimpy", "Spongebob Squarepants", "The Fairly Oddparents",
	
	# Social Media
	"Facebook", "Instagram", "MySpace", "Steam", "TikTok", "Twitch", "Twitter", "YouTube",
	
	# Sports
	"Ballet", "Basketball", "Boxing", "Football", "Formula One", "Golf", "NASCAR", "Pickleball", "Soccer", "Swimming", "Table Tennis", "Tennis", "Water Polo",
	
	# States
	"Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming",
	
	# Video Games
	"BlazBlue", "Dark Souls", "Dead or Alive", "Dig-Dug", "Elden Ring", "Final Fantasy", "Fire Emblem", "Guilty Gear", "Guitar Hero", "Harvest Moon", "Lara Croft", "Legend Of Zelda", "Mario", "Mario Kart", "Megaman", "Pac-Man", "Palworld", "Pokemon", "Sonic the Hedgehog", "SoulCalibur", "Starcraft", "Stardew Valley", "Story of Seasons", "Street Fighter", "Tekken", "Tomb Raider", "Wii Sports", "World of Warcraft", "Yu-Gi-Oh"
]


def check_letter(letter: str):
	global lives
	if letter.upper() in guessed_letters:
		print(f"You've already guessed {letter.upper()}.")
		game_round()
	elif letter.upper() in secret_word.upper():
		guessed_letters.append(letter.upper())
		print(f"{secret_word.upper().count(letter.upper())} {letter.upper()}'s.")
		check_word()
	elif not letter.isalpha():
		print("Please enter a letter.")
		game_round()
	else:
		guessed_letters.append(letter.upper())
		lives -= 1
		print(f"No {letter.upper()}'s. Lives remaining: {lives}.")
		if lives > 0:
			game_round()
		else:
			print(f"You lost your last life! The secret word was {secret_word}.")
			restart_game()


def check_word():
	for letter in secret_word.upper():
		if letter not in guessed_letters:
			game_round()
			return
	print(f"You won! The secret word was {secret_word}.")
	restart_game()


def game_round():
	show_word()
	guess_letter()


def guess_letter():
	letter = input("Guess a letter (Press \"Enter\" to see previous guesses): ")
	validate_letter(letter)


def restart_game():
	restart = input("Would you like to play again? (Y/N) ").upper()
	match restart:
		case "Y" | "YES":
			start_game()
		case "N" | "NO":
			print("Thanks for playing!")
		case _:
			print("Invalid answer")
			restart_game()


def show_word():
	word = ""
	for letter in secret_word:
		if letter.upper() in guessed_letters or letter.upper() in auto_show:
			word += letter
		else:
			word += "_"
	print(word)


def start_game():
	global secret_word, word_repository, guessed_letters, lives
	lives = 7
	guessed_letters.clear()
	if len(secret_word) > 0:
		word_repository.remove(secret_word)
		used_words.append(secret_word)
	if len(word_repository) < 1:
		word_repository = used_words.copy()
		used_words.clear()
	secret_word = random.choice(word_repository)
	game_round()


def validate_letter(letter: str):
	if len(letter) == 0:
		guessed_letters.sort()
		print(f"Guessed Letters: {guessed_letters}")
		game_round()
	elif len(letter) > 1:
		print("Please enter a single letter.")
		game_round()
	else:
		check_letter(letter)


if __name__ == "__main__":
	#start_game()
	print(len(word_repository))
