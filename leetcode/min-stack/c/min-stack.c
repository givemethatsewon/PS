typedef struct Node {
    struct Node* prev;
    struct Node* next;
    int val;
} Node;


typedef struct {
    struct Node* head;
    struct Node* tail;
} MinStack;

Node* nodeCreate(int val) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->val = val;
    newNode->prev = NULL;
    newNode->next = NULL;

    return newNode;
} 

MinStack* minStackCreate() {
    MinStack* minStack = (MinStack*)malloc(sizeof(MinStack));
    minStack->head = NULL;
    minStack->tail = NULL;

    return minStack;
}

void minStackPush(MinStack* obj, int val) {
    Node* newNode = nodeCreate(val);
    if (obj->head == NULL || obj->tail == NULL) {
        obj->head = newNode;
        obj->tail = newNode;
    } else {
        obj->tail->next = newNode;
        newNode->prev = obj->tail;
        obj->tail = newNode;
    }
}

void minStackPop(MinStack* obj) {   
    Node* tailNode = NULL; 
    if (obj->head == obj->tail) {
        tailNode = obj->tail;
        obj->head = NULL;
        obj->tail = NULL;
    } else {
        tailNode = obj-> tail;
        tailNode->prev->next = NULL;
        obj->tail = tailNode->prev;
        tailNode->prev = NULL;
    }

    free(tailNode);
}

int minStackTop(MinStack* obj) {
    return obj->tail->val;
}

int minStackGetMin(MinStack* obj) {
    Node* head = obj->head;
    Node* current = head;
    int min = head->val;

    while (current != NULL) {
        if (current->val < min) {
            min = current->val;
        }
        current = current->next;
    }

    return min;
}

void minStackFree(MinStack* obj) {
    Node* nodes= obj->head;
    free(nodes);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/