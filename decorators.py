
#decorators.py https://habrahabr.ru/post/141411/

def shout(word="yes"):
    return word.capitalize()+"!"
 
#print shout()


scream=shout()
print scream


#print shout
print scream



def talk():
 
    def whisper(word="no"):
        return word.lower()+"...";
 
    
    print whisper()
    return "Pasha"

print talk()

crick = shout()
print crick