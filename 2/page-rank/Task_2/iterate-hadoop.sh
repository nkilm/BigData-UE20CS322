#!/bin/sh
CONVERGE=1
ITER=1
rm w w1 log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /task-* 

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-mapper "'LOCAL_PATH_to_Task1_Mapper_file'" \
-reducer "'LOCAL_PATH_to_Task_1_Reducer_file' 'LOCAL_PATH to_w_file'"  \
-input HDFS_PATH_to_input.txt \
-output /task-1-output


while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
	-mapper "'LOCAL_PATH_to_Task_2_Mapper_file' 'LOCAL_PATH_to_w_file' 'LOCAL_PATH_to_page_embeddings_JSON_file'" \
	-reducer "'LOCAL_PATH_to_Task_2_Reducer_file'" \
	-input HDFS_PATH_to_input \
	-output /task-2-output
	touch w1
	hadoop dfs -cat /task-2-output/part-00000 > "LOCAL_PATH_to_current_directory/w1"
	CONVERGE=$(python3 LOCAL_PATH_to_current_directory/check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	hdfs dfs -rm -r /task-2-output/
	echo $CONVERGE
done
