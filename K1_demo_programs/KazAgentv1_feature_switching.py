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

Button_values = {"BTN_EAST": 0, "BTN_C": 0, "BTN_SOUTH": 0, "BTN_NORTH": 0, "BTN_WEST": 0, "BTN_Z": 0, "ABS_RX": 0, "ABS_RY": 0, "BTN_TL2": 0, "BTN_TR2": 0, "ABS_HAT0X": 0, "ABS_HAT0Y": 0, "BTN_START": 0, "BTN_SELECT": 0, "BTN_THUMBL": 0, "BTN_MODE": 15}

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
            # pass
            print(f'{event.ev_type} | {event.code} | {event.state}')
        if event.code == But_LB and event.state == 1:
            print("Requested Sit-down")
        elif event.code == But_RB and event.state == 1:
            print("Requested Stand-up")
        elif event.code == But_Min and event.state == 1 :
            print("Requested Dance")

    if res != 0:
        print(f"Request failed: error = {res}")


if __name__ == "__main__":
    main()
