invoice_no = 7
customer = " John doe"
amount = 199.99
print("="*30)
print("INVOICE".center(30))
print(f"Invoice No: INV-{str(invoice_no).rjust(5,'0')}".center(30))
print(f"Customer: {customer.title()}".center(31))
print(f"Amount: ${str(amount)}".center(31))
print("="*30)

receipt_no = 45
Cashier = "Alice smith"
date = "10-NOV-2025"
print("="*30)
print("CASH RECEIPT".center(30))
print(f"Receipt No: RCP-{str(receipt_no).rjust(5,'0')}".center(30))
print(f"Date: {date}".center(30))
print(f"Cashier: {Cashier.title()}".center(30))
print("="*30)

ticket_no = 12007
movie = "Inception"
seat = "f-12"
show_time = "07:30 PM"
print("*"*30)
print("MOVIE TICKET".center(30))
print(f"Ticket: TKT-{ticket_no}".center(30))
print(f"Movie: {movie}".center(30))
print(f"Seat: {seat}".center(27))
print(f"Time: {show_time}".center(30))
print("*"*30)

fruits = "apple"
print(fruits[3:0])