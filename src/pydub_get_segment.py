"""
@file pydub_get_segment.py

@brief Get segment of audio, specified (in milliseconds) as [<start_time>, <end_time>] from MP3 audio.
"""

from pydub import AudioSegment
from pydub.playback import play


TEST_FILE = "data/kvist_som_knekker.mp3"


def get_samples_from_segment(segment: AudioSegment=None, show_samples: bool=False) -> list:
    """ Extract raw samples from audio segment. """
    raw_data = list()
    for frame in segment:
        samples = frame.get_array_of_samples()
        for sample in samples:
            raw_data.append(sample)
    #
    if show_samples:
        print(raw_data)
    #
    return raw_data


def get_data_from_samples(raw_data: list=None) -> None:
    """ Get MAX/MIN-samplevalues from raw data, and calculate average 'level' (absolute value). """
    min_val = min(raw_data)
    max_val = max(raw_data)
    mean_val = 0
    #
    for val in raw_data:
        mean_val += abs(val)
    #
    mean_val = int(mean_val / len(raw_data))
    #
    print("\nData from samples:")
    print(f"MAX = {max_val}")
    print(f"MIN = {min_val}")
    print(f"AVG = {mean_val}")
    print("")
     

def get_audio_segment(audio_filename: str=None, start_time: int=0, end_time: int=0, export_to_file: bool=False, play_segment: bool=True, audio_format: str="mp3") -> AudioSegment:
    """ Get part of audio file, limited by a START and END time (in milliseconds), and - optionally - play the audio, and write the segment to file (in 'data' folder). """
    if not audio_filename:
        return None
    #
    sound = AudioSegment.from_file(audio_filename, format=audio_format)
    segment = sound[start_time:end_time]
    #
    if play_segment:
        play(segment)
    #
    if export_to_file:
        out_filename = input("Give name of output file: ")
        out_filepath = "data/" + out_filename
        segment.export(out_filepath, format=audio_format)
        print(f"Audio written to {out_filename} ...")
    #
    return segment


# ****************************************** Functional Test *****************************************
if __name__ == '__main__':
    snip = get_audio_segment(audio_filename=TEST_FILE, start_time=0, end_time=600)
    samples = get_samples_from_segment(segment=snip)
    get_data_from_samples(raw_data=samples)

