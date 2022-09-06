# Assignment 1

- Dataset(s) - [link](https://drive.google.com/drive/folders/1YVSvjSPyHswy4CENEV_pWTbbdeIximFA?usp=sharing)🔗

## Executing 

- For Windows, open `Git Bash` in the folder
```bash
cat path_to_dataset | python3 mapper.py [command line arguments] | sort -k 1,1 |python3 reducer.py > output.txt
```
> NOTE: Use only `Git Bash` to avoid getting errors.