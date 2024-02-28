from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer


class Fetch:
    def __init__(self, text):
        self.client = QdrantClient(path="Qdrant_db")
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
        self.query_embedding = self.encoder.encode(text)
        self.hits = self.client.search(collection_name="Research_papers", query_vector=self.query_embedding,limit=1)
        self.score = self.hits[0].score
        self.number = self.hits[0].payload["number"]
