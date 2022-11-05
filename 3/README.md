# Task 1 

#### How to execute/run?
```bash
make run

# if output dir exists
make clean 
```

# Task 2

1. First start `Consumer`
```bash
# to view the output in terminal
make consumer

# to save the output in .json file
make save
```
2. Start `Producer`
```bash
make producer
```

> Testing against solution
```bash
diff -s <(jq --sort-keys . output.json) <(jq --sort-keys . solution.json)
```