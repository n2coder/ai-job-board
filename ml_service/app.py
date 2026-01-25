from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Initialize FastAPI app
app = FastAPI(title="Resume Job Matching Service")


# Load model once at startup
model = SentenceTransformer("all-MiniLM-L6-v2")


# Request schema
class MatchRequest(BaseModel):
    resume_text: str
    job_text: str


# Response schema
class MatchResponse(BaseModel):
    match_score: float


@app.post("/match", response_model=MatchResponse)
def match_resume_to_job(request: MatchRequest):
    """
    Compute semantic similarity between resume and job description
    """
    texts = [request.resume_text, request.job_text]

    embeddings = model.encode(texts)
    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return {
        "match_score": round(float(similarity * 100), 2)
    }
