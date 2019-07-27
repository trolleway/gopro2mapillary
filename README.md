# gopro2mapillary
Tool for simpler conversion of GoPro video for Mapillary

```
cat > config.env << EOF
TEST=test
EOF

mkdir g2m_data #if mount with bind

docker build  github.com/trolleway/gopro2mapillary --no-cache --tag gopro2mapillary

#create volume
docker volume create g2m_data

#mount real folder
docker run -it  \
  --name g2m \
  --mount type=volume,source=$(pwd)/g2m_data,target=/g2m_data \
  --env-file config.env \
  gopro2mapillary
  
```

# More simpler way


```
# parameter r should be calced as source fps / rate. 10x become 30fps/10=3
ffmpeg -r 3 -i j:\GOPRO\20190726\GH011703.MP4   -y GH011703.MP4


c:\mav\mapillary_tools.exe video_process --import_path "c:\temp\proc" --video_import_path "c:\temp\proc" --user_name "trolleway" --advanced --geotag_source "gopro_videos" --geotag_source_path "c:\temp\raw" --interpolate_directions  --use_gps_start_time --video_sample_interval 1 --overwrite_EXIF_gps_tag
```
