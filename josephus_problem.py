# Raunak Bhojwani
# joesphus_problem.py
# Short Assignment 8
# Monday 3 November 2014
# Circular doubly linked lists


class Soldier:                                                                      # Define a class for an individual soldier
    def __init__(self, n):
        
        self.number = n                                                             # Initialize the soldier number
        self.next = None                                                            # Initialize previous and next in the linked list
        self.prev = None
        
    def kill(self, prefix = "Soldier", suffix = "bites the dust!"): # Member function: kill                 
        print prefix + " " + str(self.number) + " " + suffix                        # Print function to kill the soldier
    
    
class Army:                                                                         # Define a class for Josephus' Army
    def __init__(self, total):
        
        self.alive = total                                                          # Initialize alive soldiers to total to begin with
        
        soldier = Soldier(1)                                                        # Create the first soldier and save the reference
        first = soldier
        
        i = 1
        while i < total:                                                            # In a while loop, create the next soldier in the linked list
            soldier.next = Soldier(i+1)                                             # and link up the entire list (not circular yet)
            soldier.next.prev = soldier
            soldier = soldier.next
            i += 1
        first.prev = soldier                                                        # Make it circular by connecting the last and the saved first nodes
        soldier.next = first
        
        self.victim = soldier                                                       # Initial victim should be the last object in the list so that counting begins with the first soldier in the list
          
    def advance(self, k):   # Member function: advance
        for i in range(k):                                                          # Loop through k times so that every kth soldier is killed
            self.victim = self.victim.next
        self.victim.kill()                                                          # Kill the kth soldier and remove them from the list
        self.victim.prev.next = self.victim.next                                    
        self.victim.next.prev = self.victim.prev
        self.alive -= 1                                                             # Update the number of soldiers left alive
        
    def kill_all(self, k):  # Member function: advance
        while self.alive != 1:                                                      # Keep killing soldiers until only one soldier is left
            self.advance(k)
        self.victim.next.kill("The last remaining soldier is Soldier ", "")         # Call 'kill()' purely as a print function for the last soldier remaining
        

def main():
    total = int(raw_input("Please enter number 'n' of soldiers for Josephus' Circle of Death, at least 2:"))    # Take in inputs for total and k and run the functions
    josephus_army = Army(total)
    k = int(raw_input("Please enter the spacing between victims, between 1 and 'n':"))
    josephus_army.kill_all(k)
    
main()
        
    