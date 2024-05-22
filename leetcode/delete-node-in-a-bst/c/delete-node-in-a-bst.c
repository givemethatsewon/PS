#include <stdlib.h>

// Definition for a binary tree node.
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };

// Helper function to find the minimum node in the right subtree
struct TreeNode* findMinNode(struct TreeNode* root) {
    struct TreeNode* current = root;
    while (current && current->left) {
        current = current->left;
    }
    return current;
}

struct TreeNode* deleteNode(struct TreeNode* root, int key) {
    if (!root) {
        return NULL;
    }
    
    // Find the node to delete
    if (key < root->val) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->val) {
        root->right = deleteNode(root->right, key);
    } else {
        // Node to be deleted is found

        // Node with only one child or no child
        if (root->left == NULL) {
            struct TreeNode* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct TreeNode* temp = root->left;
            free(root);
            return temp;
        } else {
            // Node with two children: Get the inorder successor (smallest in the right subtree)
            struct TreeNode* temp = findMinNode(root->right);

            // Copy the inorder successor's value to this node
            root->val = temp->val;

            // Delete the inorder successor
            root->right = deleteNode(root->right, temp->val);
        }
    }

    return root;
}
