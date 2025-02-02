from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout, MDNavigationDrawerMenu, MDNavigationDrawerHeader, MDNavigationDrawerItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window

Window.size = (360, 640)

KV = """
MDNavigationLayout:
    ScreenManager:
        id: screen_manager
        HomeScreen:
        DonateScreen:
        NGORegisterScreen:
        ViewDonationsScreen:
        ViewNGOsScreen:

    
    MDNavigationDrawer:
        id: nav_drawer
        MDNavigationDrawerMenu:
            MDNavigationDrawerHeader:
                title: "Menu"
                spacing: "12dp"
            MDNavigationDrawerItem:
                text: "Home"
                icon: "home"
                on_release: app.change_screen('home'); nav_drawer.set_state("close")
            MDNavigationDrawerItem:
                text: "Donate Food"
                icon: "food"
                on_release: app.change_screen('donate'); app.root.ids.nav_drawer.set_state("close")
            MDNavigationDrawerItem:
                text: "Register NGO"
                icon: "account-group"
                on_release: app.change_screen('ngo_register'); app.root.ids.nav_drawer.set_state("close")
            MDNavigationDrawerItem:
                text: "View Donations"
                icon: "clipboard-list"
                on_release: app.change_screen('view_donations'); nav_drawer.set_state("close")
            MDNavigationDrawerItem:
                text: "View NGOs"
                icon: "domain"
                on_release: app.change_screen('view_ngos'); nav_drawer.set_state("close")

<HomeScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Annasamrakshna"
            left_action_items: [["menu", lambda x: app.root.ids.nav_drawer.set_state("open")]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            MDLabel:
                text: "Welcome to Annasamrakshna"
                halign: "center"
                font_style: "H5"
            MDRaisedButton:
                text: "Donate Food"
                pos_hint: {"center_x": 0.5}
                on_release: app.change_screen('donate')
            MDRaisedButton:
                text: "Register as NGO"
                pos_hint: {"center_x": 0.5}
                on_release: app.change_screen('ngo_register')
            MDRaisedButton:
                text: "View Donations"
                pos_hint: {"center_x": 0.5}
                on_release: app.change_screen('view_donations')
            MDRaisedButton:
                text: "View NGOs"
                pos_hint: {"center_x": 0.5}
                on_release: app.change_screen('view_ngos')

<DonateScreen>:
    name: 'donate'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Donate Food"
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]
        MDBoxLayout:
            orientation: 'vertical'
            MDTextField:
                id: donor_name
                hint_text: "Donor Name"
            MDTextField:
                id: food_type
                hint_text: "Food Type"
            MDTextField:
                id: quantity
                hint_text: "Quantity (kg)"
            MDTextField:
                id: location
                hint_text: "Pickup Location"
            MDRaisedButton:
                text: "Submit"
                on_release: app.add_donation()

<NGORegisterScreen>:
    name: 'ngo_register'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Register as NGO"
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]
        MDTextField:
            id: ngo_name
            hint_text: "NGO Name"
            mode: "rectangle"
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            size_hint_x: 0.8
        MDTextField:
            id: ngo_contact
            hint_text: "Contact"
            mode: "rectangle"
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            size_hint_x: 0.8
        MDTextField:
            id: ngo_location
            hint_text: "Location"
            mode: "rectangle"
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            size_hint_x: 0.8
        MDRaisedButton:
            text: "Submit"
            pos_hint: {"center_x": 0.5}
            on_release: app.register_ngo()
                            

<ViewDonationsScreen>:
    name: 'view_donations'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Donations"
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]
        ScrollView:
            MDList:
                id: donation_list

<ViewNGOsScreen>:
    name: 'view_ngos'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View NGOs"
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]
        ScrollView:
            MDList:
                id: ngo_list                
"""

class HomeScreen(Screen):
    pass

class DonateScreen(Screen):
    pass

class NGORegisterScreen(Screen):
    pass

class ViewDonationsScreen(Screen):
    pass

class ViewNGOsScreen(Screen):
    pass

class FoodWasteApp(MDApp):
    def build(self):
        self.title = "Food Waste Management"
        self.theme_cls.primary_palette = "Blue"
        self.screen_manager = Builder.load_string(KV)
        self.donations = []
        self.ngos = []
        return self.screen_manager

    def change_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

    def add_donation(self):
     screen_manager = self.root.ids.screen_manager  # Correctly reference ScreenManager
     donate_screen = screen_manager.get_screen('donate')  # Now fetch the DonateScreen

     donor_name = donate_screen.ids.donor_name.text
     food_type = donate_screen.ids.food_type.text
     quantity = donate_screen.ids.quantity.text
     location = donate_screen.ids.location.text

     if donor_name and food_type and quantity and location:
        self.donations.append({
            "Donor": donor_name,
            "Food": food_type,
            "Quantity": quantity,
            "Location": location
        })

        # Clear input fields after submission
        donate_screen.ids.donor_name.text = ""
        donate_screen.ids.food_type.text = ""
        donate_screen.ids.quantity.text = ""
        donate_screen.ids.location.text = ""

        self.show_dialog("Success", "Donation added successfully!")
        self.update_donations()
        self.change_screen('home')
     else:
        self.show_dialog("Error", "Please fill out all fields!")


    def update_donations(self):
     screen_manager = self.root.ids.screen_manager  # Correctly reference ScreenManager
     donation_list = screen_manager.get_screen('view_donations').ids.donation_list

     donation_list.clear_widgets()  # Clear existing list

     for donation in self.donations:
        item_text = f"{donation['Donor']} donated {donation['Quantity']}kg of {donation['Food']} at {donation['Location']}"
        donation_list.add_widget(OneLineListItem(text=item_text))

    def register_ngo(self):
     screen_manager = self.root.ids.screen_manager  # Correctly reference ScreenManager
     ngo_screen = screen_manager.get_screen('ngo_register')  # Get the NGO Register Screen

     ngo_name = ngo_screen.ids.ngo_name.text
     ngo_contact = ngo_screen.ids.ngo_contact.text
     ngo_location = ngo_screen.ids.ngo_location.text

     if ngo_name and ngo_contact and ngo_location:
        self.ngos.append({
            "NGO": ngo_name,
            "Contact": ngo_contact,
            "Location": ngo_location
        })

        # Clear input fields after submission
        ngo_screen.ids.ngo_name.text = ""
        ngo_screen.ids.ngo_contact.text = ""
        ngo_screen.ids.ngo_location.text = ""

        self.show_dialog("Success", "NGO registered successfully!")
        self.update_ngos()
        self.change_screen('home')
     else:
        self.show_dialog("Error", "Please fill out all fields!")

    def update_ngos(self):
     screen_manager = self.root.ids.screen_manager  # Correctly reference ScreenManager
     ngo_list = screen_manager.get_screen('view_ngos').ids.ngo_list  # Get the NGO List Screen

     ngo_list.clear_widgets()  # Clear existing list

     for ngo in self.ngos:
        item_text = f"{ngo['NGO']} | Contact: {ngo['Contact']} | Location: {ngo['Location']}"
        ngo_list.add_widget(OneLineListItem(text=item_text))
    
    


    def show_dialog(self, title, text):
        if not hasattr(self, 'dialog'):
            self.dialog = MDDialog(
                title=title,
                text=text,
                buttons=[MDRaisedButton(text="OK", on_release=lambda x: self.dialog.dismiss())]
            )
        else:
            self.dialog.title = title
            self.dialog.text = text
        self.dialog.open()

if __name__ == '__main__':
    FoodWasteApp().run()
