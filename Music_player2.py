##Kabunga Akram JOshua M25B38/004
## Kibirige Samuel M25B38/034
## Namanya Hannah Brenda M25B38/043
## Abi Mirembe Kigozi M25B38/022
## Obar Daniel M25B38/014
from collections import deque

class Stack:  # Capitalized for style points
    def __init__(self): ## This is initialised when a class is originally created in python. The self part stands for the object being created
        self.songs_list = []
    
    def push(self, song):
        self.songs_list.append(song)
        print(f"The song {song} has been played")
    
    def pop(self):
        if not self.songs_list:
            print("You have no previous songs")
        else:
            song = self.songs_list.pop()
            print(f"The song {song} was the last 🎶")
    
    def display(self):  # New display method
        if not self.songs_list:
            print("Stack’s empty")
        else:
            print("Recently played (stack):")
            for song in reversed(self.songs_list):  # Show newest first
                print(f"- {song}")

class Queue:
    def __init__(self):
        self.queue = deque()##creates a double end queue.
    
    def enqueue(self, song):
        self.queue.append(song)
        print(f"{song} has been added to queue")
    
    def dequeue(self):
        if not self.queue:
            print("The playlist is empty")
        else:
            song = self.queue.popleft()
            print(f"The song playing is {song}")
            return song
    
    def display(self):  # New display method
        if not self.queue:
            print("Queue’s empty, no vibes")
        else:
            print("Up next (queue):")
            for song in self.queue:
                print(f"- {song}")

class Node:##For our songs and their connecters
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None##our  playlist is empty, starts out empty
    
    def song_add(self, song):
        new_connection = Node(song)
        if not self.head:## checks if the playlist is empty
            self.head = new_connection## checks if the playlist is empty
            new_connection.next = new_connection#this is where the circular link in the list happens
            new_connection.prev = new_connection
        else:
            tail = self.head.prev
            tail.next = new_connection
            new_connection.prev = tail
            new_connection.next = self.head
            self.head.prev = new_connection
        print(f"{song} added to your loop playlist 🔁")
    
    def display(self, count=5):
        if not self.head:##where the playlist starts being displayed
            print("Nothing here to see 😶")
            return
        current = self.head
        played_songs = set()##avoids looping the circular loop infinitely
        print("Your playlist loop:")
        for _ in range(min(count, len(played_songs))):  # Limit to count or playlist size
            if not current or current.song in played_songs:
                break
            print(f"{current.song}", end=" ---> ")
            played_songs.add(current.song)
            current = current.next
        print("... back to the start 🔄")

def main():
    stack = Stack()
    queue = Queue()
    playlist = Playlist()
    print("🎧 Welcome to your lit music manager!")
    
    while True:
        print("\nWhat’s the vibe? Pick an option:")
        print("1. Add a song to the stack 🥞")
        print("2. Pop a song from the stack")
        print("3. Add a song to the queue 🎧")
        print("4. Play (dequeue) a song from the queue")
        print("5. Add a song to the playlist 🔁")
        print("6. Show the playlist")
        print("7. Show the stack")
        print("8. Show the queue 📋")
        print("9. Get outta here")
        choice = input("Enter option 1-9: ").strip().lower()  # Handle sloppy inputs
        
        if choice == "1":
            song = input("Drop the song name for the stack: ").strip()
            if not song:
                print("You didn’t type a song. Try again, bestie")
            else:
                stack.push(song)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            song = input("Drop the song name for the queue: ").strip()
            if not song:
                print("You didn’t type a song. Try again, bestie")
            else:
                queue.enqueue(song)
        elif choice == "4":
            queue.dequeue()
        elif choice == "5":
            song = input("Drop the song name for the playlist: ").strip()
            if not song:
                print("You didn’t type a song. Try again")
            else:
                playlist.song_add(song)
        elif choice == "6":
            playlist.display()
        elif choice == "7":
            stack.display()
        elif choice == "8":
            queue.display()
        elif choice == "9":
            print("Peace out. Enjoy your tunes")
            break
        else:
            print("That’s not a valid option. Pick 1-9, don’t make it weird")

if __name__ == "__main__":
    main()