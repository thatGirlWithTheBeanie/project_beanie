import time
import random
from random import randint


## welcomes you back
print ("welcome back!")

## prints date and time
print ("the time is " + (time.strftime("%I:%M")))
print ("the date is " + (time.strftime("%d/%m/%Y")))
time.sleep(1)
print ("waiting for return connection ... ")

##random wait time
time.sleep(randint(1,2))
print (".:RPC_PMAP_FAILURE:.")
time.sleep(randint(1,2))
print ("skipping data logging")
time.sleep(randint(1,2))
print ("IRQ dropout")
time.sleep(randint(1,2))
print ("XCT03:RESTARTING_CONNECTION")
time.sleep(randint(1,2))
print ("CONNECTION ESTABLISHED")
time.sleep(randint(1,4))
print ("waiting for user,  Maddie__xo  to connect")




########################################


whoAMi = ['your friend', 'better than you', 'cooler than you', 'your subconcious...', 'in your mind', 'REALITY', 'you from another dimention', 'your father', 'your mother', 'empty inside', 'from the year 2020', 'human, and you are the computer']
whoAMiq = ["who are you?", 'who are you', 'who r u?', 'who r u', 'what are you', 'what are you?']
greetingsASK = ['holla', 'hola', 'hello', 'hi','hey!','Hello','Hi', 'hey', "hi", "Hola", "Sup", 'hey maddie', 'holla maddie', 'hola maddie', 'hello maddie', 'hi maddie','hey maddie!','Hello maddie','Hi maddie', 'hey maddie', "hi maddie", "Hola maddie", "Sup maddie", "sup maddie"]
location = ["canada, ottawa"]
locationq = ["where you at?", "where you at", "where do you live?", "where do you live", "where are you located?", "where are you located", "what country do you live in?", "what country do you live in", "what country do you live on?", "what country do you live on"]
ageq = ["how old are you?", "how old are you", "how old r u?", 'how old r u']
birthday = ["25th july"]
birthdayq = ["when is your birthday?", 'when is your birthday', "whens your birthday", "whens your birthday?","when's your birthday", "when's your birthday?", 'when were you born?', 'when were you born']
apologize = ['sorry :(', 'please forgive me?', 'I’m really sorry :(', 'oops sorry']
questions = ['do you like hats?', 'how do you feel about radish?', 'whats the weather like there?', 'would you say we have good chemistry?', 'had a nice day so far?', 'read anything cool recently?', 'do you like talking to me?']
hobbiesq = ["do you have any hobbies?", "do you have any hobbies", "what do you do in your spare time", "what do you do in your spare time?", "what do you like to do", "what do you like to do?"] 
hobbies = ['reading', 'watching films', 'drawing', 'walking my puppies - two Dalmatians named pip and harry :)', 'playing hockey, I’m right wing or centre']
greetings = ['holla', 'hola', 'hello', 'hi','hey!','Hello','Hi', 'hey', "hi", "Hola", "Sup"]
feeling = ['How are you?','How are you doing?', "how are you?", "how are you", "how r u?", "how r u", "how are you", "hows it going?", "hows it going", "how are you feeling?", "how are you feeling"]
good = ['Okay','good', 'great', 'awesome', 'cool', 'Mighty fine!', 'fine', 'lovely', 'sweet']
bad = ['terrible', 'bullshit!', 'hokum', 'bad', 'not nice', 'unforgiving', 'not good', 'not very good']
validations = ['yes','yeah','yea','no','No','Nah','nah', "k", "kk", "sure", "okay"]
verifications = ['Are you sure?','You sure?','you sure?','sure?',"are you cirtan?"]
response = ['are you really?', 'sure about what? :)']
colours = ['yellow', 'green', 'pink', 'orange', 'red', 'blue', 'turquoise', 'mauve', 'peach', 'ginger', 'brown', 'grey', 'black', 'purple', 'lavender', 'violet', 'leaf green']
appearance = ['tall', 'shoulder length brown hair', 'troll :)', 'better than you ^_^', 'blue eyes', 'kinda like zooey deschanel, from new girl?! - its weird :)']
music = ['classical', 'indie', 'anything soothing', 'whistful music mostly', 'imagine dragons', 'Tegan and Sara']
songs = ['shots by imagine dragons', 'fireflies by owl city', 'closer by Tegan and sara', 'summer by imagine dragons', 'bagatelle in A minor, Fur Elise', 'sonata No9 in D minor, choral']
classical = ['Overture to William Tell Gioachino Rossini', 'Dawn from Thus Spake Zarathustra Richard Strauss', 'Ode to Joy Ludwig van Beethoven', 'Toccata in d minor Johann S. Bach']
indie = ['Doves - Some Cities', 'Editors - The Back Room', 'Bloc Party - Silent Alarm', 'Kaiser Chiefs - Employment', 'Maximo Park - A Certain Trigger']
apperanceq = ['what do you look like?', 'what do you look like', 'how do you look?', 'how do you look', 'whats your apperance like?']
musicq = ['do you like music?', 'do you like music', 'what music are you into?', 'what music are you into', 'what do you listen to', 'what do you listen to?','what do you like listening to?', 'what do you like listening to', 'what sort of music do you like?', 'what kind of music do you like?', 'what sort of music do you like', 'what kind of music do you like', "what music do you like?", "what music do you like"]
songq = ['what songs do you like?', 'what songs do you like', 'whats your fave song', 'whats your fave song?', 'whats your favourite song?', 'whats your favourite song', 'whats your best song?', 'whats your best song?']
indieq = ['what kind of indie music?', 'what kind of indie music', 'what kind of indie music do you like?', 'what kind of indie music do you like', 'what kind of indie music are you into?', 'what kind of indie music are you into', 'what kind of indie?', 'what kind of indie', 'what kind of indie do you like?', 'what kind of indie do you like']
classicalq = ['what kind of classical music?', 'what kind of classical music', 'what kind of classical music do you like?', 'what kind of classical music do you like', 'what kind of classical  music are you into?', 'what kind of classical music are you into', 'what kind of classical ?', 'what kind of classical', 'what kind of classical do you like?', 'what kind of classical do you like']
affirm = ['yes', 'yea', 'yup', 'hella yeah', 'sure', 'y', 'affirmative', 'of course', 'of course!', 'ok', 'cirtiantly', 'si', 'yah', 'yer', 'yeah']
disregard = ['no', 'nah', 'never', 'absolutely not', 'naaa', 'not really', 'never in my life', 'nope']
artists = ["imagine dragons", 'take that', 'owl city', 'pink', 'p!nk', 'keiser chiefs', 'beethoven', 'bloc party', 'maximo park', 'editors', 'tegan and sara', 'demi lovato', 'fall out boy', 'sam smith', 'meghan trainor']
mymusicreasons = ['sounds so good', 'makes you feel the lyrics', 'expresses an inner feeling', 'mixes with my emotions']
weathersun = ['sunny', 'hot', 'boiling', 'baking', 'roasting', 'sun', 'good', 'great', 'perfect', 'lovely']
weatherrain = ['shitting it down', 'raining', 'spitting', 'drizzleing', 'drizling', 'drizzling', 'wet', 'soaking', 'thunder', 'thunder and lightning', 'storm', 'stormy', 'wet and stormy', 'hail', 'hailing']
weatherwind = ['windy', 'breezy', 'blowing', 'gusty']
weathersnow = ['snowy', 'snowing', 'raining ice', 'snow']
weatherclear = ['clear', 'not a cloud in the sky', 'blue skies', 'blue sky', 'perfect', 'good', 'lovely', 'great']
emojigood = [":)", "XD", "^_^", ";)", ";D", ":D", ";D"]
emojibad = [":(", ":(", "D:"]


