class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class singleLinkedlist:
    def __init__(self):
        self.head = None

    def add_to_begining(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        new.next = self.head
        self.head = new

    def add_to_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new

    def insert_at_pos(self, data, pos):
        new = Node(data)
        if pos <= 0:
            print("Invalid Position")
            return
        if pos == 1:
            new.next = self.head
            self.head = new
            return
        temp = self.head
        i = 1
        while i < pos - 1 and temp is not None:
            temp = temp.next
            i += 1
        if temp is None:
            print("Invalid Position")
            return
        new.next = temp.next
        temp.next = new

    def delete_beginning(self):
        if self.head is None:
            print("Playlist is empty")
            return
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Playlist is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_at_pos(self, pos):
        if self.head is None:
            print("Playlist is empty")
            return
        if pos <= 0:
            print("Invalid Position")
            return
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        prev = None
        i = 1
        while i < pos and temp is not None:
            prev = temp
            temp = temp.next
            i += 1
        if temp is None:
            print("Invalid Position")
            return
        prev.next = temp.next

    def search(self, data):
        temp = self.head
        pos = 1
        while temp is not None:
            if temp.data == data:
                print("Song found at position", pos)
                return
            temp = temp.next
            pos += 1
        print("Song not found")

    def count(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        print("Total number of songs:", count)

    def display(self):
        if self.head is None:
            print("Playlist is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):
        prev = None
        temp = self.head
        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

playlist = singleLinkedlist()

while True:

    print("\n----- PLAYLIST MENU -----")
    print("1. Add a song to the beginning")
    print("2. Add a song to the end")
    print("3. Insert a song at a position")
    print("4. Remove the first song")
    print("5. Remove the last song")
    print("6. Remove song at a position")
    print("7. Search for a song")
    print("8. Display total number of songs")
    print("9. Display complete playlist")
    print("10. Reverse the playlist")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        song = input("Enter song name: ")
        playlist.add_to_begining(song)

    elif choice == 2:
        song = input("Enter song name: ")
        playlist.add_to_end(song)

    elif choice == 3:
        song = input("Enter song name: ")
        pos = int(input("Enter position: "))
        playlist.insert_at_pos(song, pos)

    elif choice == 4:
        playlist.delete_beginning()

    elif choice == 5:
        playlist.delete_end()

    elif choice == 6:
        pos = int(input("Enter position: "))
        playlist.delete_at_pos(pos)

    elif choice == 7:
        song = input("Enter song name to search: ")
        playlist.search(song)

    elif choice == 8:
        playlist.count()

    elif choice == 9:
        playlist.display()

    elif choice == 10:
        playlist.reverse()
        print("Playlist reversed")

    elif choice == 11:
        print("Exiting application...")
        break

    else:
        print("Invalid choice")
