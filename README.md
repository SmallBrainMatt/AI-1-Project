## How to Run:

### Clone the Repository
Clone the project and navigate to its directory:
```bash
git clone https://github.com/SmallBrainMatt/AI-1-Project.git
cd AI-1-Project
```

### Create A Virtual Environment 

-  Windows:
      ```
      python -m venv venv
      ```
-  Mac/Unix:
      ```
      python3 -m venv venv
      ```
    
### Activate the Virtual Environment

-  Windows:
      ```bash
      venv\Scripts\activate
      ```
-  Mac/Unix:
      ```bash
      source venv/bin/activate
      ```
    
### Install Python Dependencies 

```
pip install -r requirements.txt
```

### Run:

```
py bfs.py
```
or 
```
py dfs.py
```
To run on a specific maze file add the "--mazeFile" flag followed by maze_{maze_number}.csv
