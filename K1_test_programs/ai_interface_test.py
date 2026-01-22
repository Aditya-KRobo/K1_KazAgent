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
                          \n1. Start face tracking -> ft\
                          \n2. Stop face tracking -> sft\
                          \n....."
        )

        if input_cmd == "ft":
            res = client.StartFaceTracking()
        elif input_cmd == "sft":
            res = client.StopFaceTracking()

        if res != 0:
            print(f"Request failed: error = {res}")


if __name__ == "__main__":
    main()
