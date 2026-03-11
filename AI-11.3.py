###Implement a Contact Manager using Array and Linked List with operations Add, Search, and Delete contacts, generate Search and Delete methods, and compare both approaches based on insertion and deletion efficiency.
# Contact Manager using Array and Linked List
'''class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def __repr__(self):
        return f"Contact({self.name}, {self.phone}, {self.email})"
# ===== ARRAY-BASED CONTACT MANAGER =====
class ArrayContactManager:
    def __init__(self):
        self.contacts = []
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Added: {contact}")
    def search(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    def delete(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts.pop(i)
                print(f"Deleted: {contact}")
                return True
        print(f"Contact '{name}' not found")
        return False
    def display_all(self):
        print("Array Contacts:", self.contacts)

# ===== LINKED LIST-BASED CONTACT MANAGER =====
class Node:
    def __init__(self, contact):
        self.contact = contact
        self.next = None
class LinkedListContactManager:
    def __init__(self):
        self.head = None
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        new_node = Node(contact)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Added: {contact}")
    def search(self, name):
        current = self.head
        while current:
            if current.contact.name == name:
                return current.contact
            current = current.next
        return None
    def delete(self, name):
        if not self.head:
            print(f"Contact '{name}' not found")
            return False
        if self.head.contact.name == name:
            contact = self.head.contact
            self.head = self.head.next
            print(f"Deleted: {contact}")
            return True
        current = self.head
        while current.next:
            if current.next.contact.name == name:
                contact = current.next.contact
                current.next = current.next.next
                print(f"Deleted: {contact}")
                return True
            current = current.next
        print(f"Contact '{name}' not found")
        return False
    def display_all(self):
        contacts = []
        current = self.head
        while current:
            contacts.append(current.contact)
            current = current.next
        print("Linked List Contacts:", contacts)
# ===== COMPARISON & DEMO =====
if __name__ == "__main__":
    print("=" * 60)
    print("ARRAY-BASED CONTACT MANAGER")
    print("=" * 60)
    array_mgr = ArrayContactManager()
    array_mgr.add("Alice", "123456", "alice@email.com")
    array_mgr.add("Bob", "789012", "bob@email.com")
    array_mgr.add("Charlie", "345678", "charlie@email.com")
    array_mgr.display_all()
    print("Search Alice:", array_mgr.search("Alice"))
    array_mgr.delete("Bob")
    array_mgr.display_all()
    print("\n" + "=" * 60)
    print("LINKED LIST-BASED CONTACT MANAGER")
    print("=" * 60)
    ll_mgr = LinkedListContactManager()
    ll_mgr.add("Alice", "123456", "alice@email.com")
    ll_mgr.add("Bob", "789012", "bob@email.com")
    ll_mgr.add("Charlie", "345678", "charlie@email.com")
    ll_mgr.display_all()
    print("Search Alice:", ll_mgr.search("Alice"))
    ll_mgr.delete("Bob")
    ll_mgr.display_all()
    print("\n" + "=" * 60)
    print("EFFICIENCY COMPARISON")
    print("=" * 60)
    print("Array:")
    print("  - Add: O(1) average")
    print("  - Search: O(n)")
    print("  - Delete: O(n) due to shifting elements")
    print("\nLinked List:")
    print("  - Add: O(n) to find end, O(1) to insert")
    print("  - Search: O(n)")
    print("  - Delete: O(n) to find, O(1) to remove")'''

