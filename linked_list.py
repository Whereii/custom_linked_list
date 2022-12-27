class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Linked_List:
    def __init__(self):
        self.first = 0
        self.last = 0
        self.size = 0

    def add_first(self, value):
        new_node = Node(value, 0)
        if self.first == 0:
            self.first = new_node
            self.last = new_node
            self.size += 1
        else:
            new_node.next = self.first
            self.first = new_node
            self.size += 1

    def print(self):
        if self.first == 0:
            raise Exception('NoSuchElementException()')
        holder = self.first
        cycle = True
        while cycle:
            print(holder.value)
            if holder.next == 0:
                cycle = False
            else: holder = holder.next

    def add_last(self, value):
        new_node = Node(value, 0)
        if self.first == 0:
            self.first = self.last = new_node
            self.size += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.size += 1

    def delete_first(self):
        if self.first == 0:
            raise Exception('NoSuchElementException()')
        if self.first == self.last:
            self.first = self.last = 0
            self.size -= 1
            return
        holder = self.first
        self.first = self.first.next
        holder.next = 0
        self.size -= 1

    def delete_last(self):
        if self.first == 0:
            raise Exception('NoSuchElementException()')
        if self.first == self.last:
            self.first = self.last = 0
            self.size -= 1
            return
        holder = self.first
        cycle = True
        while cycle:
            if holder.next == self.last:
                del holder.next
                holder.next = 0
                self.last = holder
                self.size -= 1
                cycle = False
            else:
                holder = holder.next

    def contains(self, num):
        holder = self.first
        cycle = True
        while cycle:
            if holder.value == num:
                return True
            else:
                holder = holder.next
            if holder == self.last:
                return False

    def index_of(self, num):
        if self.first == 0:
            raise Exception('NoSuchElementException()')
        holder = self.first
        index = 0
        cycle = True
        while cycle:
            if holder.value == num:
                return index
            if holder == self.last:
                return -1
            holder = holder.next
            index += 1

    def to_array(self):
        array = []
        holder = self.first
        cycle = True
        while cycle:
            if self.first == 0:
                raise Exception('NoSuchElementException()')
            if holder == self.last:
                array.append(holder.value)
                return array
            else:
                array.append(holder.value)
                holder = holder.next

    def reverse(self):
        holder = self.first
        self.first = self.last
        self.last = holder
        holder = self.last
        holder_forward = 0
        holder_backwards = 0
        cycle = True
        while cycle:
            if self.first == 0:
                return
            if self.first == self.last:
                return self.first
            if holder == self.last:
                holder_backwards = holder
                holder = holder.next
                holder_backwards.next = 0
                continue
            if holder == self.first:
                self.first.next = holder_backwards
                cycle = False
            else:
                holder_forward = holder.next
                holder.next = holder_backwards
                holder_backwards = holder
                holder = holder_forward
                
    def return_kth_node(self, num):
        holder = self.first
        index = self.size - num
        if index < 0 or num < 1:
            raise Exception('invalidNumber') 
        for i in range(index + 1):
            if i < index:
                holder = holder.next
                continue
            return holder.value

    def return_middle(self):
        searcher = self.first
        finder = self.first
        middle = 0
        counter = 1
        while searcher.next != 0:
            searcher = searcher.next
            counter +=1
            if searcher.next != 0:
                searcher = searcher.next
                finder = finder.next
                counter += 1
        if counter % 2 == 0:
            middle = finder.value + finder.next.value
        else:
            middle = finder.value
        return middle

    def has_loop(self):
        fast = self.first.next
        slow = self.first
        while fast != slow:
            fast = fast.next
            if fast == 0:
                return 'Has no loop'
            fast = fast.next
            if fast == 0:
                return 'Has no loop'
            slow = slow.next
        return 'There is a loop'