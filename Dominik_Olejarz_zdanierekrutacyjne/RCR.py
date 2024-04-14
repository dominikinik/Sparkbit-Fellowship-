# Tree structure
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)


class RoboticCodeRepresentationGenerator:

    def __init__(self, issued_commands: list[str]):
        assert len(issued_commands) > 0, "List of commands is empty"
        self.issued_commands = issued_commands
        self.frequency = self.make_frequency()
        self.nodes = self.MakeNodes()
        self.huffmanCode = self.huffman_code_tree(self.nodes[0][0])

    def huffman_code_tree(self, node, left=True, coding=""):
        if type(node) is str:
            return {node: coding}
        (l, r) = node.children()
        d = dict()
        d.update(self.huffman_code_tree(l, True, coding + "0"))
        d.update(self.huffman_code_tree(r, False, coding + "1"))
        return d

    def MakeNodes(self) -> list[NodeTree]:
        nodes = self.frequency
        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))

            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        return nodes

    def get_rcr(self, command: str) -> str:
        return self.huffmanCode[command]

    def make_frequency(self) -> dict[str, int]:
        freq = {}
        for c in self.issued_commands:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return freq
