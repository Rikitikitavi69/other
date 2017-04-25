"""
	Двоичное дерево поиска

В заданном двоичном дереве поиска с дубликатами найдите все наиболее часто встречающиеся элементы.

Считайте, что двоичное дерево поиска определено следующим образом:
Левое поддерево узла состоит только из узлов с ключами, меньшими либо равными ключу данного узла.
Правое поддерево узла состоит только из узлов с ключами, большими либо равными ключу данного узла.
Левое поддерево и правое поддерево также являются двоичными деревьями поиска.
Примечание: в случае, если наиболее часто встречающихся элементов более одного, их можно возвращать в любом порядке.

Например, для дерева
  1
    \
     2
    /
   2
результат [2]
Элемент двоичного дерева поиска на Java описывается вот таким классом:
public class Node {
    public final int val;
    public final Node left;
    public final Node right;

    Node(int x) { val = x; }
}
"""

def tree2list(Node):
	if (Node.left == None and Node.right == None):
		return [Node.val]
	elif (Node.left != None and Node.right != None):
		return [Node.val] + tree2list(Node.left) + tree2list(Node.right)
	elif (Node.left == None):
		return [Node.val] + tree2list(Node.right)
	else:
		return [Node.val] + tree2list(Node.left)

def count_duplicates(Node):
	l = tree2list(Node)
	d = {x:l.count(x) for x in l}
	return [key for key in d.keys() if d[key] > 1]
