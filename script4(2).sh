#!/usr/bin/sh
for i in `ls $1`
do
  if file "$i" | grep -q "ASCII"; then
    cat "$i" >> ../show_all
  fi
done
sort ../show_all | head -n 10 | tail -n 5 | cat
