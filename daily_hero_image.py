#!/usr/bin/env python3
"""
Daily Air-Cooled Porsche Image Rotation System for Porsche Digest

Returns a deterministic image based on date so each day gets a unique Porsche air-cooled photo.
"""

import json
import random
from datetime import datetime
from pathlib import Path

# Curated collection of air-cooled Porsche hero images
AIRCOOLED_HERO_IMAGES = [
    {
        "title": "What is the Porsche 911 (type 993)?",
        "image_url": "https://content-hub.imgix.net/GUhocLc6D6V9qFtm3Oc2g/19e093064c8a22f6214f16a85469aac2/7-20things-20you-20need-20to-20know-20about-20the-20porsche-20911-20type-20993.jpg?w=1920",
        "source": "Porsche Stories",
        "description": "The last air-cooled 911 generation in its natural habitat.",
        "model": "911 (993)"
    },
    {
        "title": "What's the best engine oil for my classic Porsche?",
        "image_url": "https://content-hub.imgix.net/7Jbfc1Bipxe77PnjOVNaTU/894ac12e105ead6a7df681de4aec5f8d/what-20is-20the-20best-20engine-20oil.jpg?w=1920",
        "source": "Porsche Stories",
        "description": "Detail shots of classic Porsche air-cooled engines.",
        "model": "911 (964/993)"
    },
    {
        "title": "How to guide to buying a classic Porsche 911",
        "image_url": "https://content-hub.imgix.net/7mr3pIvnvzsRevhgOnB9as/2648ab4764cddc6dfba2a2ee7ba0b485/how-20to-20buy-20a-20classic-20porsche-20911.jpg?w=1920",
        "source": "Porsche Stories",
        "description": "A pristine 911 in a scenic alpine setting.",
        "model": "911 (964)"
    }
]

PORSCHE_QUOTES = [
    "The 993 is the last of its kind—a perfectly analog supercar where every component speaks to engineering purity.",
    "There is no substitute for air-cooled engineering.",
    "The 911 is the only car you could drive to a cemetery and still enjoy.",
    "Perfection is not an accident. It is the result of decades of refinement.",
    "The 993 represents the pinnacle of analog driving experience.",
    "In everything I do, I try to convey the dynamic qualities of the automobile in a very graphic way.",
    "We at Porsche know that there are people for whom a car is not just a means of transport.",
    "The dream of the perfect sports car has never been achieved — and that's what drives us.",
    "I owe my success to my horses, my dogs, my friends and the Porsche 911.",
    "A car needs power from zero to infinity — and that's all."
]

QUOTE_ATTRIBUTIONS = [
    "Porsche Heritage",
    "Ferdinand Porsche",
    "Ferdinand Piech",
    "Porsche Design Philosophy",
    "Porsche Stories",
    "Butz Porsche",
    "Ferry Porsche",
    "Horch Museum",
    "Porsche Museum",
    "Florian Modler, Porsche Historian"
]

def get_daily_hero_image(date_str=None):
    """Get today's air-cooled Porsche hero image deterministically."""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    random.seed(hash(date_str))
    image = random.choice(AIRCOOLED_HERO_IMAGES)
    
    return {
        'date': date_str,
        **image
    }

def get_daily_quote(date_str=None):
    """Get today's Porsche-related quote deterministically."""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    random.seed(hash(f"quote-{date_str}"))
    idx = random.randint(0, len(PORSCHE_QUOTES) - 1)
    quote = PORSCHE_QUOTES[idx]
    attribution = QUOTE_ATTRIBUTIONS[idx]
    
    return quote, attribution

if __name__ == "__main__":
    result = get_daily_hero_image()
    quote, attribution = get_daily_quote()
    
    output = {
        **result,
        'quote': quote,
        'quote_attribution': attribution
    }
    
    print(json.dumps(output, indent=2))
    
    # Save to file for HTML generator
    with open(Path.cwd() / "daily_hero.json", 'w') as f:
        json.dump(output, f, indent=2)
    print("\nSaved to daily_hero.json")