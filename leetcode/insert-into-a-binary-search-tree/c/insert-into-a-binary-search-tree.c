/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* insertIntoBST(struct TreeNode* root, int val) {
    if (!root) {
        struct TreeNode* newTreeNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newTreeNode->val = val;
        newTreeNode->left = NULL;
        newTreeNode->right = NULL;
        return newTreeNode;
    }
    if (val < root->val) {
        root->left = insertIntoBST(root->left, val);
    } else if (root->val < val) {
        root->right = insertIntoBST(root->right, val);
    }
    return root;
}