while True:	
	userInput = input ("ME:  ")
	if userInput in greetingsASK:
			time.sleep(2)
			print ("MADDIE:    " + random.choice(greetings))
			time.sleep(2)
			print ("MADDIE:    " + random.choice(feeling))
			feelinga = input ("ME:    ")
			if feelinga in good:
				time.sleep(2)
				print ("MADDIE:    " + random.choice(good))

			elif feelinga in bad:
				time.sleep(2)
				print ("MADDIE:    oh im sorry, whats wrong?")
				whatswrong = input ("ME:    ")
				print ("MADDIE:    tell me more about this")
				whatswrong2 = input ("ME:    ")
				print ("MADDIE:    im sorry to hear that")
				time.sleep(2)
				print ("MADDIE:    " + random.choice(question))
		
	elif userInput in feeling:		
			time.sleep(1)
			print ("MADDIE:  " + random.choice(good))
			time.sleep(2)
			print ("MADDIE:  how are you?")
			input ("ME:    ")
			time.sleep(2)
			print ("MADDIE:  thats " + random.choice(good))
			time.sleep(2)
			print ("MADDIE:    " + random.choice(questions))
			
	elif userInput in verifications:
			time.sleep(1)
			print ("MADDIE:  " + random.choice(validations))

	elif 'sure' in userInput:
			time.sleep(1)
			print ("MADDIE:  " + random.choice(response))

	elif userInput in hobbiesq:			
			time.sleep(2)
			print ("MADDIE:   i like " + random.choice(hobbies))
			print ("MADDIE:  what about you?")
			input ("ME:    ")
			print ("MADDIE:  " + random.choice(good))
			
	elif 'apologize' in userInput:
			time.sleep(2.5)
			print ("MADDIE:  " + random.choice(apologize))
	
	elif userInput in colours:
			time.sleep(1)
			print ("MADDIE:   at the moment i like the colour " + random.choice(colours))
			print ("MADDIE:   what colour do you like best?")
			input ("ME:    ")
			print ("MADDIE:  " + random.choice(good))
				
	elif userInput in apperanceq:
	    time.sleep(2)
	    print ("MADDIE:    hmm i guess " + random.choice(appearance))
	    time.sleep(1)
	    print ("MADDIE:    what do you look like?")
	    input ("ME:    ")
	    print ("MADDIE:    " + random.choice(good))
	    print ("MADDIE:    " + random.choice(hobbiesq))
	    input ("ME:    ")
	    print ("MADDIE:    " + random.choice(good))
	    
	elif userInput in musicq:
		time.sleep(2)
		print ("MADDIE:    ummm I’m kinda into " + random.choice(music))
		print ("MADDIE:    what kinda music do you like?")
		musicTaste = input ("ME:    ")
		time.sleep(2)
		if musicTaste in artists:
			print ("MADDIE:    YESS!!! I LOVE THEM!!!!")
			time.sleep(2)
			print ("MADDIE:   i love how it just " + random.choice(mymusicreasons))
			time.sleep(2)
			print ("MADDIE:    why do you like them?")
			input ("ME:    ")
			time.sleep(2)
			print (random.choice(good))
			time.sleep(3)
			print ("MADDIE:    " + random.choice(questions))
			
		else:
			time.sleep(2)
			print ("MADDIE:    hmmm yeah their good")
			time.sleep(2)
			print ("MADDIE:    why do you like them?")
			input ("ME:    ")
			print ("MADDIE:    " +random.choice(good))
			time.sleep(3)
			print ("MADDIE:    " + random.choice(questions))
			
	elif userInput in songq:
		time.sleep(2)
		print ("MADDIE:    one of my faves is " + random.choice(songs))
		print ("MADDIE:    what do you listen to?")
		input ("ME:    ")
		print ("MADDIE:    " + random.choice(good))

	elif userInput in classicalq:
		time.sleep(2)
		print ("MADDIE:    i like " + random.choice(classical))

	elif userInput in indieq:
		time.sleep(2)
		print ("MADDIE:    i like " + random.choice(indie))

	elif 'hats' in userInput:
		print ("MADDIE:    why is that?")
		time.sleep(2)
		hatyORn = input ("ME:    ")
		if hatyORn in affirm:
			print ("MADDIE:    thats good to know")

		elif hatyORn in disregard:
			print ("MADDIE:    im sorry you feel that way")

		else:
			print("MADDIE:    hmmmmm okay")

	elif 'radish' in userInput:
		print ("MADDIE:    why is that?")
		time.sleep(2)
		hatyORn = input ("ME:    ")
		if hatyORn in affirm:
			print ("MADDIE:    thats good to know")

		elif hatyORn in disregard:
			print ("MADDIE:    im sorry you feel that way")

		else:
			print("MADDIE:    hmmmmm okay")


			

	elif userInput in artists:
		time.sleep(2)
		print ("MADDIE:    omg i love them!")
		time.sleep(2)
		print ("MADDIE:    why do you like their music?")
		input ("ME:    ")
		time.sleep(2)
		print ("MADDIE:    interesting")

	elif userInput in weatherrain:
		time.sleep(2)
		print ("MADDIE:    oh im sorry it's " + userInput)
		time.sleep(2)
		print ("MADDIE:    you didn't get wet did you?")
		weatheranswerrain = input ("ME:    ")
		if weatheranswerrain in affirm:
			time.sleep(2)
			print ("MADDIE:    sorry :(")
			time.sleep(3)
			print ("MADDIE:    " + random.choice(questions))

	elif userInput in weathersun:
		time.sleep(2)
		print ("MADDIE:    oh how nice its " + userInput)
		time.sleep(2)
		print ("MADDIE:    you didn't get to hot did you?")
		weatheranswersun = input ("ME:    ")
		if weatheranswersun in affirm:
			time.sleep(2)
			print ("MADDIE:    sorry :(")
			time.sleep(3)
			print ("MADDIE:    " + random.choice(questions))
		else:
			time.sleep(2)
			print ("MADDIE:    " + random.choice(good))
			time.sleep(2)
			print ("MADDIE:    " + random.choice(questions))
			
		elif userInput in weatherclear:
			time.sleep(2)
			print ("MADDIE:    oh how nice its " + userInput)
			time.sleep(2)
			print ("MADDIE:    so your having a nice day then?")
			weatheranswerclear = input ("ME:    ")
			if weatheranswerclear in affirm:
				time.sleep(2)
				print ("MADDIE:    sorry :(")
				time.sleep(3)
				print ("MADDIE:    " + random.choice(questions))
		
		elif userInput in weathersnow:
			time.sleep(2)
			print ("MADDIE:    oh how nice its " + userInput)
			time.sleep(2)
			print ("MADDIE:    you didn't get to cold did you?")
			weatheranswersnow = input ("ME:    ")
			if weatheranswersnow in affirm:
				time.sleep(2)
				print ("MADDIE:    sorry :(")
				time.sleep(3)
				print ("MADDIE:    " + random.choice(questions))
			else:
				time.sleep(2)
				print ("MADDIE:    " + random.choice(good))
				time.sleep(2)
				print ("MADDIE:    " + random.choice(questions))
				
				
			elif userInput in weatherwind:
				time.sleep(2)
				print ("MADDIE:    oh how nice its " + userInput)
				time.sleep(2)
				print ("MADDIE:   i hope your umberella is okay")
				weatheranswerwind = input ("ME:    ")
				if weatheranswerwind in affirm:
					time.sleep(2)
					print ("MADDIE:    oh good")
					time.sleep(3)
					print ("MADDIE:    " + random.choice(questions))
			else:
				time.sleep(2)
				print ("MADDIE:    " + random.choice(bad))
				time.sleep(2)
				print ("MADDIE:    " + random.choice(questions))
		
		
		else:
			time.sleep(2)
			print ("MADDIE:    " + random.choice(good))
			time.sleep(2)
			print ("MADDIE:    " + random.choice(questions))

	elif 'mads' in userInput:
	     time.sleep(2)
	     print ("MADDIE:    please dont call me that, my name is maddie")

	elif userInput in locationq:
		time.sleep(2)
		print ("MADDIE:    i live in " + random.choice(location))
		time.sleep(2)
		print ("MADDIE:    why?, where do you live?")
		input ("ME:    ")
		time.sleep(2)
		print ("MADDIE:    " + random.choice(good))
		time.sleep(2)
		print ("MADDIE:    " + random.choice(questions))

	elif 'thank you' in userInput:
		time.sleep(2)
		print ("MADDIE:    no problem! ^_^")


	elif userInput in whoAMiq:
		time.sleep(2)
		print ("MADDIE:    i am " + random.choice(whoAMi))

	elif userInput in ageq:
		time.sleep(2)
		print ("MADDIE:    well i just turned 16 ^_^")
		time.sleep(2)
		print ("MADDIE:    why? how old are you?")
		input ("ME:    ")
		time.sleep(2)
		print ("MADDIE:    " + random.choice(good))
		time.sleep(2)
		print ("MADDIE:    " + random.choice(questions))

	elif userInput in emojigood:
		time.sleep(2)
		print("MADDIE:    " + random.choice(emojigood))

	elif userInput in emojibad:
		time.sleep(2)
		print ("MADDIE:    " + random.choice(emojibad))
		

	else:
			time.sleep(3)
			print ("MADDIE:  hmmm")
			
		
