from collections import Counter

class Reflection:
    def most_common_emotion(self,entries):
        #check if entries list is empty
        if(len(entries)==0):
            return "no emotion are found"
        #geting the emotion from the entries
        emotions=[ entry[1] for entry in entries]
        #emotions the most we geting
        top_emotions= Counter(emotions).most_common(1)[0]
        print(top_emotions)
