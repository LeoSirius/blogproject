import os

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from doctree_server.utils import *



class DocTreeView(APIView):

    def get(self, request):
        doc_tree = {}
        doc_tree['children'] = []
        summary_path = os.path.join(settings.DOC_REPO_PATH, 'notes/summary.md')
        non_leaf_ancestors = []
        with open(summary_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                # skip lines which contain only '\n'
                if len(line) <= 1:
                    continue
                if line.lstrip()[0] not in ['-', '*']:
                    continue
                name = get_name(line)
                node = {}
                node['name'] = name

                level = get_level(line)

                if is_leaf(line):
                    node['path'] = get_path(line)
                    if level == 1:
                        doc_tree['children'].append(node)
                        non_leaf_ancestors = [name]
                        continue
                    for ancestor in non_leaf_ancestors:
                        print('ancestor = {}'.format(ancestor))
                        print('parent_node = {}'.format(parent_node))
                        child_node = find_child_node_in_children_list(parent_node['children'], ancestor)
                        if child_node:
                            parent_node = child_node
                        else:
                            parent_node['children'].append(node)
                else:
                    node['children'] = []
                    if level == 1:
                        doc_tree['children'].append(node)
                        non_leaf_ancestors = [name]
                        continue
                    non_leaf_ancestors = non_leaf_ancestors[:level - 1]  # back to parent
                    non_leaf_ancestors.append(name)

                    # not root, add node to its parent
                    parent_node = doc_tree
                    for ancestor in non_leaf_ancestors:
                        print('ancestor = {}'.format(ancestor))
                        print('parent_node = {}'.format(parent_node))
                        child_node = find_child_node_in_children_list(parent_node['children'], ancestor)
                        if child_node:
                            parent_node = child_node
                        else:
                            parent_node['children'].append(node)

                print('====')
        print('doc_tree = {}'.format(doc_tree))

        return Response({'doctree': doc_tree})
