from booster_robotics_sdk_python import (
    B1LocoClient,
    ChannelFactory,
    RobotMode,
    B1HandIndex,
    GripperControlMode,
    Position,
    Orientation,
    Posture,
    GripperMotionParameter,
    GetModeResponse,
    Quaternion,
    Frame,
    Transform,
    DexterousFingerParameter,
)
import sys, time, random


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} networkInterface")
        sys.exit(-1)

    ChannelFactory.Instance().Init(0, sys.argv[1])

    client = B1LocoClient()
    client.Init()
    x, y, z, yaw, pitch = 0.0, 0.0, 0.0, 0.0, 0.0
    res = 0
    hand_action_count = 0

    while True:
        input_cmd = input(
            "Here is the command list:\
                          \n1. Enter damp mode -> md\
                          \n2. Enter prep mode -> mp\
                          \n3. Enter walk mode -> mw\
                          \n4. Enter cust mode -> mc\
                          \n5. Start Handshake -> hsko\
                          \n6. Stop Handshake -> hskc\
                          \n7. Dance NewYear -> d0\
                          \n8. WB Dance Moonwalk -> wbd4\
                          \n....."
        )

        if input_cmd == "mp":
            res = client.ChangeMode(RobotMode.kPrepare)
        elif input_cmd == "md":
            res = client.ChangeMode(RobotMode.kDamping)
        elif input_cmd == "mw":
            res = client.ChangeMode(RobotMode.kWalking)
        elif input_cmd == "mc":
            res = client.ChangeMode(RobotMode.kCustom)
        elif input_cmd == "hsko":
            res = client.Handshake(kHandOpen)
        elif input_cmd == "d0":
            res = client.Dance(DanceId.kNewYear)
        elif input_cmd == "wbd4":
            res = client.WholeBodyDance(WholeBodyDanceId.kMoonWalk)

        if res != 0:
            print(f"Request failed: error = {res}")


if __name__ == "__main__":
    main()
