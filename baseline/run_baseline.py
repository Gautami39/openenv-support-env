import requests

BASE="http://localhost:7860"

requests.post(
    f"{BASE}/reset",
    json={"task_id":"easy_password_reset"}
)

requests.post(
    f"{BASE}/step",
    json={
        "action_type":"reply",
        "message":"reset password"
    }
)

score=requests.get(f"{BASE}/grader")

print(score.json())