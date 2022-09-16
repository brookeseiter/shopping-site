"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(
        self, 
        first_name, 
        last_name, 
        email, 
        password,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return (
            f"<Customer: {self.first_name}, {self.last_name}, {self.email}, {self.password}>"
        )

def read_customers_from_file(filepath):
    """Read customer type data and populate dictionary of customers.

    Dictionary will be {email: Customer object}
    """

    customers = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password,
            ) = line.strip().split("|")

            customers[email] = Customer(
                first_name,
                last_name,
                email,
                password,
            )

    return customers

def get_by_email(email):
    """Return a customer, given their email."""

    # This relies on access to the global dictionary `customers`

    print(customers.get(email))
    # Don't use customers[email] like in melons. If we encounter user that doesnt
    # exist, it will give key error. Using .get allows us to avoid key error, it
    # instead returns None and allows the program to continue through to the 
    # flash message.
    return customers.get(email)

customers = read_customers_from_file("customers.txt")




# HOW PASSWORDS ARE HANDLED IN REAL WORLD:
# def is_correct_password(self, password):
#     """Check if password is correct password for this customer.

#     Compare the hash of password to the stored hash of the
#     original password.
#     """

#     return hash(password) == self.hashed_password

