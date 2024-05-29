/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool hasPathSum(struct TreeNode* root, int targetSum) {
    if (!root) return false;

    targetSum -= root->val;
    
    if (!root->left && !root->right) {
        if (targetSum == 0) return true;
    }

    if (hasPathSum(root->left, targetSum)) return true;
    if (hasPathSum(root->right, targetSum)) return true;

    // root->left에도 없고 root->right에도 없을 경우
    return false;
}