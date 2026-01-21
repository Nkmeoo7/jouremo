#journal class make
from analyzer import Analyzer
from storage import Storage
from datetime import datetime
from reflection import Reflection


class Journal:
    def __init__(self):
        self.analyzer= Analyzer()
        self.storage= Storage()
        self.reflection=Reflection()

    def add_entry(self,text):
        emotion = self.analyzer.emotion_extract(text)

        created_at=datetime.now().isoformat()


        self.storage.save_entry(text,emotion,created_at)

        return {
                "text":text,
                "emotion":emotion,
                "created_at": created_at
                }


    def fetch_emotion(self,emotion):
        entries= self.storage.fetch_by_emotion(emotion)
        return entries 
    

    def fetch_all_entries(self):
        return self.storage.fetch_all()
     

    def fetch_latest(self, limit:int=10):
        return self.storage.fetch_latest(limit)
    
    def reflect(self):
       entries= self.storage.fetch_all()
       common_emotion=self.reflection.most_common_emotion(entries)


    
    
