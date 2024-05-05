bool containsDuplicate(int* nums, int numsSize) {
    // nums == array

    bool hash[] = {false};
    for (int i = 0; i < numsSize; i++) {
        if (hash[nums[i+1000000000]] == true) {
            return true;
        }
        hash[nums[i+1000000000]] = true;
    }
    return false;
}