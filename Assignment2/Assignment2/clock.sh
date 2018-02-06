#!/bin/bash

case "$1" in
  no)
    for (( ; ; ))
    do
      clear
      TZ="Europe/Oslo" date +%T
      sleep 1
    done ;;
  sk)
    for (( ; ; ))
    do
      clear
      TZ="Asia/Seoul" date +%T
      sleep 1
    done ;;
  us)
    for (( ; ; ))
    do
      clear
      TZ="America/New_York" date +%T
      sleep 1
    done ;;
  *)
    echo "$0: invalid option \"$1\""; exit ;;
esac