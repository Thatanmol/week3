class ShoppingCart:
    def __init__(self, is_registered, has_items_in_cart, is_guest, is_gift_card):
        self.is_registered = is_registered
        self.has_items_in_cart = has_items_in_cart
        self.is_guest = is_guest
        self.is_gift_card = is_gift_card

    def can_make_purchase(self):
        # For a registered user:
        if self.is_registered and self.has_items_in_cart:
            return "You can make a purchase."
        # For a guest user:
        elif self.is_guest and (self.is_gift_card or not self.has_items_in_cart):
            return "You can make a purchase."
        else:
            return "You cannot make a purchase."