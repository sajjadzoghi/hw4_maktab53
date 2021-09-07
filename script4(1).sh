#!/usr/bin/sh
for i in `ls $1`
do
  if [ -f "$i" ]; then
    cat $i >> ../show_all 
  fi
done
sort ../show_all | head -n 10 | tail -n 5 | cat
