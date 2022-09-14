class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def DFS(node, row, column):
            if node is not None:
                node_list.append((column, row, node.val))
                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        # step 1). construct the node list, with the coordinates
        DFS(root, 0, 0)

        # step 2). sort the node list globally, according to the coordinates
        node_list.sort(key = lambda x:(x[0],x[1],x[2]))

        # step 3). retrieve the sorted results grouped by the column index
        ret = []
        curr_column_index = node_list[0][0]
        curr_column = []
        print(node_list)
        hmap = defaultdict(list)
        # node.list.
        for value in node_list:
            hmap[value[0]].append(value[2])
            
        return list(hmap.values())
            