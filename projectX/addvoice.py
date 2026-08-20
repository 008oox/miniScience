import os
import asyncio
import hashlib
import edge_tts


VOICE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "voice"
)


def add_voice(scene, voice):
    """
    voice:
        1. voice目录下的音频文件 → 直接播放
        2. voice目录下的txt文件 → 读取文本后生成语音
        3. 不存在的文件 → 直接把voice当作文本生成语音
    """

    voice_path = os.path.join(VOICE_DIR, voice)

    if os.path.isfile(voice_path):

        if voice.lower().endswith((".mp3", ".wav", ".m4a", ".ogg")):
            scene.add_sound(voice_path)
            return

        if voice.lower().endswith(".txt"):
            with open(
                voice_path,
                "r",
                encoding="utf-8"
            ) as f:
                text_voice = f.read()

            audio_path = text_to_voice(text_voice)
            scene.add_sound(audio_path)
            return

    audio_path = text_to_voice(voice)
    # print("ADD VOICE:", audio_path)
    # print("SCENE TIME:", scene.time)
    # print("EXISTS:", os.path.exists(audio_path))
    scene.add_sound(audio_path)


def text_to_voice(text_voice):

    os.makedirs(VOICE_DIR, exist_ok=True)

    text_hash = hashlib.md5(
        text_voice.encode("utf-8")
    ).hexdigest()

    audio_path = os.path.join(
        VOICE_DIR,
        f"{text_hash}.mp3"
    )

    if os.path.exists(audio_path):
        return audio_path

    async def generate():
        tts = edge_tts.Communicate(
            text_voice,
            # "zh-CN-XiaoxiaoNeural"
            "zh-CN-YunyangNeural"
        )
        await tts.save(audio_path)

    asyncio.run(generate())

    return audio_path