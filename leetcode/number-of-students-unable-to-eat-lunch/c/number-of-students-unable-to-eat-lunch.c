typedef struct Node {
    int val;
    struct Node* next;
    struct Node* prev;
} Node;

typedef struct Queue {
    Node* front;
    Node* rear;
    int count;
} Queue;

typedef struct Stack {
    Node* head;
    Node* tail;
} Stack;

Node* createNode(int val) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->val = val;
    newNode->next = NULL;
    newNode->prev = NULL;

    return newNode;
}

void push(Stack* stack, int val) {
    Node* newNode = createNode(val);
    if (stack->head == NULL) {
        stack->head = newNode;
        stack->tail = newNode;
    } else {
        stack->tail->next = newNode;
        newNode->prev = stack->tail;
        stack->tail = newNode;
    }
}

int pop(Stack* stack) {
    int num;
    if (stack->head == NULL) {
        return -1;
    } else {
        Node* tailNode = stack->tail;
        num = tailNode->val;
        if (stack->head == stack->tail) {
            stack->head = NULL;
            stack->tail = NULL;
        } else {
            tailNode->prev->next = NULL;
            stack->tail = tailNode->prev;
            tailNode->prev = NULL;
        }
        free(tailNode);
        return num;
    } 
}

void enqueue(Queue* queue, int val) {
    Node* newNode = createNode(val);
    if (queue->front == NULL) {
        queue->front = newNode;
        queue->rear = newNode;
    } else {
        Node* rearNode = queue->rear;
        rearNode->next = newNode;
        newNode->prev = rearNode;
        queue->rear = newNode;
    }

    queue->count += 1;
}

int dequeue(Queue* queue) {
    int num;
    if (queue->front == NULL) {
        return -1;
    } else  {
        Node* frontNode = queue->front;
        num = frontNode->val;
        if (queue->front == queue->rear) {
            queue->front = NULL;
            queue->rear = NULL;
        } else {
            frontNode->next->prev = NULL;
            queue->front = frontNode->next;
            frontNode->next = NULL;
        }
        free(frontNode);
        queue->count -= 1;
        return num;
    }

}


int countStudents(int* students, int studentsSize, int* sandwiches, int sandwichesSize) {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->head = NULL;
    stack->tail = NULL;
    for (int i = sandwichesSize-1; i >= 0; i--) {
        push(stack, sandwiches[i]);
    }

    Queue* queue = (Queue*)malloc(sizeof(Queue));
    queue->front = NULL;
    queue->rear = NULL;
    queue->count = 0;

    for (int i = 0; i < studentsSize; i++) {
        enqueue(queue, students[i]);
    }

    bool flag = true;
    int loopCnt;
    while (flag) {
        loopCnt = 0;
        for (int i = 0; i < queue->count; i++) {
            if (queue->front->val == stack->tail->val) {
                pop(stack);
                dequeue(queue);
                loopCnt = 0;
                break;
            } else {
                int student = dequeue(queue);
                enqueue(queue, student);
                loopCnt += 1;
            }
        }
        if (loopCnt == queue->count || queue->count == 0) {
            flag = false;
        }
    }
    
    return queue->count;
}
