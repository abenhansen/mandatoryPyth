import os
required_list = []
def get_read_me():
    for i in os.listdir():
        os.chdir(i)
        with open('README.md', 'r') as f:
            flag = False
            for line in f:
                if len(line.split()) == 0:
                    continue
                else:
                    if line.startswith("### Supplementary reading"):
                        flag = False
                    if line.startswith("## Supplementary reading"):
                        flag = False
                    if line.startswith("## Supplemantary reading"):
                        flag = False
                    if line.startswith("## Exercises"):
                        flag = False
                    if flag:
                        required_list.append(line)
                    if line.startswith("## Required reading"):
                        flag = True
        os.chdir("C:/Users/abenh/PycharmProjects/mandatoryPyth/reps")

def write_to_file():
    required_list.sort(key=str.casefold)
    required_list.insert(0,"Required Reading:")
    # filter(None, required_list)
    final_list = []
    os.chdir("C:/Users/abenh/PycharmProjects/mandatoryPyth")
    if not os.path.exists('ReadingRepo'):
        os.makedirs('ReadingRepo')
    # os.mkdir("ReadingRepo")
    os.chdir("C:/Users/abenh/PycharmProjects/mandatoryPyth/ReadingRepo")
    with open("C:/Users/abenh/PycharmProjects/mandatoryPyth/ReadingRepo/required_reading.md", 'w+') as file_handler:
                for i in required_list:
                    i = i.strip()
                    if i not in required_list:
                        file_handler.write("{}\n".format(i))

