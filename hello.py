import random
from pettingzoo.classic import tictactoe_v3

# Hello world example with the tic tac toe environment
# Chooses randomly


env = tictactoe_v3.env()

actions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ep_no = 0
total_episodes = 5

def policy(observation):
    illegal = True
    while illegal:
        action = random.choice([a*b for a,b in zip(actions,observation['action_mask'])])
        if action != 0:
            illegal = False
    return action - 1


while ep_no <= total_episodes:
    print(f"---------------------Starting Episode {ep_no}---------------------")
    env.reset()
    for agent in env.agent_iter():
        observation, reward, done, info = env.last()
        action = policy(observation) if not done else None
        env.step(action)
        env.render()
    ep_no += 1
