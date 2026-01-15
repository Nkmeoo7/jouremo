class Analyzer:
    def emotion_extract(self,text):
        t= text.lower()
        if any(word in t for word in ["sad","fell bad","nesty","not well","cry"]):
            return "sad";
        if any(word in t for word in ["joy","cheerfull","happy","nice", "good ha ji"]):
            return "happy";
        return "neutral"


