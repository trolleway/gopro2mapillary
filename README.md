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

#mount with bind, for debug and filezilla
docker gopro2mapillary -it  \
  --name g2m \
  --mount type=volume,source=g2m_data,target=/gopro2mapillary/g2m_data \
  --env-file config.env \
  gopro2mapillary
  
```