#Justification: - The Array-based Contact Manager allows for O(1) average time complexity for adding contacts, - The Linked List-based Contact Manager allows for O(1) time complexity for adding contacts at the end.

    
##2.Implement a **Library Book Request System** using a **Queue (FIFO)** and **Priority Queue** where **faculty requests have higher priority than student requests**, generate **enqueue() and dequeue() methods using GitHub Copilot**, and **test with mixed student and faculty requests to verify correct prioritization.
'''class RequestType(Enum):
    STUDENT = 2
    FACULTY = 1

class BookRequest:
    def __init__(self, request_id, requester_name, book_title, request_type):
        self.request_id = request_id
        self.requester_name = requester_name
        self.book_title = book_title
        self.request_type = request_type
    
    def __lt__(self, other):
        return self.request_type.value < other.request_type.value
    
    def __repr__(self):
        return f"BookRequest(ID: {self.request_id}, {self.requester_name}, '{self.book_title}', {self.request_type.name})"

# ===== FIFO QUEUE =====
class FIFOQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, request):
        self.queue.append(request)
        print(f"Enqueued: {request}")
    
    def dequeue(self):
        if self.queue:
            request = self.queue.pop(0)
            print(f"Dequeued: {request}")
            return request
        print("Queue is empty")
        return None
    
    def display(self):
        print("FIFO Queue:", self.queue)

# ===== PRIORITY QUEUE =====
class PriorityQueueManager:
    def __init__(self):
        self.heap = []
        self.counter = 0
    
    def enqueue(self, request):
        heapq.heappush(self.heap, (request.request_type.value, self.counter, request))
        self.counter += 1
        print(f"Enqueued: {request}")
    
    def dequeue(self):
        if self.heap:
            _, _, request = heapq.heappop(self.heap)
            print(f"Dequeued: {request}")
            return request
        print("Priority Queue is empty")
        return None
    
    def display(self):
        requests = [req[2] for req in self.heap]
        print("Priority Queue:", requests)

# ===== DEMO & TESTING =====
if __name__ == "__main__":
    print("=" * 70)
    print("FIFO QUEUE - LIBRARY BOOK REQUEST SYSTEM")
    print("=" * 70)
    fifo = FIFOQueue()
    fifo.enqueue(BookRequest(1, "John (Student)", "Python Basics", RequestType.STUDENT))
    fifo.enqueue(BookRequest(2, "Dr. Smith (Faculty)", "AI Research", RequestType.FACULTY))
    fifo.enqueue(BookRequest(3, "Sarah (Student)", "Data Science", RequestType.STUDENT))
    fifo.display()
    print("\nProcessing requests:")
    fifo.dequeue()
    fifo.dequeue()
    fifo.display()
    
    print("\n" + "=" * 70)
    print("PRIORITY QUEUE - LIBRARY BOOK REQUEST SYSTEM")
    print("=" * 70)
    pq = PriorityQueueManager()
    pq.enqueue(BookRequest(1, "John (Student)", "Python Basics", RequestType.STUDENT))
    pq.enqueue(BookRequest(2, "Dr. Smith (Faculty)", "AI Research", RequestType.FACULTY))
    pq.enqueue(BookRequest(3, "Sarah (Student)", "Data Science", RequestType.STUDENT))
    pq.enqueue(BookRequest(4, "Prof. Johnson (Faculty)", "ML Advanced", RequestType.FACULTY))
    pq.display()
    print("\nProcessing requests (Faculty priority):")
    pq.dequeue()
    pq.dequeue()
    pq.dequeue()
    pq.display()
    
    print("\n" + "=" * 70)
    print("COMPARISON")
    print("=" * 70)
    print("FIFO Queue: First-come, first-served (equal priority)")
    print("Priority Queue: Faculty requests processed before student requests")'''

#Justification: - The FIFO Queue processes requests in the order they were received, which is simple and fair for equal priority requests. - The Priority Queue ensures that faculty requests are handled before student requests, which is important in a library setting where faculty may have more urgent needs.        


#3 Implement an **IT Help Desk Ticket System using a Stack (LIFO)** with operations **push(ticket), pop(), and peek()**, simulate **five tickets being raised and resolved**, and use **GitHub Copilot to suggest additional operations like isEmpty() and isFull()**.
'''class Ticket:
    def __init__(self, ticket_id, issue_title, priority):
        self.ticket_id = ticket_id
        self.issue_title = issue_title
        self.priority = priority
    
    def __repr__(self):
        return f"Ticket(ID: {self.ticket_id}, '{self.issue_title}', Priority: {self.priority})"

# ===== STACK-BASED HELP DESK TICKET SYSTEM =====
class HelpDeskTicketSystem:
    def __init__(self, max_size=10):
        self.stack = []
        self.max_size = max_size
    
    def push(self, ticket):
        if self.isFull():
            print("Stack is full. Cannot add more tickets.")
            return False
        self.stack.append(ticket)
        print(f"Pushed: {ticket}")
        return True
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty. No tickets to resolve.")
            return None
        ticket = self.stack.pop()
        print(f"Resolved: {ticket}")
        return ticket
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
            return None
        ticket = self.stack[-1]
        print(f"Next to resolve: {ticket}")
        return ticket
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) >= self.max_size
    
    def display(self):
        print("Current Stack:", self.stack)

# ===== DEMO & TESTING =====
if __name__ == "__main__":
    print("=" * 70)
    print("IT HELP DESK TICKET SYSTEM (LIFO - Stack)")
    print("=" * 70)
    
    help_desk = HelpDeskTicketSystem(max_size=10)
    
    print("\n--- Raising 5 Tickets ---")
    help_desk.push(Ticket(1, "Password Reset", "Low"))
    help_desk.push(Ticket(2, "Printer Not Working", "Medium"))
    help_desk.push(Ticket(3, "Email Configuration", "High"))
    help_desk.push(Ticket(4, "VPN Connection Issue", "High"))
    help_desk.push(Ticket(5, "Software Installation", "Medium"))
    
    help_desk.display()
    
    print("\n--- Checking Stack Status ---")
    print(f"Is Empty: {help_desk.isEmpty()}")
    print(f"Is Full: {help_desk.isFull()}")
    
    print("\n--- Peeking at Next Ticket ---")
    help_desk.peek()
    
    print("\n--- Resolving Tickets (LIFO Order) ---")
    help_desk.pop()
    help_desk.pop()
    help_desk.pop()
    
    help_desk.display()
    
    print("\n--- Remaining Operations ---")
    help_desk.peek()
    help_desk.pop()
    help_desk.pop()
    
    print(f"\nIs Empty: {help_desk.isEmpty()}")'''

