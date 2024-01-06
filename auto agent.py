# THIS ONLY WORKS IF YOUR RESOLUTION IS 1920x1080 because of how the lock button section works. (could possibly work with other resolutions but have not checked and wont check)

#imports // pyautogui for clicking on agent and taking screenshot of screen
import pyautogui


def main():


    try:

        #locates where the agent is located on the screen // only valid if 90% accurate
        agent_location = pyautogui.locateOnScreen(f"agents/{agent}", confidence=0.9)

        #x and y coordinates of the agents location (top left coords)
        x = agent_location.left
        y = agent_location.top

        #clicks where the agent is to select the agent
        selector = pyautogui.click(x, y)

        #position of the Lock In button to lock the agent in
        lockX = 923
        lockY = 746

        #Click the lock in button
        lockIN = pyautogui.click(lockX, lockY)

    #if an error/exception occurs it just restarts main() and continues to search for the agent on the screen and select it
    except:
        main()


#select what agent you want
agent = str(input("Select your agent: "))

#adding .png to end of the agent variable so it can find the picture of the agent from the agents folder
agent = agent + ".png"

main()