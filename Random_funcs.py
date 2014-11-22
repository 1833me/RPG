import pickle

def save_file(list, file_name):
    pickle_file = open(file_name,'w')
    pickle.dump(list,pickle_file)
    pickle_file.close()
    return


def load_file(file_name):
    pickle_file = open(file_name, "r")
    list = pickle.load(pickle_file)
    pickle_file.close()
    return list
