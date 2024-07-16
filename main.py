from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from login import LoginScreen as ls
import sys
import shopclient as shp

# Define shopping items and their prices, pictures, and descriptions
shopping_items = {
    "Item 1": {"price": 10, "picture": "vanilla.jpg", "description": "Vanilla ice cream"},
    "Item 2": {"price": 20, "picture": "chocolate.jpg", "description": "Chocolate ice cream"},
    "Item 3": {"price": 30, "picture": "butterscotch.jpg", "description": "Butterscotch ice cream"},
    "Item 4": {"price": 50, "picture": "strawberry.jpg", "description": "strawberry ice cream"},
    "Item 5": {"price": 60, "picture": "mango.jpg", "description": "mango ice cream"},
    "Item 6": {"price": 50, "picture": "redvelvet.jpg", "description": "red velvet ice cream"},
}

class ShoppingApp(App):
    def build(self):
        self.cart = []
        layout = BoxLayout(orientation="horizontal")
        scrollview = ScrollView()

        grid_layout = GridLayout(cols=2, spacing=10, padding=(dp(10), dp(10)))
        grid_layout.bind(minimum_height=grid_layout.setter("height"))
        header_label = Label(text='Ice Cream Shop', font_size=40, size_hint_y=0.2,height=dp(30))
        layout.add_widget(header_label)

        for item, details in shopping_items.items():
            item_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(dp(200), dp(200)))
            item_layout.add_widget(Image(source=details["picture"], size=(dp(150), dp(150))))

            item_info_layout = BoxLayout(orientation="vertical", spacing=5, padding=5)
            # item_info_layout.add_widget(Label(text=item, size_hint_y=None, height=dp(30), font_size=16))

            item_info_layout.add_widget(Label(text=details["description"], size_hint_y=None, height=dp(30), font_size=14))
            
            item_info_layout.add_widget(Label(text=f"${details['price']}", size_hint_y=None, height=dp(30), font_size=16))

            add_button = Button(text="Add to Cart", size_hint_y=None, height=dp(40))
            add_button.bind(on_press=lambda event, item=item: self.add_to_cart(item))
            item_info_layout.add_widget(add_button)

            item_layout.add_widget(item_info_layout)
            grid_layout.add_widget(item_layout)

        scrollview.add_widget(grid_layout)
        layout.add_widget(scrollview)

        self.bill_label = Label(text="Total Bill: $0", size_hint=(None, None), height=dp(50), font_size=18)
        layout.add_widget(self.bill_label)

        buy_button = Button(text="Buy", size_hint=(None, None), height=dp(50), font_size=18)
        buy_button.bind(on_press=self.buy_items)
        layout.add_widget(buy_button)

        return layout

    def add_to_cart(self, item):
        quantity = 1
        self.cart.append((item, quantity))  
        # Update the bill label
        total_price = sum(
            shopping_items[item]["price"] * quantity for item, quantity in self.cart
        )
        self.bill_label.text = f"Total Bill: ${total_price}"

    def buy_items(self, event):
        cart_info = self.get_cart_info()
        username=cart_info[1]
        print(f"Cart Info: {cart_info}")
        shp.mainf(str(cart_info))
        

    def get_cart_info(self):
        cart_info = {}
        for item, quantity in self.cart:
            cart_info[item] = cart_info.get(item, 0) + quantity

        formatted_cart_info = [(item, quantity, shopping_items[item]["price"] * quantity) for item, quantity in cart_info.items()]
        formatted_cart_info=[0,username]+formatted_cart_info
        return formatted_cart_info

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        username = sys.argv[1]
        print(f"Username: {username}")

    #     # Process the order here...
    #     order = sys.argv[2]  # Assuming the order details are provided as the second command-line argument
    #     print(f"Order: {order}")

    #     # Print the combined information
    #     print([0, username, order])
    # else:
        # print("Username and order not provided as command-line arguments.")
    ShoppingApp().run()


