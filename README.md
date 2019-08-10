# Remote Environment Helper #

This is your own personal text-driven remote-environment helper.
 
It is meant to simplify your everyday work by automating simple ssh-based tasks.
It allows you to store SSH login data in a simple CSV file and use them easily, without the fuss of copy-pasting 
long ssh commands.


### Features ###

* **ssh** - allows you to easily connect with a remote environment
* **info** - prints info about a remote environment
* **download** - download a file from a remote environment via SSH
* **upload** - upload a file to a remote environment via SSH


### Prerequisites

* **Python3**


### Installation ###

1. Clone the repository
2. Add the path to the executable ```env-helper``` to your $PATH to 
make it available anywhere

### Usage ###

To start the program simply run the ```env-helper``` executable.

You can pass values as program arguments to skip steps and speed up the process, e.g.

```
env-helper <<command>> <<project>>
```

The program will help you find what you want quickly. Simply hit the ```TAB``` button
on your keyboard to invoke autocompletion.


### Updating access data ###

To add/update access data for project/environment copy the ```envhelper/data/access.csv.dist``` 
to ```envhelper/data/access.csv``` and edit.

The file structure goes as follows:
```
project,environment,ssh user,ip address,ssh port,additional information
```
E.g.
```
my_project,develop,root,127.0.0.1,22,Authentication using private key
my_project,staging,root,127.0.0.1,22,
```

## Authors

* **Maciej Sławik** - https://github.com/maciejslawik
