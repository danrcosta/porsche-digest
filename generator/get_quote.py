import random

date_str = "2026-08-22"
porsche_quotes = [
    "The 993 is the last of its kind—a perfectly analog supercar where every component speaks to engineering purity. — Porsche Stories",
    "There is no substitute for air-cooled engineering. — Ferdinand Porsche",
    "The 911 is the only car you could drive to a cemetery and still enjoy. — Ferdinand Piech",
    "Perfection is not an accident. It is the result of decades of refinement. — Porsche Design Philosophy",
    "The 993 represents the pinnacle of analog driving experience. — Porsche Heritage"
]

random.seed(hash(date_str))
quote = random.choice(porsche_quotes)
print(quote)
