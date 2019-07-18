
import gpxpy
import gpxpy.gpx

from datetime import datetime

def get_gpx_duration(gpx_filename):
    gpx_file = open(gpx_filename, 'r')
    gpx = gpxpy.parse(gpx_file)

    frist_point = None
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if frist_point is None: frist_point = point
    last_point = point

    difference = (last_point.time - frist_point.time).total_seconds()
    return(int(difference))

#validate
#check if any mp4 in folder

#cycle
    #export data stream from mp4

    #convert data to gpx

    #get lenght of time of gpx track

    #get length of video

    #calc video speed rate (x1, x5, x10, x15, x30)

    #if video speed not x1 - slow down video using ffmpeg
    #later mapillary video_process will operate as video in standart speed

    #call video_process
