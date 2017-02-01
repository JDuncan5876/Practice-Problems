void moveZeroes(int* nums, int numsSize) {
    int i = 0;
    int j;
    for (j = 0; j < numsSize; ++j) {
        if (*(nums + j)) {
            *(nums + i++) = *(nums + j);
        }
    }
    while (i < numsSize) {
        *(nums + i++) = 0;
    }
}