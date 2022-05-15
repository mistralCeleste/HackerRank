#include <iostream>
#include <cstddef>

class Node {
public:
    int data;
    Node *left;
    Node *right;
    Node(int d) {
        data = d;
        left = NULL;
        right = NULL;
    }
};

class Solution {
public:

    void preOrder(Node *root) {

        if( root == NULL )
            return;

        std::cout << root->data << " ";

        preOrder(root->left);
        preOrder(root->right);
    }

/* you only have to complete the function given below.
Node is defined as

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

*/

    Node* insert(Node *root, int data)
    {
        auto node = new Node(data);

        if (root == nullptr)
        {
            return node;
        }

        Node *previous = nullptr;
        auto current = root;

        while (current != nullptr)
        {
            if (data < current->data)
            {
                previous = current;
                current = current->left;
            }
            else if (data > current->data)
            {
                previous = current;
                current = current->right;
            }
        }

        if (data < previous->data)
        {
            previous->left = node;
        }
        else if (data > previous->data)
        {
            previous->right = node;
        }

        return root;
    }
}; //End of Solution

int main() {

    Solution myTree;
    Node* root = NULL;

    int t;
    int data;

    std::cin >> t;

    while(t-- > 0) {
        std::cin >> data;
        root = myTree.insert(root, data);
    }
    myTree.preOrder(root);
    return 0;
}
