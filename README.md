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
