from fastapi import FastAPI
from app.env import SupportEnv
from app.models import ResetRequest, Action
from app.tasks import tasks
from app.grader import grade

app = FastAPI()

env = SupportEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset(req: ResetRequest):
    return env.reset(req.task_id)

@app.post("/step")
def step(action: Action):
    return env.step(action.dict())

@app.get("/state")
def state():
    return env.get_state()

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/grader")
def grader():
    return {"score": grade(env)}

@app.get("/baseline")
def baseline():

    env.reset("easy_password_reset")

    env.step({
        "action_type": "reply",
        "message": "please reset password"
    })

    score = grade(env)

    return {"baseline_score": score}