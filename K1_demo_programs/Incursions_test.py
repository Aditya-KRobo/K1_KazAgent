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
import pygame

def main():

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} networkInterface")
        sys.exit(-1)

    ChannelFactory.Instance().Init(0, sys.argv[1])

    client = B1LocoClient()
    client.Init()
    res = 0

    # res = client.ChangeMode(RobotMode.kCustom)

    pygame.init()

    try:
        pygame.mixer.music.load("/home/booster/Workspace/K1_Custom_Behaviors/K1_test_programs/res/Michael Jackson - Billie Jean(2).mp3")
    except pygame.error as e:
        print(f"Could not load music file: {e}")
        # Handle the error, maybe exit the program or use a placeholder
        exit()

    pygame.mixer.music.set_volume(0.7)

    try:
        pygame.mixer.music.play(-1)
        print("Music started playing...")
        while pygame.mixer.music.get_busy():
            time.sleep(1) 
            if res != 0:
                print(f"Request failed: error = {res}")
    except KeyboardInterrupt:
        print("Music playback interrupted by user.")
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
