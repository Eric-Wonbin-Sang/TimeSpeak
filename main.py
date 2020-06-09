import datetime
import os
from gtts import gTTS
from playsound import playsound


def get_mp3_from_str(data_str, file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    audio_object = gTTS(
        text=data_str,
        lang='en',
        slow=False
    )
    audio_object.save(file_path)


def main():

    time_mp3_path = "time.mp3"

    curr_datetime = datetime.datetime.now()
    prev_datetime = curr_datetime
    while True:

        curr_datetime = datetime.datetime.now()

        if curr_datetime.second % 5 == 0 and curr_datetime.second != prev_datetime.second:
            get_mp3_from_str(curr_datetime.strftime("The time is %H %M %p and %S seconds"), time_mp3_path)
            playsound(time_mp3_path)

        prev_datetime = curr_datetime


main()