# Justification: - The Stack (LIFO) structure allows the most recently raised tickets to be resolved first, which can be beneficial for urgent issues. - The isEmpty() and isFull() methods help manage the stack's state, ensuring that we don't attempt to resolve tickets when there are none or add tickets beyond capacity.        

#'''#4.Implement a **Hash Table in Python** with methods **insert, search, and delete**, handle **collisions using chaining**, and generate **well-commented methods** starting from `class HashTable: pass`.

'''class HashTable:
    """Hash Table implementation with collision handling using chaining."""
    
    def __init__(self, size=10):
        """Initialize hash table with given size."""
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Generate hash value for a key using modulo operation."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        
        # Check if key already exists and update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                print(f"Updated: {key} -> {value}")
                return
        
        # Add new key-value pair
        bucket.append((key, value))
        print(f"Inserted: {key} -> {value}")
    
    def search(self, key):
        """Search for a value by key in the hash table."""
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        
        for k, v in bucket:
            if k == key:
                print(f"Found: {key} -> {v}")
                return v
        
        print(f"Key '{key}' not found")
        return None
    
    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                deleted = bucket.pop(i)
                print(f"Deleted: {deleted[0]} -> {deleted[1]}")
                return True
        
        print(f"Key '{key}' not found")
        return False
    
    def display(self):
        """Display all key-value pairs in the hash table."""
        print("Hash Table Contents:")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"  Index {i}: {bucket}")

# ===== DEMO & TESTING =====
if __name__ == "__main__":
    print("=" * 70)
    print("HASH TABLE WITH CHAINING - COLLISION HANDLING")
    print("=" * 70)
    
    ht = HashTable(size=5)
    
    print("\n--- Inserting key-value pairs ---")
    ht.insert("name", "Alice")
    ht.insert("age", 25)
    ht.insert("city", "New York")
    ht.insert("email", "alice@email.com")
    ht.insert("phone", "123456789")
    ht.insert("job", "Engineer")  # Potential collision
    
    ht.display()
    
    print("\n--- Searching for keys ---")
    ht.search("name")
    ht.search("job")
    ht.search("unknown")
    
    print("\n--- Updating existing key ---")
    ht.insert("age", 26)
    
    print("\n--- Deleting key-value pairs ---")
    ht.delete("city")
    ht.delete("unknown")
    
    ht.display()'''
# Justification: - The Hash Table provides O(1) average time complexity for insertions, searches, and deletions. - Collision handling using chaining allows multiple key-value pairs to be stored at the same index without data loss, ensuring the integrity of the hash table even when collisions occur.


# #5.Design a **Campus Resource Management System** by selecting suitable **data structures for attendance tracking, event registration, library borrowing, bus scheduling, and cafeteria order queue**, justify each choice in **2–3 sentences**, and **implement one feature in Python using AI-generated code** with a **Feature → Data Structure → Justification table**.

