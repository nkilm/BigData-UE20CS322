run:
	hadoop jar /home/pes1ug20cs667/hadoop-3.3.3/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar \
	-mapper "'/home/pes1ug20cs667/bigdata/page-rank/mapper_1.py'" \
	-reducer "'/home/pes1ug20cs667/bigdata/page-rank/reducer_1.py' '/home/pes1ug20cs667/bigdata/page-rank/w'" \
	-input /bigdata/pagerank/web-BerkStan.txt \
	-output /bigdata/pagerank/Task_1_output
	
list:
	hdfs dfs -ls /bigdata/
	hdfs dfs -ls /bigdata/pagerank

clean:
	hdfs dfs -rm -r /bigdata/pagerank/Task_1_output

python:
	cat ./Task_1/web-BerkStan.txt | python3 mapper_1.py | python3 reducer_1.py "/home/pes1ug20cs667/bigdata/page-rank/Task_1/w.txt" > output.txt