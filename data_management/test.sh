#!/bin/bash
TEMP=`getopt -o b:c:m:o: --long bot:,corpus:,mod:,out:,parallel: -n 'report' -- "$@"`

if [ $? != 0 ] ; then echo "Terminating..." >&2 ; exit 1 ; fi

# Note the quotes around `$TEMP': they are essential!
eval set -- "$TEMP"
# echo "$@"
parallel_flag=0
while true ; do
	case "$1" in
        -b|--bot)
                bot=$2
                shift 2
                # echo $bot
                ;;
	-c|--corpus) 
		corpus=`pwd`/$2
		shift 2
		echo -e "\033[36;4mcorpus\' path is $corpus\033[0m"
		;;
	-m|--mod) 
		mod=$2
		shift 2
		# echo $mod
		;;
	-o|--out) 
		out=`pwd`/$2
                echo -e "\033[36;4moutput dir is $out\033[0m"
                shift 2
		;;
	--parallel)
                parallel_flag=1 
		parts=$2
                echo -e "\033[36;4mThe total of threads is $parts\033[0m"
                shift 2
		;;

	--) shift ; break ;;
	*) echo "Internal error!" ; exit 1 ;;
	esac
done
#echo "Remaining arguments:"
for arg do echo 'extra argument --> '"\`$arg'" ; done
export PYTHONPATH=/opt/tools/:$PYTHONPATH
cd /opt/tools/data_management
source venv/bin/activate
if [ $parallel_flag -eq 1 ];then
    op=parallel
    python run.py -P 1781 --op $op -b $bot -c $corpus -m $mod -o $out --parts $parts
else
    op=batchprocessing
    python run.py -P 1781 --op $op -b $bot -c $corpus -m $mod -o $out
fi
deactivate
