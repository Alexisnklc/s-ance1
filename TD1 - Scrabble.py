points={'a':1, 'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'d':2,'g':2,'m':2,'b':3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10, "?":0}

with open("C:\\Users\\couch\\OneDrive\\Bureau\\programmation et structures de données\\mots.sansaccent.txt", "r") as file:
    words=file.read().split("\n")

def is_valid(word, tirage):
    copie_tirage=tirage.copy()
    joker=False #pour exercice 4
    for letter in word:
        if letter in copie_tirage:
            copie_tirage.remove(letter)
        elif '?' in copie_tirage and not joker:#pour exercice 4
            copie_tirage.remove('?')#pour exercice 4
            joker=True #pour exercice 4
        else:
            return False
    return True


def word_list(tirage):
    if type(tirage)==str:
        tirage=list(tirage)
        print(tirage)
    mots=[]
    for word in words:
        if is_valid(word, tirage):
            mots.append(word)
    return mots#liste de mots possibles avec le tirage

def longest_word(word_list):
    return max(word_list, key=len)

def score(word):
    score=0
    for letter in word:
        score+=points[letter]
    return score

def max_score(word_list):
    best_word=""
    best_score=0
    for word in word_list:
        if score(word)>best_score:
            best_score=score(word)
            best_word=word
    return (best_word, best_score)

#tirage ='zxcvrrt?'
#print(max_score(word_list(tirage)))
#print (max_score(['rte', 'ver', 'ce', 'etc', 'cet', 'ex', 'cr', 'et', 'ter', 'te', 'ct']))



