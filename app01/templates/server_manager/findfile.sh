for line in `find $1 -type f`
do
if [ -n "`grep $2 $line`" ];then
 echo $line
fi
done
