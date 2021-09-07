#!/usr/bin/sh
if [ -d $1 ]; then
  echo "directory exists."
else
  mkdir $1
fi
