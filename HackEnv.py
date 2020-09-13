import gym, os, subprocess
from gym import spaces
import requests
from bs4 import BeautifulSoup

class HackEnv(gym.Env):
    # Enum relating commands to numbers for discrete action space
    # I know it's not an enum but it should be lol
    commands = {
        0: "ls",
        1: "cd",
        2: "cat",
        3: "echo",
        4: "grep"
    }
    """Custom filesystem environment that follows gym interface"""

    """pull text from an HTML file (for finding relevant words that help with finding flags"""
    def news(self):
        # the target we want to open
        url = 'https://pwnable.tw/challenge/#2'

        # open with GET method
        resp = requests.get(url)

        # http_respone 200 means OK status
        if resp.status_code == 200:
            print("Successfully opened the web page")
            print("Flags-\n")

            soup = BeautifulSoup(resp.text, 'html.parser')
            relwords = soup.find("ul", {"class": commands})

            # now we want to print only the text part of the anchor.
            # find all the elements of a, i.e anchor
            for i in l.findAll("a"):
                print(i.text)
        else:
            print("Error")

    news()

    metadata = {render.modes: ['human']}



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