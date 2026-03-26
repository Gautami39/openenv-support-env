def grade(env):

    if "resolved" not in env.state:
        return 0.0

    if env.state["resolved"]:
        return 1.0

    return 0.0