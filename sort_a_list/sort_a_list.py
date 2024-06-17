
text = '''
sister	semester	sometimes	someone	something	some	science	students
strategies 	stories	specialize	software	situation	son	studying	say
sport	successful	spoken 	skills	social	short	speaking	simple
sentences	several	small	since	started	school	since	seen
situated	significance	significant	several	sun	spend	schedule	sleep
said	spiritualities	shopping 	see	snack	set	stress	sailing
smaller	scotland	so	share	site	sure	sounds	station
sick	same	sea	stop	ship	safety	systems	
'''

 # Split the text into a list of words
words = text.split()

# Sorting the list using sort()
words.sort()
words = " ".join(words)
print(words)