#!/bin/bash
#change base_dir to folder where the docker folders are held
base_dir=/home/docker/dockers
#edit below as needed
declare -a ignoredfolders=("ignore1" "ignore2")

#read -p "Do you want to run 'docker compose up -d' as well? y/[n] " run
#run=${run:-"n"}
run="y"

docker_update(){
  cd $2
  echo "Updating docker at" $2
  if [ $run == "y" ]
  then
    docker compose pull; docker compose up -d
  else
    docker compose pull
  fi
  cd $1
}

for folder in $base_dir/*
do
  foldername=$(basename $folder)
  if [[ ! "${ignoredfolders[@]}" =~ "$foldername" ]]
    for file in $folder/*
    do
      filename=$(basename $file)
      if [ $filename == "compose.yml" ] || [ $filename == "compose.yaml" ]
      then
        docker_update $base_dir $folder; break
      elif [ $filename == "docker-compose.yml" ] || [ $filename == "docker-compose.yaml" ]
      then
        docker_update $base_dir $folder; break
      fi
    done
  fi
done
