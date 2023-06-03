#include<iostream>
using namespace std;

class Node {
public:
    int data;
    Node* left;
    Node* right;
    bool isThreaded;
    Node(int data) {
        this->data = data;
        left = right = nullptr;
        isThreaded = false;
    }
};

// Converts tree with given root to threaded
// binary tree.
// This function returns rightmost child of
// root.
Node* createThreaded(Node* root) {
    if (root == nullptr)
        return nullptr;
    if (root->left == nullptr && root->right == nullptr)
        return root;

    // Find predecessor if it exists
    if (root->left != nullptr) {
        // Find predecessor of root (Rightmost
        // child in left subtree)
        Node* l = createThreaded(root->left);

        // Link a thread from predecessor
        // to root.
        l->right = root;
        l->isThreaded = true;
    }

    // If current node is rightmost child
    if (root->right == nullptr)
        return root;

    // Recur for right subtree.
    return createThreaded(root->right);
}

// find the leftmost node
Node* leftMost(Node* root) {
    while (root != nullptr && root->left != nullptr)
        root = root->left;
    return root;
}

// Function to do inorder traversal of a
// threaded binary tree
void inOrder(Node* root) {
    if (root == nullptr)
        return;

    // Find the leftmost node in Binary Tree
    Node* cur = leftMost(root);

    while (cur != nullptr) {
        cout << cur->data << " ";

        // If this Node is a thread Node, then
        // go to inorder successor
        if (cur->isThreaded)
            cur = cur->right;

        // Else go to the leftmost child in right subtree
        else
            cur = leftMost(cur->right);
    }
}

// Driver Code
int main() {
    /*
     *        1
     *       / \
     *      2   3
     *     / \ / \
     *    4  5 6  7
     */
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);

    createThreaded(root);
    cout << "Inorder traversal of created threaded tree is" << endl;
    inOrder(root);
    return 0;
}