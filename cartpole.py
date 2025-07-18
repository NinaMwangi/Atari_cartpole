import gymnasium as gym
import time

# Inclass Activity...

env = gym.make("CartPole-v1", render_mode="human")
obs, info = env.reset()

done = False
step_count = 0
max_steps = 100000

while not done and step_count < max_steps:
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
    step_count += 1

    print(f"Step: {step_count}, Action: {action}, Reward: {reward}, State: {obs}")

    time.sleep(0.10)  

env.close()
