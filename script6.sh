#!/usr/bin/sh
mkdir ../ascii-ones/
for i in `ls $1`
do
  if file "$i" | grep -q "ASCII"; then
    x=`find "$i" -name  \*a\*`
    if [ -n "$x" ]; then
      cp "$x" ../ascii-ones/
    fi
  fi
done
