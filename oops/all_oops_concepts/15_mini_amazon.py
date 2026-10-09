# 15. Create a mini version of Amazon with:
# Classes:
# • User
# • Product
# • Seller(User)
# • Buyer(User)
# • Order
# • Cart
# Requirements (must use all OOP concepts):
# >Inheritance: Seller and Buyer extend User
# >Encapsulation: protect internal cart list, user password
# >Abstraction: base class User defines abstract get_role()
# >Polymorphism: different users behave differently in checkout
# >Composition: Buyer “has” a Cart
# >Operator overloading:
# • + to add product to Cart
# • - to remove product
# >Properties: validate product price


# >Class methods: tracking total users
# >Static methods: validating product IDs
# >__str__ for readable summaries
# >MRO behavior when Buyer inherits from multiple mixins (e.g., RewardsMixin)


