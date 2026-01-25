import requests

ML_SERVICE_URL = "http://127.0.0.1:8001/match"

def get_match_score(candidate_text, job_text):
    payload = {
    "resume_text": candidate_text,
    "job_text": job_text
}

    response = requests.post(ML_SERVICE_URL, json=payload, timeout=5)
    response.raise_for_status()

    return response.json().get("score", 0)

    print("ML PAYLOAD:", payload)