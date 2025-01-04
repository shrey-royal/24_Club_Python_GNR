"""
-> Problem Statement 1: Banking System  
Design a Banking System that allows customers to manage their bank accounts. Implement the following functionality using classes, objects, and constructors:

1. Class `BankAccount`:
   - Attributes: `account_number`, `account_holder`, `balance`, `account_type` (e.g., savings, checking).
   - Constructor: Initializes the account with the account number, account holder name, account type, and initial balance.

2. Functionalities:
   - Deposit: Method to add money to the account.
   - Withdraw: Method to deduct money from the account if the balance is sufficient.
   - Transfer: Method to transfer money from one account to another. Ensure that the recipient account exists, and the balance in the sender's account is sufficient.
   - Display: Method to display account details (account number, holder name, type, and balance).

3. Create multiple bank account objects and test the above functionalities by simulating deposits, withdrawals, and transfers.

---

-> Problem Statement 2: Library Management System  
Create a Library Management System to handle book borrowing and returning. Implement the following using classes, objects, and constructors:

1. Class `Book`:
   - Attributes: `book_id`, `title`, `author`, `copies_available`.
   - Constructor: Initializes a book with its ID, title, author, and number of copies available.

2. Class `LibraryMember`:
   - Attributes: `member_id`, `name`, `borrowed_books` (a list of books borrowed by the member).
   - Constructor: Initializes a member with an ID, name, and an empty list of borrowed books.

3. Functionalities:
   - Borrow Book: Allow a member to borrow a book if copies are available. Update the `borrowed_books` list for the member and decrease the `copies_available` for the book.
   - Return Book: Allow a member to return a book. Update the `borrowed_books` list for the member and increase the `copies_available` for the book.
   - Display Borrowed Books: Show the list of books borrowed by a specific member.
   - Display Available Books: Display all books with their details, including the number of copies available.

4. Create multiple book and library member objects to test the system by simulating borrowing and returning books.

"""