#include <stdlib.h>

typedef struct {
    int heap[100001];
    int heap_size;
} heapType;

heapType* createHeap() {
    heapType* newHeap = (heapType*)malloc(sizeof(heapType));
    newHeap->heap_size = 0;
    return newHeap;
}

int topHeap(heapType* h) {
    return h->heap[1];
}

int popHeap(heapType* h) {
    int item = h->heap[1];
    int lastItem = h->heap[h->heap_size]; // 고르고 1 감소
    h->heap_size -= 1;

    int parent = 1, child = 2;
    while (child <= h->heap_size) {
        if (child < h->heap_size && h->heap[child] < h->heap[child + 1]) {
            child++;
        }
        if (lastItem > h->heap[child]) { // 마지막 아이템이 자식보다 크면 break
            break;
        }
        h->heap[parent] = h->heap[child]; // 자식이 크면 부모에 자식을 넣는다.(max heap)
        parent = child;
        child = child * 2;
    }
    h->heap[parent] = lastItem;

    return item;
}

void pushHeap(heapType* h, int item) {
    h->heap_size += 1;
    int i = h->heap_size;

    while ((i != 1) && (item > h->heap[i / 2])) {
        h->heap[i] = h->heap[i / 2];
        i = i / 2;
    }
    h->heap[i] = item;
}


int findKthLargest(int* nums, int numsSize, int k) {
    heapType* numHeap = createHeap();
    for (int i = 0; i < numsSize; i++) {
        pushHeap(numHeap, nums[i]);
    }
    for (int i = 1; i < k; i++) {
        popHeap(numHeap);
    }

    int ans = popHeap(numHeap);
    free(numHeap);
    return ans;

}
