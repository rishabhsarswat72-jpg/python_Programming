class Account:
    pass

class PremiumAccount(Account):
    pass

print(issubclass(PremiumAccount, Account))
print(issubclass(Account, PremiumAccount))