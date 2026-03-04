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

    pad_lock = False

    pygame.init()

    while True:

        events = get_gamepad()
        
        for event in events:
            # print(f'{event.ev_type} | {event.code} | {event.state}')
            Button_values[event.code] = event.state
            
            #Command to stop music and dance combo
            if Button_values[But_Min] == 1 and pad_lock:
                pad_lock = False
                # pygame.mixer.music.stop()
                # res = client.ChangeMode(RobotMode.kPrepare)
                # print("Music stopped and robot set to prepare mode.")

            #Command to start music and dance combo
            if Button_values[But_Plu] == 1 and not pad_lock:
                pad_lock = True
                
                #Play the music first
                try:
                    pygame.mixer.music.load('/home/booster/Workspace/K1_Custom_Behaviors/K1_test_programs/res/Lion Dance.mp3')

                except pygame.error as e:
                    print(f"Could not load music file: {e}")
                    # Handle the error, maybe exit the program or use a placeholder
                    exit()

                pygame.mixer.music.set_volume(1.0)

                try:
                    # res = client.WholeBodyDance(WholeBodyDanceId.kMichaelDance2)
                    pygame.mixer.music.play()
                    print("Music started playing...")
                    while pygame.mixer.music.get_busy():
                        time.sleep(1) 
                except KeyboardInterrupt:
                    print("Music playback interrupted by user.")
                    pygame.mixer.music.stop()
                    # res = client.ChangeMode(RobotMode.kPrepare)
    


if __name__ == "__main__":
    main()
