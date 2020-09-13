import gym, os, subprocess
from gym import spaces

class HackEnv(gym.Env):
    """Custom filesystem environment that follows gym interface"""

    metadata = {render.modes: ['human']}

    # Enum relating commands to numbers for discrete action space
    commands = {
        0 : "ls",
        1 : "cd",
        2 : "cat",
        3 : "echo",
        4 : "grep"
    }

    # Initialize registers
    location, directory, filename, string = "","","",""

    def __init__(self):
        super(HackEnv, self).__init__()

        # Action space: 5 commands
        self.action_space = spaces.Discrete(5)

        # Observation space: Flag, error, directory, filename, string
        self.observation_space = spaces.Discrete(5)


    def step(self, action):

        # Execute command with given parameters
        os.system(*action)

        # Interpret stdout
        result = read_stdout()

        # Observation of new state as dictionary of registers
        # Choose new values of currently location and currently held parameters
        # Check type of console output and update relevant registers
        #   If given list of outputs, choose one at random
        observation = {
            location : "",
            directory : "",
            filename : "",
            string : ""
        }
        done = false

        # Calculate reward
        reward = 0
        if result:
            if result.contains("flag.txt"):
                reward = 50
                done = true
            elif result.contains("error"):
                reward = -10
            else:
                reward = len(result) * 3

        return observation, reward, done, {}

    def reset(self):
        location, directory, filename, string = "","","",""
        return observation

    def render(self):
        pass

    def close(self):
        pass

    # Read one line from stdout as a list of parameters
    def read_stdout(self):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return str.split(p.stdout.readline())