# PLANE SEATING ASSIGNMENT 
## Algorithm, based on seating plan from last week

- if 2 or more days before flight, block out bulkhead seats
  - if less than 2 days before flight, mark as available
>
- remove option for economy plus seating if input
  >
- if input **any number**, then assign each one standard way
  - standard fill includes
    - filling all middle and aisle seats
    - THEN filling window seats last
>
- if input as needing a **pair accommodation**, then assign as a group of two together
  - implement **move over** function to move one person over
>
- if input asks for **window seat**
  - increase price by X amount
  - assign to window seat
  - return message if  needing a **pair accommodation**, then assign as a group of two together
  - implement **move over** function to move one person over
>
  
>
- optional: give preference for window seating at an extra price by moving an already assigned seat on the left side over one and already assigned seat on the right side back one (blocked out accommodation seats such as verified pairs and bulkhead seats excluded); to make it more manageable, if there is no case where there is an available seat after one move, then this preference is rendered unavailable

