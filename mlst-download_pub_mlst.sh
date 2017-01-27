#!/bin/bash
#adapted from:
#https://github.com/tseemann/mlst/blob/master/scripts/mlst-download_pub_mlst
#Torsten Seemann

set -e
currentDir=$(pwd)
OUTDIR=pubmlst
mkdir -p "$OUTDIR"
wget --no-clobber -P "$OUTDIR" http://pubmlst.org/data/dbases.xml 

for URL in $(grep '<url>' $OUTDIR/dbases.xml); do
#  echo $URL
  cd $currentDir
  URL=${URL//<url>}
  URL=${URL//<\/url>}
#  echo ${URL: -4}
  if [ ${URL:(-4)} = ".txt" ]; then
    PROFILE=$(basename $URL .txt)
    echo "$PROFILE "
    PROFILEDIR="$OUTDIR/$PROFILE"
    mkdir -p $PROFILEDIR
    cd $PROFILEDIR && wget $URL
  elif [ ${URL:(-4)} = ".tfa" ]; then
    cd $PROFILEDIR && wget $URL
  fi 
done
