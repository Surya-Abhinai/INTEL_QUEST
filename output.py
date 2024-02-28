from Extract_User import TextExtractor
from Fetch_Score import Fetch
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer


class Output :

    def __init__(self,file_path):
        self.client = QdrantClient(path="Qdrant_db")
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
        self.script = self.get_the_text(file_path)
        self.output = self.fn(self.script)



    def get_the_text(self,file_path):
        script = TextExtractor(file_path).text
        return script


    def colorize(self,text, color):
        color_codes = {
            'red': '\033[31m',
            'green': '\033[32m',
            'blue': '\033[34m',
            'reset': '\033[0m',
        }

        return f"{color_codes[color]}{text}{color_codes['reset']}"


    def fn(self,script):
        final_string = ""
        final_score = 0
        split_sentences = script.split(".")
        val = len(split_sentences)
        for i in split_sentences:
            temp = Fetch(i, self.client, self.encoder)
            score = temp.score
            id = temp.number
            final_score += score
            if score > 0.7:
                st = self.colorize(i, 'red')
                final_string += f"{i}., id = {id}\n"
            else:
                final_string += f"{i}.\n"

        final_score /= val
        final_score *= 100
        return final_string, final_score