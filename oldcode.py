import urllib.request as ur
import subprocess
import re
import os
import fileFunctions as f
import gitstuff as g
# read_me_list = []

g.get_rep_names()
g.get_githubs_reps()
f.get_read_me()
f.write_to_file()
g.push_git()

# def get_data():
#     file =ur.urlopen('https://api.github.com/orgs/python-elective-2-spring-2019/repos?per_page=100').read()
#     fil = file.decode("utf-8")
#     data = re.findall(r'"clone_url":"([^"]+)', fil)
#     print (data)
#     return data
#
# def get_rep_names():
#     file = ur.urlopen('https://api.github.com/orgs/python-elective-2-spring-2019/repos?per_page=100').read()
#     fil = file.decode("utf-8")
#     data = re.findall(r'"name":"([^"]+)', fil)
#     data.sort(key=str.casefold)
#     print(data)
#     return data




# os.mkdir('reps')
# os.chdir('reps')
# print(os.listdir())

# if (get_rep_names()==os.listdir()):
#     for j in os.listdir("C:/Users/abenh/PycharmProjects/mandatoryPyth/reps"):
#         os.chdir(j)
#         subprocess.run(['git', 'pull'])
#         print("hej")
#         os.chdir("C:/Users/abenh/PycharmProjects/mandatoryPyth/reps")
# else:
#     for i in get_data():
#         subprocess.run(['git','clone',i])

# def get_read_me2():
#     for i in os.listdir():
#         os.chdir(i)
#         f = str(open("README.md","r").read())
#         read_me_list.append(f)
#         os.chdir("C:/Users/abenh/PycharmProjects/mandatoryPyth/reps")


# def get_read_me():
#     required_list = []
#     for i in os.listdir():
#         os.chdir(i)
#         with open('README.md', 'r') as f:
#             flag = False
#             for line in f:
#                 if len(line.split()) == 0:
#                     continue
#                 else:
#                     if line.startswith("### Supplementary reading"):
#                         flag = False
#                     if line.startswith("## Supplementary reading"):
#                         flag = False
#                     if line.startswith("## Supplemantary reading"):
#                         flag = False
#                     if line.startswith("## Exercises"):
#                         flag = False
#                     if flag:
#                         required_list.append(line)
#                     if line.startswith("## Required reading"):
#                         flag = True
#         os.chdir("C:/Users/abenh/PycharmProjects/mandatoryPyth/reps")
# get_read_me()


# def write_to_file():
#     required_list.sort(key=str.casefold)
#     required_list.insert(0,"Required Reading:")
#     # filter(None, required_list)
#     final_list = []
#     os.chdir("C:/Users/abenh/PycharmProjects/mandatoryPyth")
#     # os.mkdir("ReadingRepo")
#     os.chdir("C:/Users/abenh/PycharmProjects/mandatoryPyth/ReadingRepo")
#     with open("C:/Users/abenh/PycharmProjects/mandatoryPyth/ReadingRepo/required_reading.md", 'w+') as file_handler:
#                 for i in required_list:
#                     i = i.strip()
#                     if i not in required_list:
#                         file_handler.write("{}\n".format(i))
