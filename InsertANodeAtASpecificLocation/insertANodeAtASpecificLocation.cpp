

/*
 * Complete the 'insertNodeAtPosition' function below.
 *
 * The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
 * The function accepts following parameters:
 *  1. INTEGER_SINGLY_LINKED_LIST llist
 *  2. INTEGER data
 *  3. INTEGER position
 */

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */

SinglyLinkedListNode* insertNodeAtPosition
(
        SinglyLinkedListNode* linkedListNode
        , int data
        , int position
)
{
    auto currentNode = linkedListNode;

    for (auto index=0; index < position-1; index++)
    {
        currentNode = currentNode->next;
    }

    auto node = new SinglyLinkedListNode(data);
    node->next = currentNode->next;
    currentNode->next = node;
    return linkedListNode;
}

