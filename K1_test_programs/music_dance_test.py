from booster_robotics_sdk_python import (
    DanceId,
    WholeBodyDanceId,
    B1LocoClient,
    ChannelFactory,
    RobotMode,
    PlaySound,
    StopSound,
    Position,
    Orientation,
    Posture,
    GetModeResponse,
    Quaternion,
    Frame,
    Transform,
)
import sys, time, random

from pygame import mixer  # Load the popular external library


def main():

    # mixer.init()
    # mixer.music.load('')

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} networkInterface")
        sys.exit(-1)

    ChannelFactory.Instance().Init(0, sys.argv[1])

    client = B1LocoClient()
    client.Init()
    res = 0

    res = client.ChangeMode(RobotMode.kWalking)

    # res = client.PlaySound()
    # res = client.StopSound()
    res = client.Dance(DanceId.kNewYear)
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

    if res != 0:
        print(f"Request failed: error = {res}")


if __name__ == "__main__":
    main()
