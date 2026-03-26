# OpenEnv Support Environment

## Overview

This project implements a simple customer support simulation environment following the OpenEnv specification.
The environment simulates support interactions where an agent must resolve user issues through a sequence of actions.

The environment exposes an API built with FastAPI and is deployed using Docker.

## Tasks

The environment includes three tasks with increasing difficulty:

**Easy Task**

* Resetting a user's password.

**Medium Task**

* Troubleshooting a login issue.

**Hard Task**

* Resolving a billing dispute.

Each task is evaluated by a grader which returns a score between **0.0 and 1.0**.

## Observation Space

The observation returned by the environment contains:

* conversation: List of messages exchanged between the user and support agent
* resolved: Boolean indicating whether the issue has been resolved

Example:

{
"conversation": ["User: I cannot log in", "Agent: Please reset your password"],
"resolved": false
}

## Action Space

Each step requires an action containing:

* message: Response from the support agent

Example:

{
"message": "Please reset your password using the forgot password link."
}

## API Endpoints

**POST /reset**

* Starts a new episode for a given task.

**POST /step**

* Sends an agent action and updates the environment state.

**GET /state**

* Returns the current environment state.

**GET /tasks**

* Lists available tasks and their action schemas.

**POST /grader**

* Returns the score for the completed episode.

**POST /baseline**

* Runs the baseline inference script and returns scores.

## Running Locally

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn app.main:app --host 0.0.0.0 --port 7860

Open API documentation:

http://localhost:7860/docs

## Docker Deployment

Build the container:

docker build -t openenv-support-env .

Run the container:

docker run -p 7860:7860 openenv-support-env

## Baseline

A baseline inference script is included in:

baseline/run_baseline.py

It runs through the tasks and produces reproducible scores.
