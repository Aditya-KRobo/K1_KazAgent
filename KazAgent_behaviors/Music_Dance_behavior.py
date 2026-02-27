from booster_robotics_sdk_python import (
    DanceId,
    WholeBodyDanceId,
    B1LocoClient,
    ChannelFactory,
    RobotMode,
    Position,
    Orientation,
    Posture,
    GetModeResponse,
    Quaternion,
    Frame,
    Transform,
)
import sys, time, random
from inputs import get_gamepad

import pygame # Load the popular external library

But_A = "BTN_EAST"
But_B = "BTN_C"
But_X = "BTN_SOUTH"
But_Y = "BTN_NORTH"
But_LB = "BTN_WEST"
But_RB = "BTN_Z"
But_LT = "ABS_RX"
But_RT = "ABS_RY"
But_Min = "BTN_TL2"
But_Plu = "BTN_TR2"
D_X = "ABS_HAT0X"
D_Y = "ABS_HAT0Y"
But_START = "BTN_START"
But_SELECT = "BTN_SELECT"
But_O = "BTN_THUMBL"
But_HOME = "BTN_MODE"

Button_values = {"BTN_EAST": 0, "BTN_C": 0, "BTN_SOUTH": 0, "BTN_NORTH": 0, "BTN_WEST": 0, "BTN_Z": 0, "ABS_RX": 0, "ABS_RY": 0, "BTN_TL2": 0, "BTN_TR2": 0, "ABS_HAT0X": 0, "ABS_HAT0Y": 0, "BTN_START": 0, "BTN_SELECT": 0, "BTN_THUMBL": 0, "BTN_MODE": 0}

def main():

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} networkInterface")
        sys.exit(-1)

    ChannelFactory.Instance().Init(0, sys.argv[1])

    client = B1LocoClient()
    client.Init()
    res = 0

    pygame.init()

    while True:

        events = get_gamepad()
        
        for event in events:
            # print(f'{event.ev_type} | {event.code} | {event.state}')
            Button_values[event.code] = event.state

            #Command to start music and dance combo
            if Button_values[But_Plu] == 1:
                
                #Play the music first
                pygame.init()
                try:
                    pygame.mixer.music.load('/home/booster/Workspace/K1_Custom_Behaviors/K1_test_programs/res/Michael Jackson - Billie Jean(2).mp3')

                except pygame.error as e:
                    print(f"Could not load music file: {e}")
                    # Handle the error, maybe exit the program or use a placeholder
                    exit()

                pygame.mixer.music.set_volume(0.7)

                try:
                    pygame.mixer.music.play()
                    print("Music started playing...")
                    while pygame.mixer.music.get_busy():
                        time.sleep(1) 
                except KeyboardInterrupt:
                    print("Music playback interrupted by user.")
    

                #Then start the dance
                #Start with setting the robot to stand mode(LT+Start), then switch to dance agent(LT+RT+Y), then switch to walk mode(RT+A)
                #Then give it the dance command from the preprogrammed dance options(LB+Y),(LB+Dpad_Up).

    # res = client.ChangeMode(RobotMode.kWalking)

    # res = client.PlaySound()
    # res = client.StopSound()
    # res = client.Dance(DanceId.kNewYear)
    # res = client.PlaySound("/home/booster/Workspace/K1_Custom_Behaviors/K1_test_programs/res/Michael Jackson - Billie Jean(2).mp3")

    # res = client.Dance(DanceId.kNezha)
    # res = client.Dance(DanceId.kTowardsFuture)
    # res = client.Dance(DanceId.kPogbaGuesture)
    # res = client.Dance(DanceId.kUltramanGuesture)
    # res = client.Dance(DanceId.kChineseGreetingGuesture)
    # res = client.Dance(DanceId.kCheeringGuesture)
    # res = client.Dance(DanceId.kManekiGuesture)
    # res = client.Dance(DanceId.kStop)

    # res = client.WholeBodyDance(WholeBodyDanceId.kArbicDance)
    # res = client.WholeBodyDance(WholeBodyDanceId.kMichaelDance1)
    # res = client.WholeBodyDance(WholeBodyDanceId.kMichaelDance2)
    # res = client.WholeBodyDance(WholeBodyDanceId.kMichaelDance3)
    # res = client.WholeBodyDance(WholeBodyDanceId.kMoonWalk)
    # res = client.WholeBodyDance(WholeBodyDanceId.kBoxingStyleKick)
    # res = client.WholeBodyDance(WholeBodyDanceId.kRoundhouseKick)

    # mixer.music.play()
    
    # client.StopSound()

    # if res != 0:
    #     print(f"Request failed: error = {res}")


if __name__ == "__main__":
    main()
