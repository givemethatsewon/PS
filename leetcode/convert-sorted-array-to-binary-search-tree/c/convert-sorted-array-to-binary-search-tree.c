
struct TreeNode* createTreeNode(int val) {
    struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->val = val;
    newNode->left = NULL;
    newNode->right = NULL;

    return newNode;
}


struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    if (numsSize == 0) {
        return NULL;
    }

    int mid = numsSize / 2 ;
    struct TreeNode* root = createTreeNode(nums[mid]);

    int leftSize = mid;
    int rightSize = numsSize - mid - 1;

    if (leftSize > 0) {
        int* lhs = (int*)malloc(sizeof(int) * leftSize);
        for (int i = 0; i < leftSize; i++) {
            lhs[i] = nums[i];
        }
        root->left = sortedArrayToBST(lhs, leftSize);
        free(lhs);
    } else {
        root->left = NULL;
    }

    if (rightSize > 0) {
        int* rhs = (int*)malloc(sizeof(int) * rightSize);
        for (int j = 0; j < rightSize; j++) {
            rhs[j] = nums[mid + 1 + j];
        }
        root->right = sortedArrayToBST(rhs, rightSize);
        free(rhs);
    } else {
        root->right = NULL;
    }



    return root;

}