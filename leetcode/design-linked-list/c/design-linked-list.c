typedef struct Node {
    int val;
    struct Node* next;
} Node;

typedef struct MyLinkedList{
    struct Node* head;
    int length;
} MyLinkedList;

Node* myNodeCreate(int val) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->val = val;
    newNode->next = NULL;

    return newNode; 
}

MyLinkedList* myLinkedListCreate() {
    MyLinkedList* linkedList = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    linkedList->head = NULL;
    linkedList->length = 0;

    return linkedList;
}

// return val of the index th node int the linked list 
int myLinkedListGet(MyLinkedList* obj, int index) {
    if (!obj) return -1;
    
    Node* current = obj->head;

    while (current != NULL && index--) {
        current = current->next;
    }
    if (current == NULL) {
        return -1;
    }
    return current->val;
}

// Add a node before the first node with val
void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    Node* newNode = myNodeCreate(val);
    obj->length += 1;

    if (obj->head == NULL) {
        obj->head = newNode;
        return;
    }
    newNode->next = obj->head;
    obj->head = newNode;
}

// Append a node after tail
void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    Node* newNode = myNodeCreate(val);
    obj->length += 1;

    if (obj->head == NULL) {
        obj->head = newNode;
        return;
    } 

    Node* current = obj->head;

    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
}

// add a node before the indexth node
// if index equals the length of linked list, append
// if index is greater than the length, do nothing
void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    if (obj->length == index) {
        myLinkedListAddAtTail(obj, val);
        return;
    }
    else if (index == 0) {
        myLinkedListAddAtHead(obj, val);
        return;
    } 
    else if (obj->length < index+1) {
        return;
    } 
    else {
        Node* newNode = myNodeCreate(val);

        Node* current = obj->head;
        Node* prev = NULL;

        while (current != NULL && index--) {
            prev = current;
            current = current->next;
        }
        prev->next = newNode;
        newNode->next = current;
        obj->length += 1;
    }
}

// delete the index th node in the linked list, if the index is valid
void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    if (obj->length < index+1) {
        return;
    } else {
        if (index == 0) {
            Node* temp = obj->head;
            obj->head = obj->head->next;
            obj->length--;
            return;
        }

        Node* current = obj->head;
        Node* prev = NULL;

        while(current != NULL && index--) {
            prev = current;
            current = current->next;
        }
        if (current == NULL) {
            prev->next = NULL;
            obj->head = prev;
        } else {
            prev->next = current->next;
        }
        obj->length -= 1;
    }
    }


void myLinkedListFree(MyLinkedList* obj) {
    MyLinkedList* temp;
    Node* current = obj->head;
    while (current) {
        temp = current;
        current = current->next;
        free(temp);
    }
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);
 
 * myLinkedListAddAtHead(obj, val);
 
 * myLinkedListAddAtTail(obj, val);
 
 * myLinkedListAddAtIndex(obj, index, val);
 
 * myLinkedListDeleteAtIndex(obj, index);
 
 * myLinkedListFree(obj);
*/