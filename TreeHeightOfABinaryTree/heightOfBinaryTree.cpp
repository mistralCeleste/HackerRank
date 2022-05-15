#include <bits/stdc++.h>

using namespace std;

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
    Node* insert(Node* root, int data) {
        if(root == NULL) {
            return new Node(data);
        } else {
            Node* cur;
            if(data <= root->data) {
                cur = insert(root->left, data);
                root->left = cur;
            } else {
                cur = insert(root->right, data);
                root->right = cur;
            }

            return root;
        }
    }
/*The tree node has data, left child and right child
class Node {
    int data;
    Node* left;
    Node* right;
};

*/
    bool nodeExists(Node* node)
    {
        return nullptr != node;
    }

    int height(Node* root)
    {
        auto leftHeight = 0;
        auto rightHeight = 0;

        if (nodeExists(root->left))
        {
            leftHeight = height(root->left) + 1;
        }

        if (nodeExists(root->right))
        {
            rightHeight = height(root->right) + 1;
        }

        auto count = leftHeight > rightHeight
                     ? leftHeight
                     : rightHeight;

        return count;
    }

}; //End of Solution