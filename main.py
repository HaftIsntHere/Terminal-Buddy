from textual.app import App
from textual.widgets import Button, Label

class CLIBuddyApp(App):
    def compose(self):
        yield Button("Say Hello", id="hello_button")
        
        self.chat_labels = []
        
        self.chat_labels.append("CLI Buddy: Hi, how can I help you today")
        
        for label in self.chat_labels:
          yield label

    def on_button_pressed(self, message: Button.Pressed) -> None:
        # Change the label text when the button is pressed
         if message.button.id == "hello_button":
            new_message = Label("CLI Buddy: Hello, how can I assist you?")
            self.chat_labels.append(new_message)
            self.refresh()
            
    def refresh(self):
        # Re-compose the layout with all chat messages
        self.query_one("app").remove_widgets()
        for label in self.chat_labels:
            self.query_one("app").add_widget(label)

if __name__ == "__main__":
    CLIBuddyApp().run()