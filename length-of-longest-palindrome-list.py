class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LengthOfLongestPalindromicList:
    def cs(self, a, b):
        c=0
        while(a != None and b != None):
            if(a.val == b.val):
                a = a.next
                b = b.next
                c += 1
            else:
                break
        return c
    def solve(self, A):
        head = A
        current = head
        previous = None
        ans = 0
        while current != None:
            next = current.next
            current.next = previous
            ans = max(ans, 2 * self.cs(previous,next)+1) # Odd center
            ans = max(ans, 2 * self.cs(current, next)) # even
            previous = current
            current = next
        return ans

if __name__ == "__main__":
    headNode = Node(2)
    headNode.next = Node(2)
    print(LengthOfLongestPalindromicList().solve(headNode))