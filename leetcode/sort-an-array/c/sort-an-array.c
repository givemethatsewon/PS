/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void merge(int* arr, int s, int m, int e) {
    int i, j, k;
    int leftLen = m - s + 1;
    int rightLen = e - m; // e - (m - 1) + 1
    int* leftArr = (int*)malloc(sizeof(int) * leftLen);
    int* rightArr = (int*)malloc(sizeof(int) * rightLen);

    for (i = 0; i < leftLen; i++) {
        leftArr[i] = arr[s + i];
    }
    for (j = 0; j < rightLen; j++) {
        rightArr[j] = arr[m + 1 + j]; 
    }
    // two pointer
    i = 0; // index for left
    j = 0; // index for right
    k = s; // insex for arr
    
    while ((i < leftLen) && (j < rightLen)) {
        if (leftArr[i] > rightArr[j]) {
            arr[k++] = rightArr[j++];
        }
        else {
            arr[k++] = leftArr[i++];
        }
    }

    //handle remaining part
    while (i < leftLen) {
        arr[k++] = leftArr[i++];
    }
    while (j < rightLen) {
        arr[k++] = rightArr[j++];
    }
    free(leftArr);
    free(rightArr);
}

void mergeSort(int* arr, int s, int e) {
    if (s < e) {
        int m = (s + e) / 2;
        mergeSort(arr, s, m);
        mergeSort(arr, m+1, e);
        merge(arr, s, m, e);
    }
}

int* sortArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;

    mergeSort(nums, 0, numsSize - 1);
    return nums;
}