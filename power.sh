#!/usr/bin/bash
echo "\$ bash power.sh"
echo -en "Enter number: "
read input
while [ "$input" != "exit" ]
do
  expr $input \* $input
  if [ $? -ne "0" ]; then
    echo "Sorry! Please enter an integer."
  fi
  echo -en "Enter number: "
  read input  
done
echo "\$"
