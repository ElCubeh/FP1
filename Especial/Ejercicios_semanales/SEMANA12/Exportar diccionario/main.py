import file_utils
import string_utils

test_dict = {"agua": (30, 10, 8), "pescado": (32, 78), "arroz": (50, 25, 12)}
string_utils.export_dict(test_dict, "output.csv")
file_utils.show_file("output.csv")
