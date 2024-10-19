import moviepy.editor as mp
import pysrt
from datetime import timedelta, datetime

def load_video(video):
    return mp.VideoFileClip(video)

def load_subtitles(subtitle_path):
    return pysrt.open(subtitle_path)

def print_subtitle_timings(subtitles):
    for subtitle in subtitles:
        print(f"Start: {subtitle.start}, End: {subtitle.end}")

def new_subtitle(subtitles, offset):
    for subtitle in subtitles:
        # Create a timedelta for the offset
        offset_timedelta = timedelta(seconds=offset)
        
        # Convert SubRipTime to datetime, add the offset, then convert back
        start_datetime = datetime.combine(datetime.min, subtitle.start.to_time()) + offset_timedelta
        end_datetime = datetime.combine(datetime.min, subtitle.end.to_time()) + offset_timedelta
        
        # Set the adjusted times back to the subtitle
        subtitle.start = pysrt.SubRipTime(start_datetime.hour, start_datetime.minute, start_datetime.second, start_datetime.microsecond // 1000)
        subtitle.end = pysrt.SubRipTime(end_datetime.hour, end_datetime.minute, end_datetime.second, end_datetime.microsecond // 1000)

def main(video_path, subtitle_path, offset):
    video = load_video(video_path)
    subtitles = load_subtitles(subtitle_path)

    print(f"Video duration: {video.duration} seconds")
    print(f"Number of subtitles: {len(subtitles)}")
    print_subtitle_timings(subtitles)

    new_subtitle(subtitles, offset)
    subtitles.save('adjusted_subtitles.srt')
    print("Adjusted subtitles saved as 'adjusted_subtitles.srt'.")

if __name__ == "__main__":
    video_path = 'demo video.mp4'
    subtitle_path = 'Chernobyl.S01E01.AMZN.WEBRip-NTb.English-WWW.MY-SUBS.CO.srt'
    offset_seconds = 5  # Adjust the offset as needed

    main(video_path, subtitle_path, offset_seconds)
