#include <stdlib.h>
#include <stdbool.h>   

bool isBSTNode(struct TreeNode* root, long min, long max) {
    if (!root) return true;


    if (root->val <= min || root->val >= max) {
        return false;
    }
    return isBSTNode(root->left, min, root->val) && isBSTNode(root->right, root->val, max);
}

bool isValidBST(struct TreeNode* root) {
    return isBSTNode(root->left, LONG_MIN, root->val) && isBSTNode(root->right, root->val, LONG_MAX);
}


