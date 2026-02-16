import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
import threading

class SimpleUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restarant Price checking AI Powerred tool")
        self.root.geometry("800x600")

        # Input textbox
        tk.Label(self.root, text="Enter a dish and restaurant name to find the price. Example:   'I want the price of Chilli Gobi at Bawarchi Sunnyvale'").pack(padx=10, pady=(10, 0), anchor="w")
        self.textbox = tk.Entry(self.root, width=50)
        self.textbox.pack(padx=10, pady=10)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send)
        self.send_button.pack(padx=10, pady=5)

        # Response display
        tk.Label(self.root, text="Response:").pack(padx=10, pady=(10, 0), anchor="w")
        self.response_text = scrolledtext.ScrolledText(self.root, width=70, height=15, wrap=tk.WORD)
        self.response_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def send(self):
        user_input = self.textbox.get()
        if not user_input.strip():
            messagebox.showwarning("Empty Input", "Please enter a query")
            return
        
        # Run send_request in a separate thread to avoid blocking UI
        threading.Thread(target=self.send_request, args=(user_input,), daemon=True).start()

    def send_request(self, query):
        try:
            self.response_text.insert(tk.END, f"\n[Sending query...]\n")
            self.response_text.see(tk.END)
            
            # Make POST request to FastAPI endpoint
            response = requests.post(
                "http://127.0.0.1:9001/chat",
                data={"query": query},
                timeout=300
            )
            
            if response.status_code == 200:
                result = response.json()
                answer = result.get("answer", "No answer received")
                self.response_text.insert(tk.END, f"Query: {query}\n")
                self.response_text.insert(tk.END, f"Response: {answer}\n")
                self.response_text.insert(tk.END, "-" * 50 + "\n")
                self.textbox.delete(0, tk.END)
                print(f"Response: {answer}")
            else:
                error_msg = f"Error: {response.status_code} - {response.text}"
                self.response_text.insert(tk.END, f"{error_msg}\n")
                print(error_msg)
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.response_text.insert(tk.END, f"{error_msg}\n")
            print(error_msg)
        finally:
            self.response_text.see(tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui = SimpleUI()
    ui.run()
