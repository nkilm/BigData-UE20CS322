run:
	hadoop jar /home/pes1ug20cs667/hadoop-3.3.3/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar \
	-mapper '/home/pes1ug20cs667/bigdata/page-rank/mapper_1.py' \
	-reducer "'/home/pes1ug20cs667/bigdata/page-rank/reducer_1.py' 'w.txt'" \
	-input /bigdata/pagerank/web-BerkStan.txt \
	-output /bigdata/pagerank/Task_1_output/output.txt

test:
	hadoop jar /home/pes1ug20cs667/hadoop-3.3.3/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar \
	-mapper '/home/pes1ug20cs667/bigdata/page-rank/mapper_1.py' \
	-reducer "'/home/pes1ug20cs667/bigdata/page-rank/reducer_1.py' 'w.txt'" \
	-input "/bigdata/pagerank/sample_input.txt" \
	-output "/bigdata/pagerank/Task_1_testoutput/output.txt"

	hdfs dfs -cat /bigdata/pagerank/Task_1_testoutput/output.txt/part-00000


list:
	hdfs dfs -ls /bigdata/
	hdfs dfs -ls /bigdata/pagerank

show:
	hdfs dfs -cat /bigdata/pagerank/Task_1_output/output.txt/part-00000

test-show:
	hdfs dfs -cat /bigdata/pagerank/Task_1_testoutput/output.txt/part-00000

clean: 
	hdfs dfs -rm -r /bigdata/pagerank/Task_1_output

test-clean:
	hdfs dfs -rm -r /bigdata/pagerank/Task_1_testoutput

python:
	cat ./Task_1/sample_input.txt | python3 mapper_1.py | python3 reducer_1.py "/home/pes1ug20cs667/bigdata/page-rank/Task_1/w.txt" > output.txt