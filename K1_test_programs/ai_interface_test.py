from booster_robotics_sdk_python import (
    B1LocoClient,
    AiClient,
    ChannelFactory,
    StartAiChatParameter,
    TtsConfig,
    LlmConfig,
    AsrConfig,
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


def build_default_start_param(
    enable_face_tracking: bool = False,
) -> StartAiChatParameter:
    """
    Build a sample StartAiChatParameter.
    Adjust system_prompt / welcome_msg / TTS / ASR as needed.
    """
    # Example TTS configuration
    tts = TtsConfig(
        voice_type="zh_male_wennuanahu_moon_bigtts",
        ignore_bracket_text=[1, 2],
    )

    # Example LLM configuration
    llm = LlmConfig(
        system_prompt="You are a helpful humanoid robot assistant.",
        welcome_msg="Hello, I am the Booster robot assistant.",
        prompt_name="default",
    )

    # Example ASR configuration
    asr = AsrConfig(
        interrupt_speech_duration=800,
        interrupt_keywords=["stop", "hold on", "do not speak"],
    )

    p = StartAiChatParameter()
    p.interrupt_mode = True
    p.tts_config = tts
    p.llm_config = llm
    p.asr_config = asr
    p.enable_face_tracking = enable_face_tracking
    return p


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} networkInterface")
        sys.exit(-1)

    ChannelFactory.Instance().Init(0, sys.argv[1])

    client = AiClient()
    client.Init()

    print("AI CLI started.")
    client.Init()
    x, y, z, yaw, pitch = 0.0, 0.0, 0.0, 0.0, 0.0
    res = 0
    hand_action_count = 0

    while True:
        input_cmd = input(
            "Here is the command list:\
                          \n1. Start face tracking -> ft\
                          \n2. Stop face tracking -> sft\
                          \n3. Stop Ai Chat -> stp\
                          \n....."
        )

        if input_cmd == "ft":
            param = build_default_start_param(enable_face_tracking=True)
            res = client.StartAiChat(param)
            print("[OK] StartAiChat (face_tracking = True) sent.")
        elif input_cmd == "sft":
            param = build_default_start_param(enable_face_tracking=False)
            res = client.StartAiChat(param)
            print("[OK] StartAiChat (face_tracking = False) sent.")
        elif input_cmd == "stp":
            res = client.StopAiChat()

        if res != 0:
            print(f"Request failed: error = {res}")


if __name__ == "__main__":
    main()
