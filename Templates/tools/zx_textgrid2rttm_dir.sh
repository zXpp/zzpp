#!/bin/bash
rootdir=/home/zzpp220/Documents/LIUM-master
textgridfile_dir=/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/SCUTPHONE/textgrid
#rttmfile_dir=$rootdir/newchain_praat2rttm
rttmfile_dir=/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/SCUTPHONE/ref_rttm
mode='test'
for file in $textgridfile_dir/*.TextGrid
do  
  if [ -f "$file" ]
  then
	#echo $file
	   python2.7 ~/Templates/tools/textgrid2rttm.py $file $mode
	   echo ok    
  fi
done
mv `pwd`/*.ref.rttm $rttmfile_dir/
