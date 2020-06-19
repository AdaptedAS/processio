### Python ProcessIO
###### Running functions with multiprocessing hassle free

![PyPI - Format](https://img.shields.io/pypi/format/processio)
![PyPI - Status](https://img.shields.io/pypi/status/processio)
![Downloads](https://pepy.tech/badge/processio)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/processio)

A nice package to help you run functions with multiprocessing and get their result.<br />

### Installation
```
pip install processio
```

### Usage
##### Run function in own process
```python
import time
from processio import ProcessIO


def get_company_name():
    # Do work in own process
    time.sleep(5)
    return 'Adapted'


def do_some_work():
    get_name = ProcessIO(get_company_name)

    # do stuff or run a while loop to wait for result

    while get_name.doing_work():
        print('Waiting for process to finnish')

    # You can also call .result() and the main thread will wait 
    # for the thread to return your result.

    company_name = get_name.result()

    print(company_name) # Outputs -> Adapted

    
if __name__ == '__main__': # <- its required to execute the function main
    do_some_work() 
    
```

### Main commands

```python
# Import the module
from processio import ProcessIO

# Start your function with or without arguments
var = ProcessIO(function, args, kwargs)

# Wait for the function to finnish or get the result if its finished
var.result()
```

## Optional commands
```python
# Check if your thread is still working on the function.
# This will return True if the function is not completed.

var.doing_work()

```

##### Use parseIO to save a lot of time on list parsing

```python
import time
from processio import ParseIO


def list_parser(list):
    result = 0
    for line in list:
        result += get_total_amout(line)
    return result


def do_some_work():
    # this will split the list into 4 and run the function on
    # 4 different processes, that in most cases will almost speed
    # up the work time by 4.

    # you can define the number of processes you want to run, but as a
    # default the module runs on the systems cpu cores - 1

    parser = ParseIO(list_parser, huge_list)

    # do stuff or run a while loop to wait for result

    while parser.doing_work():
        print('Waiting for processes to finnish')

    # You can also call .result() and the main thread will wait 
    # for the thread to return your result.

    result = parser.result()
    
    # result comes back as list pr process, so in this case we will get 
    # a list with 4 numbers that we can loop thru.
    
    print(result) # Outputs -> [1000, 1000, 1000, 1000] <- example

    
    total = 0
    for res in result:
        total += res


    print(total) # Outputs -> 4000 <- example
    
if __name__ == '__main__': # <- its required to execute the function main
    do_some_work() 
```
### Testing

Use the following command to run tests.

```bash
python -m unittest threadit.tests.test_threadit
```

### Changelog:

See CHANGELOG.md
