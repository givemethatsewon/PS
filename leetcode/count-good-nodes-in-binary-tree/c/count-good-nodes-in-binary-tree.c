int travel(struct TreeNode* node, int preMax) {
    if (!node) return 0;

    int count = 0;
    if (node->val >= preMax) {
        count += 1;
        preMax = node->val;
    } 

    count += travel(node->left, preMax);
    count += travel(node->right, preMax);
    
    return count;
}

int goodNodes(struct TreeNode* root){

    return travel(root, root->val);
}