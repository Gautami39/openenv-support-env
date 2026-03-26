class SupportEnv:

    def __init__(self):
        self.task = None
        self.state = {}
        self.done = False

    def reset(self, task_id):

        self.task = task_id

        self.state = {
            "conversation": [],
            "resolved": False
        }

        self.done = False

        return self.state

    def step(self, action):

        msg = action["message"].lower()

        self.state["conversation"].append(msg)

        reward = 0.0

        if self.task == "easy_password_reset":

            if "reset password" in msg:
                reward = 1.0
                self.state["resolved"] = True
                self.done = True
            else:
                reward = 0.2

        if self.task == "medium_refund_request":

            if "refund" in msg:
                reward = 1.0
                self.state["resolved"] = True
                self.done = True
            else:
                reward = 0.3

        if self.task == "hard_connection_issue":

            if "restart router" in msg:
                reward = 1.0
                self.state["resolved"] = True
                self.done = True
            else:
                reward = 0.4

        return {
            "state": self.state,
            "reward": reward,
            "done": self.done
        }

    def get_state(self):
        return self.state