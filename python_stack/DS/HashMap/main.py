class MyHashMap:
    def __init__(self):
        # 1. Define the total range of possible keys (0 to 1,000,000)
        self.size = 1000001
        self.data_store = []
        
        # 2. Use 'append' to manually initialize our "memory" block.
        # This builds a flat 1D array without using any implicit map.
        for _ in range(self.size):
            self.data_store.append(-1)

    def _perfect_hash(self, key: int) -> int:
        """
        An explicit Perfect Hash Function.
        Using modulus against the full range ensures that every key 
        gets its own unique slot, resulting in ZERO collisions.
        """
        return key % self.size

    def put(self, key: int, value: int) -> None:
        # Get the unique index via the hash function
        index = self._perfect_hash(key)
        
        # Direct assignment: Since no two keys share an index, 
        # there is never a collision to resolve.
        self.data_store[index] = value

    def get(self, key: int) -> int:
        index = self._perfect_hash(key)
        return self.data_store[index]

    def remove(self, key: int) -> None:
        index = self._perfect_hash(key)
        # Reset the unique slot to -1
        self.data_store[index] = -1
        
        
class MyHashMap:
    def __init__(self):
        # Constraint: keys are up to 1,000,000.
        # We define a fixed size to cover the entire possible key space.
        self.size = 1000001
        
        # We manually create a flat array filled with -1.
        # This is NOT an implicit map; it is a raw block of memory.
        self.data_store = [-1] * self.size

    def _perfect_hash(self, key: int) -> int:
        """
        Explicit Perfect Hash Function.
        For a continuous range of integers, the Identity Function 
        is the only hash function that guarantees 0 collisions.
        """
        return key

    def put(self, key: int, value: int) -> None:
        # Step 1: Compute the unique address using the perfect hash
        address = self._perfect_hash(key)
        
        # Step 2: Direct access. No collision resolution logic needed.
        self.data_store[address] = value

    def get(self, key: int) -> int:
        # Step 1: Compute the unique address
        address = self._perfect_hash(key)
        
        # Step 2: Direct retrieval. Guaranteed O(1) time.
        return self.data_store[address]

    def remove(self, key: int) -> None:
        # Step 1: Compute the unique address
        address = self._perfect_hash(key)
        
        # Step 2: Reset the memory slot to the empty state (-1)
        self.data_store[address] = -1
        
class MyHashMap:
    def __init__(self):
        # The range of keys is 0 to 1,000,000.
        # We allocate a size that covers every possible key directly.
        self.size = 1000001
        self.map = [-1] * self.size

    def put(self, key: int, value: int) -> None:
        # Use the key as the direct index. 
        # No two keys will ever share the same index (Collision-Free).
        self.map[key] = value

    def get(self, key: int) -> int:
        # Direct lookup at the specific memory address.
        return self.map[key]

    def remove(self, key: int) -> None:
        # Reset the specific index to -1.
        self.map[key] = -1

class MyHashMap:
    def __init__(self):
        # We split the 1,000,000 space into 1001 buckets.
        # Each bucket will eventually hold 1000 elements.
        # This 2D approach saves memory if keys are sparse.
        self.num_buckets = 1001
        self.bucket_size = 1000
        self.map = [None] * self.num_buckets

    def _get_hash(self, key: int):
        # This is our "Perfect Hash" for this range:
        # It breaks the key into a unique row and column.
        return key // self.bucket_size, key % self.bucket_size

    def put(self, key: int, value: int) -> None:
        bucket, offset = self._get_hash(key)
        # Initialize the bucket only when a key is first added
        if self.map[bucket] is None:
            self.map[bucket] = [-1] * self.bucket_size
        
        # Direct assignment: guaranteed no collision
        self.map[bucket][offset] = value

    def get(self, key: int) -> int:
        bucket, offset = self._get_hash(key)
        # If the bucket was never created, the key doesn't exist
        if self.map[bucket] is None:
            return -1
        return self.map[bucket][offset]

    def remove(self, key: int) -> None:
        bucket, offset = self._get_hash(key)
        # If the bucket exists, reset the slot to -1
        if self.map[bucket] is not None:
            self.map[bucket][offset] = -1
            
class MyHashMap:
    def __init__(self):
        # The key range is 0 to 1,000,000.
        # We set the size to 1,000,001 to ensure every key has a unique slot.
        self.size = 1000001
        self.table = []
        
        # Manually building the storage using append.
        # This creates a flat memory space with NO nested buckets.
        for _ in range(self.size):
            self.table.append(-1)

    def put(self, key: int, value: int) -> None:
        # Use modulus directly to find the unique index.
        # This is a Perfect Hash: Every unique key maps to a unique index.
        # Zero collisions possible because the table size matches the key range.
        index = key % self.size
        self.table[index] = value

    def get(self, key: int) -> int:
        # Direct memory access using the perfect modulus hash.
        index = key % self.size
        return self.table[index]

    def remove(self, key: int) -> None:
        # Reset the unique slot back to the empty state (-1).
        index = key % self.size
        self.table[index] = -1