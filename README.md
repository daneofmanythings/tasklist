# **TASKLIST**

A tool to help guide you through choosing a task workload.

## **STATE OF MAIN**

Fully functional v1.

## **USAGE GUIDE**

* Install the latest version of python. 
* Run `python main.py` from the root of the repository in a terminal. Earlier versions of python may still work (back to 3.6), but have not been tested.

####    TASKS
    
    * length: time to complete the task in minutes
    * period: time until the task should be repeated in days. use 0 for one time tasks.
    * strict recurrence: 
        - true: due status is calculated without regard for last completed date.
        - false: due status is calculated from last completed date

####    TASKLIST
    
    * Processing a tasklist updates the registry with the tasks' completion status.
    
## **COMING UP**

* Implementation of tags to sort tasks for more customized tasklist generation.
* More features around managing tasklists

## **BUG REPORTING**

If you happen to get a crash, please submit the output of the crash (stacktrace) as copied text or a screenshot, and I will fix it.
If you find a bug, please submit the intended behavior, what actually happened, and recreation steps.

