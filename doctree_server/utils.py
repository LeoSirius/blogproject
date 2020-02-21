from rest_framework.response import Response


def is_leaf(line):
    """
    whether line is leaf
    """
    return '(' in line and ')' in line and '[' in line and ']' in line


def get_path(line):
    """
    only leaf node need to call this function
    """
    l_parenthesis_idx = line.find('(')
    r_parenthesis_idx = line.find(')')
    # not include ( and )
    return line[l_parenthesis_idx+1:r_parenthesis_idx]


def get_name(line):
    """
    if is leaf
        get name in [some name]
    else
        get name directly use split
    """
    if is_leaf(line):
        l_bracket_idx = line.find('[')
        r_bracket_idx = line.find(']')
        # not include [ and ]
        name = line[l_bracket_idx+1:r_bracket_idx]
    else:
        name = line.split()[-1]
    return name


def get_level(line):
    """
    start from 1
    README.md is in first level
    """
    idx = len(line) - len(line.lstrip()) # get_first_idx_not_of_whitespace
    if idx == 0:
        return 1
    else:
        return idx // 2 + 1


def find_child_node_in_children_list(children_list, name):
    for child in children_list:
        if child and child['name'] == name:
            return child
    return None


def api_err(status_code, error_msg):
    err_resp = {'error_msg': error_msg}
    return Response(err_resp, status=status_code)
