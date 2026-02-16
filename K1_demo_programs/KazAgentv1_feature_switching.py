# from evdev import InputDevice, categorize, ecodes

from inputs import get_gamepad

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


def main():

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} networkInterface")
        sys.exit(-1)

    ChannelFactory.Instance().Init(0, sys.argv[1])

    client = B1LocoClient()
    client.Init()
    res = 0

    # res = client.ChangeMode(RobotMode.kCustom)
    # # res = client.GetUpWithMode(RobotMode.kWalking)
    # res = client.EnterWBCGait()

    while True:
        events = get_gamepad()
        for event in events:
            print(f'{event.ev_type} | {event.code} | {event.state}')
        if event.code == "" and event.state == 1:
            print("Requested Sit-down")
        elif event.code == "" and event.state == 1:
            print("Requested Stand-up")
        elif event.code == "" and event.state == 1:
            print("Requested Dance")

    if res != 0:
        print(f"Request failed: error = {res}")


if __name__ == "__main__":
    main()
