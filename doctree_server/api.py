import os
from urllib.parse import unquote

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from doctree_server.utils import api_err, get_path, get_level, get_name, \
    is_leaf, find_child_node_in_children_list


class DocTreeView(APIView):

    def get(self, request):
        doc_tree = {}
        doc_tree['children'] = []
        summary_path = os.path.join(settings.DOC_REPO_PATH, 'summary.md')
        non_leaf_ancestors = []   # store ancestors from root node, e.g. ['编程语言','c','c和指针']
        with open(summary_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                # skip lines which contain only '\n'
                if len(line) <= 1:
                    continue
                # skip lines not started with - or *
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

                    # let parent_node point to closest ancestor of leaf, i.e. parent of leaf
                    for ancestor in non_leaf_ancestors:
                        child_node = find_child_node_in_children_list(parent_node['children'], ancestor)
                        if child_node:
                            parent_node = child_node
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
                        child_node = find_child_node_in_children_list(parent_node['children'], ancestor)
                        if child_node:
                            parent_node = child_node
                        else:
                            parent_node['children'].append(node)

        return Response({'doctree': doc_tree})


class DocContentView(APIView):

    def get(self, request, path):

        # params check
        file_path = os.path.join(settings.DOC_REPO_PATH, path)
        file_path = unquote(file_path)
        if not os.path.exists(file_path):
            error_msg = 'file "{}" not found.'.format(file_path)
            return api_err(status.HTTP_500_INTERNAL_SERVER_ERROR, error_msg)

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        return Response({'content': content})
