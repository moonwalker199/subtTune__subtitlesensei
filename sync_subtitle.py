import moviepy.editor as mp
import pysrt
from datetime import timedelta

def load_video(video):
    return mp.VideoFileClip(video)

def load_subtitles(subtitle_path):
    return pysrt.open(subtitle_path)

def print_subtitle_timings(subtitles):
    for subtitle in subtitles:
        print(f"Start: {subtitle.start}, End: {subtitle.end}, Text: {subtitle.text}")

def adjust_subtitle_timings(subtitles, offset):
    offset_timedelta = timedelta(seconds=offset)
    for subtitle in subtitles:
        subtitle.start = subtitle.start + offset_timedelta
        subtitle.end = subtitle.end + offset_timedelta

def main(video_path, subtitle_path, offset):
    video = load_video(video_path)
    subtitles = load_subtitles(subtitle_path)

    print(f"Video duration: {video.duration} seconds")
    print(f"Number of subtitles: {len(subtitles)}")
    print_subtitle_timings(subtitles)

    adjust_subtitle_timings(subtitles, offset)
    subtitles.save('adjusted_subtitles.srt')
    print("Adjusted subtitles saved as 'adjusted_subtitles.srt'.")

if __name__ == "__main__":
    video_path = 'demo video.mp4'
    subtitle_path = 'Chernobyl.S01E01.AMZN.WEBRip-NTb.English-WWW.MY-SUBS.CO.srt'
    offset_seconds = 1  # Adjust the offset as needed

    main(video_path, subtitle_path, offset_seconds)
