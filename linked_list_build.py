#pylint: disable=no-member
import linked_list

my_list = linked_list.Linked_List()


my_list.add_last(1)
my_list.add_last(2)
my_list.add_last(3)
my_list.add_last(4)
my_list.add_last(16)
my_list.add_last(2)
my_list.add_last(11)

print(my_list.return_middle())
print(my_list.has_loop())