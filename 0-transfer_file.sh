#!/usr/bin/env bash
#Bash script that transfers a file from our client to a server

if [ "$#" -lt 3 ];
then
    echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
    exit
fi

file_path="$1"
ip="$2"
username="$3"
ssh_key="$4"

scp -i "$ssh_key" -o StrictHostKeyChecking=no "$file_path" "$username@$ip:~/"