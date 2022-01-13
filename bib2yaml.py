import sys
import os


def bib2yaml(default, not_fields):
    # Read argv and create input and output paths
    if len(sys.argv) > 3:
        print("Warning! Too many arguments. Usage: bib2yaml.py <input.bib> <output.yaml>")
    in_file = sys.argv[1]
    if len(sys.argv) == 3:
        out_file = sys.argv[2]
    else:
        out_file = in_file.replace(".bib", ".yaml")
    in_file = str(os.getcwd()) + "/" + in_file
    out_file = str(os.getcwd()) + "/" + out_file

    # Read input file and initialize list for references, counter r, default reference and non-wanted fields list
    with open(in_file, 'r') as fr:
        list_lines = fr.readlines()
    r = 0
    ref_list = []

    # Iterate through lines, and create list of lines
    for str_line in list_lines:
        if str_line.startswith('@'):
            type = str_line.split('{')[0].replace("@", "")
            ref_list.append("- " + "type" + ": " + type)
        elif not str_line.startswith('}') and str_line != "\n":
            field = str_line.split('={')[0].replace(" ", "")
            if field not in not_fields:
                value = str_line.split(field+'={')[1].replace('},\n', '').replace('}\n', '')
                ref_list.append("    " + field + ": " + value)
        if  str_line.startswith('}'):
            r += 1

    with open(out_file, 'w') as fw:
       fw.write('\n'.join(ref_list))


if __name__ == "__main__":
    ## Change default dict to have whatever fields you want and their default values
    default = {"type": ""}
    ## Change not_fields to have whatever fields do not want to have in the output
    not_fields = []
    bib2yaml(default, not_fields)
    print("Done!")