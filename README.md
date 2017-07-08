# Nickel
Micro tasks library written in pure Python

## Installation
1. Clone repo 

        $ git clone https://github.com/bjornus/Nickel
    
2. Build & install

        $ python setup.py build
    
        $ sudo python setup.py install
        
4. Init manager

        $ nickel.py init
        
Done!

## Adding new task
If you want to place task in some project

      $ nickel.py add --project=PROJ_NAME
      
Or if you want to just add new task without project

      $ nickel.py add
      
## Checking tasks state
If you want to check some project

      $ nickel.py check --project=PROJ_NAME
    
 Or if you want to just check all tasks
 
     $ nickel.py check
