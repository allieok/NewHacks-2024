class Account:
    def __init__(self, email, company, max_data, current_usage):
        self.email = email
        self.company = company
        self.max_data = max_data
        self.current_usage = current_usage

    def remaining_data(self):
        """Calculate the remaining data for the account."""
        return self.max_data - self.current_usage

    def __str__(self):
        """Return a string representation of the account."""
        return (f"Company: {self.company}\n"
                f"Max Data: {self.max_data} MB\n"
                f"Current Usage: {self.current_usage} MB\n"
                f"Remaining Data: {self.remaining_data()} MB\n"
                f"You have used {self.current_usage/self.max_data*100}% of your data plan.\n"
                "- You're running out of Data!")
