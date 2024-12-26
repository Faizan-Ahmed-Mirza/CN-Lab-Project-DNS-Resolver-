import tkinter as tk
from tkinter import messagebox
import socket
import dns.resolver


def resolve_domain():
    domain = entry.get().strip()
    protocol = protocol_var.get()

    if not domain:
        messagebox.showerror("Error", "Please enter a domain name.")
        return

    if protocol == "UDP":
        try:
            resolved_ip = socket.gethostbyname(domain)
            result_label.config(text=f"Resolved IP: {resolved_ip}", fg="green")
        except socket.gaierror:
            result_label.config(text=f"Unable to resolve domain: {domain}", fg="red")

    elif protocol == "HTTPS":
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = ['8.8.8.8']
            answers = resolver.resolve(domain)
            resolved_ip = answers[0].address
            result_label.config(text=f"Resolved IP: {resolved_ip}", fg="green")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            result_label.config(text=f"Unable to resolve domain: {domain}", fg="red")

    elif protocol == "TLS":
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = ['1.1.1.1']  # Cloudflare DNS over TLS
            answers = resolver.resolve(domain)
            resolved_ip = answers[0].address
            result_label.config(text=f"Resolved IP: {resolved_ip}", fg="green")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            result_label.config(text=f"Unable to resolve domain: {domain}", fg="red")


# Create the main application window
root = tk.Tk()
root.title("DNS Resolver")
root.geometry("400x300")
root.resizable(False, False)

# Title Label
tk.Label(root, text="DNS Resolver", font=("Arial", 16, "bold")).pack(pady=10)

# Create input field
tk.Label(root, text="Enter Domain Name:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

# Create Protocol Selection Dropdown
tk.Label(root, text="Select Protocol:", font=("Arial", 12)).pack(pady=5)
protocol_var = tk.StringVar(root)
protocol_var.set("UDP")  # Default selection
protocol_dropdown = tk.OptionMenu(root, protocol_var, "UDP", "HTTPS", "TLS")
protocol_dropdown.config(font=("Arial", 12))
protocol_dropdown.pack(pady=5)

# Create Resolve button
resolve_button = tk.Button(root, text="Resolve", command=resolve_domain, font=("Arial", 12), bg="#0078D7", fg="white")
resolve_button.pack(pady=10)

# Label to display results
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Footer
tk.Label(root, text="© Made by Faizan MirZa and Tazeem Hussain", font=("Arial", 8), fg="blue").pack(side="bottom",
                                                                                                    pady=5)

# Run the application
root.mainloop()
