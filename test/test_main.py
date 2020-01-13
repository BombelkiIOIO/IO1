import data.data

def test_make_list_all_source_files():
    files = data.data.make_list_all_source_files('.')
    assert len(files) == 6

# def test_prepare_data_to_visualisation():
#     nodes = data.prepare_data_to_visualisation('.')
#     assert len([node in nodes if "data" in node.name]) == 1
     
