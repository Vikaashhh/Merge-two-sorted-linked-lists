class Solution:
    def sortedMerge(self, head1, head2):
        # Dummy node banate hain jisse final merged list start hogi
        dummy = Node(0)
        tail = dummy  # Tail pointer jahan se naye nodes append honge
        
        # Jab tak dono lists mein nodes hain
        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1  # head1 ka node attach karo
                head1 = head1.next
            else:
                tail.next = head2  # head2 ka node attach karo
                head2 = head2.next
            tail = tail.next  # Tail ko aage badhao

        # Agar koi list khatam ho gayi ho, toh dusri list ke remaining nodes attach karo
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        
        return dummy.next  # Dummy ke next se actual merged list start hoti hai
