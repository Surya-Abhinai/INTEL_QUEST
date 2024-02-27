from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from Extract_User import TextExtractor

client = QdrantClient(path="Qdrant_db")
encoder = SentenceTransformer("all-MiniLM-L6-v2")

script = TextExtractor("Framework_for_Bank_Loan_Re-Payment_Prediction_and_Income_Prediction.pdf").text

val = len(script)
for i in range(int(val/100)):
    query_embedding = encoder.encode(script[i*100:(i+1)*100])
    hits = client.search(collection_name="Research_papers", query_vector=query_embedding,limit=1)
    print(i, [hits[0].score, hits[0].payload['number']])
