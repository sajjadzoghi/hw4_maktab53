#!/usr/bin/bash
echo "number of files: `ls -l $1 | cut -c1 | grep - | wc -l`"
echo "number of folders: `ls -l $1 | cut -c1 | grep d | wc -l`"
