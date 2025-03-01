#!/bin/bash

OPTIONS=""
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -a)
    ALGO="$2"
    shift
    ;;
    -e1)
    EX_PATH_1="$2"
    shift
    ;;
    -e2)
    EX_PATH_2="$2"
    shift
    ;;
    -p|-t)
    OPTIONS="${OPTIONS}${1} "
    ;;
    *)
        echo "Argument inconnu: ${1}"
        exit
    ;;
esac
shift
done
python ./main.py $ALGO $EX_PATH_1 $EX_PATH_2 $OPTIONS
