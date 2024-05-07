/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void merge(int* arr, int s, int m, int e) {
    int i, j, k;
    int leftLen = m - s + 1;
    int rightLen = e - m;
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
            arr[k] = rightArr[j];
            j++;
        }
        else {
            arr[k] = leftArr[i];
            i++;
        }
        k++;
    }

    //handle remaining part
    while (i < leftLen) {
        arr[k] = leftArr[i];
        k++;
        i++;
    }
    while (j < rightLen) {
        arr[k] = rightArr[j];
        k++;
        j++;
    }
    free(leftArr);
    free(rightArr);
}

int* mergeSort(int* arr, int s, int e) {
    if (e - s <= 0) {
        return arr;
    }
    int m = (s + e) / 2;
    mergeSort(arr, s, m);
    mergeSort(arr, m+1, e);

    merge(arr, s, m, e);
    
    return arr;
}

int* sortArray(int* nums, int numsSize, int* returnSize) {
    int* sortedArr = (int*)malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;

    for (int i = 0; i < numsSize; i++) {
        sortedArr[i] = nums[i];
    }
    
    mergeSort(sortedArr, 0, numsSize - 1);

    return sortedArr;
}