# ===== CAMPUS RESOURCE MANAGEMENT SYSTEM =====
# Feature -> Data Structure -> Justification Table
"""
┌─────────────────────────┬──────────────────────┬─────────────────────────────────────┐
│ Feature                 │ Data Structure       │ Justification                       │
├─────────────────────────┼──────────────────────┼─────────────────────────────────────┤
│ Attendance Tracking     │ Dictionary/Hash Map  │ O(1) lookup by student ID, fast     │
│                         │                      │ update and retrieval of records.    │
├─────────────────────────┼──────────────────────┼─────────────────────────────────────┤
│ Event Registration      │ Set                  │ Prevents duplicate registrations,   │
│                         │                      │ O(1) insertion and membership test. │
├─────────────────────────┼──────────────────────┼─────────────────────────────────────┤
│ Library Borrowing       │ Queue (FIFO)         │ Manages requests in order received, │
│                         │                      │ fair processing for all students.   │
├─────────────────────────┼──────────────────────┼─────────────────────────────────────┤
│ Bus Scheduling          │ Priority Queue       │ Prioritizes urgent routes/times,    │
│                         │                      │ efficient scheduling of buses.      │
├─────────────────────────┼──────────────────────┼─────────────────────────────────────┤
│ Cafeteria Order Queue   │ Queue (FIFO)         │ First-come-first-served service,    │
│                         │                      │ maintains fairness among students.  │
└─────────────────────────┴──────────────────────┴─────────────────────────────────────┘
"""

# ===== IMPLEMENTATION: ATTENDANCE TRACKING SYSTEM =====
'''class AttendanceSystem:
    """Manages student attendance using a dictionary for O(1) operations."""
    
    def __init__(self):
        self.attendance = {}
    
    def mark_attendance(self, student_id, date, status):
        """Mark attendance for a student on a specific date."""
        if student_id not in self.attendance:
            self.attendance[student_id] = {}
        self.attendance[student_id][date] = status
        print(f"Marked {student_id} as {status} on {date}")
    
    def get_attendance(self, student_id):
        """Retrieve attendance record for a student."""
        if student_id in self.attendance:
            print(f"Attendance for {student_id}: {self.attendance[student_id]}")
            return self.attendance[student_id]
        print(f"No record for {student_id}")
        return None
    
    def attendance_percentage(self, student_id):
        """Calculate attendance percentage for a student."""
        if student_id not in self.attendance:
            return 0
        records = self.attendance[student_id].values()
        present = sum(1 for status in records if status == "Present")
        percentage = (present / len(records) * 100) if records else 0
        print(f"{student_id}: {percentage:.2f}% attendance")
        return percentage

# ===== EVENT REGISTRATION SYSTEM =====
class EventRegistrationSystem:
    """Manages event registrations using sets to prevent duplicates."""
    
    def __init__(self):
        self.events = {}
    
    def create_event(self, event_name):
        """Create a new event."""
        if event_name not in self.events:
            self.events[event_name] = set()
            print(f"Event '{event_name}' created")
    
    def register_student(self, event_name, student_id):
        """Register a student for an event."""
        if event_name in self.events:
            if student_id not in self.events[event_name]:
                self.events[event_name].add(student_id)
                print(f"{student_id} registered for '{event_name}'")
            else:
                print(f"{student_id} already registered for '{event_name}'")
        else:
            print(f"Event '{event_name}' not found")
    
    def get_registrations(self, event_name):
        """Get all students registered for an event."""
        if event_name in self.events:
            print(f"'{event_name}' registrations: {self.events[event_name]}")
            return self.events[event_name]
        return set()

# ===== DEMO & TESTING =====
if __name__ == "__main__":
    print("=" * 70)
    print("CAMPUS RESOURCE MANAGEMENT SYSTEM")
    print("=" * 70)
    
    print("\n--- ATTENDANCE TRACKING ---")
    attendance = AttendanceSystem()
    attendance.mark_attendance("S001", "2024-01-15", "Present")
    attendance.mark_attendance("S001", "2024-01-16", "Present")
    attendance.mark_attendance("S001", "2024-01-17", "Absent")
    attendance.get_attendance("S001")
    attendance.attendance_percentage("S001")
    
    print("\n--- EVENT REGISTRATION ---")
    events = EventRegistrationSystem()
    events.create_event("Tech Summit")
    events.register_student("Tech Summit", "S001")
    events.register_student("Tech Summit", "S002")
    events.register_student("Tech Summit", "S001")  # Duplicate attempt
    events.get_registrations("Tech Summit")'''

# Justification: - The Attendance System uses a dictionary to allow for O(1) time complexity when marking and retrieving attendance records, making it efficient for large student populations. - The Event Registration System utilizes sets to ensure that each student can only register once for an event, preventing duplicates and allowing for O(1) insertion and membership checks.
