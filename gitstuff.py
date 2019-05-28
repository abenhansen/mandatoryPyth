import os
import subprocess
import re
import urllib.request as ur

def get_data():
    file =ur.urlopen('https://api.github.com/orgs/python-elective-2-spring-2019/repos?per_page=100').read()
    fil = file.decode("utf-8")
    data = re.findall(r'"clone_url":"([^"]+)', fil)
    return data

def get_rep_names():
    file = ur.urlopen('https://api.github.com/orgs/python-elective-2-spring-2019/repos?per_page=100').read()
    fil = file.decode("utf-8")
    data = re.findall(r'"name":"([^"]+)', fil)
    data.sort(key=str.casefold)
    return data

def get_githubs_reps():
    if not os.path.exists('reps'):
        os.makedirs('reps')
    os.chdir('reps')
    if (get_rep_names()==os.listdir()):
        for j in os.listdir():
            os.chdir(j)
            subprocess.run(['git', 'pull'])
            os.chdir("../")
    else:
        for i in get_data():
            subprocess.run(['git','clone',i])


def push_git():
    os.chdir("../ReadingRepo")
    path = os.getcwd()
    subprocess.run(['git', 'init',path])
    subprocess.run(['git','remote', 'add', 'origin', "https://github.com/abenhansen/mandatory1"])
    subprocess.run(['git', 'add', 'required_reading.md'])
    subprocess.run(['git','commit','-m','first''' "required_reading.md"])
    subprocess.run(['git','push','origin','master'])