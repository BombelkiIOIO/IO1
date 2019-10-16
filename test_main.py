import data

def make_list_all_source_files_test():
    file_list = data.make_list_all_source_files("../")
    assert len(file_list) == 5