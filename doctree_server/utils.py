def get_first_idx_not_of_whitespace(line):
    return len(line) - len(line.lstrip())
#
# def get_first_char_not_whitespace(line):
#     return line.lstrip()

def is_root_node(line):
    return line[0] in ['-', '*']


def is_leaf(line):
    return '(' in line and ')' in line and '[' in line and ']' in line


def get_path(line):
    l_parenthesis_idx = line.find('(')
    r_parenthesis_idx = line.find(')')
    # not include ( and )
    return line[l_parenthesis_idx+1:r_parenthesis_idx]


def get_ancestors_by_path(path):
    return path.split('/')[:-1]


def get_name(line):
    if is_leaf(line):
        l_bracket_idx = line.find('[')
        r_bracket_idx = line.find(']')
        # not include [ and ]
        name = line[l_bracket_idx+1:r_bracket_idx]
    else:
        name = line.split()[-1]
    return name

def find_child_node_in_children_list(children_list, name):
    for child in children_list:
        if child and child['name'] == name:
            return child
    return None

def get_level(line):
    idx = get_first_idx_not_of_whitespace(line)
    if idx == 0:
        return 1
    else:
        return idx // 2 + 1