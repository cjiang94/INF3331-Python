#!/bin/bash

# I assume that the path to the .bookmarks will lie under HOME-directory
path="$HOME/.bookmarks"

if [[ $# -eq 0 ]]; then
  while IFS='|' read b_name b_loc
    do
      export $b_name="$b_loc"
    done < $path
else
  arg=$1
  case "$arg" in
    -a)
      if [[ $# -lt 2 ]]; then
        echo "Error: Missing bookmarkname"
      else
        echo "$2|$PWD" >> $path
        #The assignment does not ask to define a shell variable when adding. But I do it here so I don't have to call ./bookmark.sh again
        export $2="$PWD"
      fi
      ;;
    -r)
      if [[ $# -lt 2 ]]; then
        echo "Error: Missing bookmarkname"
      else
        while IFS='|' read b_name b_loc
          do
            if [[ "$b_name" == "$2" ]]; then
              unset "$b_name"
              sed -i "/$b_name|/d" $path
            fi
          done < $path
      fi
      ;;
    *)
      echo "$0: invalid option \"$arg\"";
      ;;
  esac
fi
