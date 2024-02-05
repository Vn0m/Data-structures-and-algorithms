# define the hash, can also use dict()
voted = {}

def checkVoter(name):
    # check if a name is on the hash and if true it means that person alr voted
    if voted.get(name):
        print("Already voted!")
    else:
        # else add the name to the hash and let the person vote
        voted[name] = True
        print("Let him vote")


checkVoter("mike")
checkVoter("tom")
checkVoter("tom")