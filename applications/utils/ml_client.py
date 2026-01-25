import requests

ML_SERVICE_URL = "http://127.0.0.1:8001/match"


def get_match_score(resume_text: str, job_text: str) -> float:
    payload = {
        "resume_text": resume_text,
        "job_text": job_text,
    }

    response = requests.post(ML_SERVICE_URL, json=payload, timeout=10)
    response.raise_for_status()

    return response.json()["match_score"]
