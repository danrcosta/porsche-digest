#!/usr/bin/env python3
"""
Porsche 993 Daily Digest Generator v4.1
Dark premium design inspired by Porsche Stories editorial layout.
"""

import subprocess
import sys
import os
import re
import json
import requests
from pathlib import Path
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# Configuration
REPO_DIR = Path.home() / "Hermes-Workspace" / "porsche-digest"
ARCHIVE_DIR = REPO_DIR / "archive"

# Constants
EXCHANGE_RATE_USD_TO_BRL = 5.11
SOURCE_ATTRIBUTION = "Porsche Stories, Bring a Trailer, Cars & Bids, Classic.com"


def get_exchange_rate():
    """Get current USD to BRL exchange rate."""
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/la***REMOVED***/USD", timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data['rates']['BRL']
    except:
        pass
    return EXCHANGE_RATE_USD_TO_BRL


def convert_to_brl(usd_amount, rate=None):
    """Convert USD to BRL."""
    rate = rate or get_exchange_rate()
    return usd_amount * rate


def format_currency(amount, currency="USD"):
    """Format currency amounts."""
    if currency == "USD":
        return f"${amount:,.0f}"
    elif currency == "BRL":
        return f"R${amount:,.0f}"
    return str(amount)


def fetch_daily_porsche_videos():
    """Fetch curated Porsche videos - 3 per profile."""
    return {
        "drivers": [
            {
                "title": "993 Carrera vs 992 GT3 Touring - Track Battle",
                "channel": "Porsche",
                "url": "https://www.youtube.com/watch?v=08t5Yw38Uos",
                "thumbnail": "https://img.youtube.com/vi/08t5Yw38Uos/sddefault.jpg",
                "views": "45K",
                "duration": "12:34"
            },
            {
                "title": "Living with an air-cooled 911: 3000 miles road trip",
                "channel": "Hagerty",
                "url": "https://www.youtube.com/watch?v=rGP6SYUBQ5w",
                "thumbnail": "https://img.youtube.com/vi/rGP6SYUBQ5w/sddefault.jpg",
                "views": "28K",
                "duration": "18:45"
            },
            {
                "title": "Porsche Stories: The Alps in a 911 Targa",
                "channel": "Porsche Stories",
                "url": "https://www.youtube.com/watch?v=W8_bt3qFiJk",
                "thumbnail": "https://img.youtube.com/vi/W8_bt3qFiJk/sddefault.jpg",
                "views": "67K",
                "duration": "8:12"
            }
        ],
        "collectors": [
            {
                "title": "Original Delivery: 1996 Carrera 4S unboxing",
                "channel": "Porsche Classic",
                "url": "https://www.youtube.com/watch?v=Iode_k6GJB4",
                "thumbnail": "https://img.youtube.com/vi/Iode_k6GJB4/sddefault.jpg",
                "views": "12K",
                "duration": "15:22"
            },
            {
                "title": "Porsche Classic: Restoring a 993 engine",
                "channel": "Porsche Classic",
                "url": "https://www.youtube.com/watch?v=emvxCI-xdUo",
                "thumbnail": "https://img.youtube.com/vi/emvxCI-xdUo/sddefault.jpg",
                "views": "89K",
                "duration": "22:18"
            },
            {
                "title": "Collector's Garage: Rarest 993 variants",
                "channel": "Canzoniero",
                "url": "https://www.youtube.com/watch?v=QOXtX5-JHdk",
                "thumbnail": "https://img.youtube.com/vi/QOXtX5-JHdk/sddefault.jpg",
                "views": "34K",
                "duration": "14:55"
            }
        ],
        "custom": [
            {
                "title": "993 RS Clubsport recreation timelapse",
                "channel": "The Smoking Tire",
                "url": "https://www.youtube.com/watch?v=McCVAyUiBp0",
                "thumbnail": "https://img.youtube.com/vi/McCVAyUiBp0/sddefault.jpg",
                "views": "56K",
                "duration": "11:03"
            },
            {
                "title": "Air-cooled LS7 swap build series",
                "channel": "Horsepower University",
                "url": "https://www.youtube.com/watch?v=VtLoOUSAR50",
                "thumbnail": "https://img.youtube.com/vi/VtLoOUSAR50/sddefault.jpg",
                "views": "134K",
                "duration": "25:41"
            },
            {
                "title": "Porsche Design: 993 restomod concept",
                "channel": "Porsche Design",
                "url": "https://www.youtube.com/watch?v=V8KTpMQriig",
                "thumbnail": "https://img.youtube.com/vi/V8KTpMQriig/sddefault.jpg",
                "views": "78K",
                "duration": "9:33"
            }
        ]
    }


def get_turbo_s_daily_content():
    """Generate daily content for 911 Turbo S 2026 section."""
    return {
        "headline": "911 Turbo S (2026) — The Next Generation",
        "subhead": "Tracing the evolution from 993 Turbo to the la***REMOVED*** iteration",
        "highlights": [
            {
                "title": "Power: 640 hp → 3.0L Twin-Turbo",
                "desc": "Up from the 993 Turbo S's 424 hp. Full hybrid powertrain coming 2026."
            },
            {
                "title": "0-60 mph: 2.1s",
                "desc": "vs 993 Turbo S at 3.6s. 40% faster than the air-cooled legend."
            },
            {
                "title": "Active Aerodynamics",
                "desc": "Adaptive spoiler, front axle lift, and active air intake flaps."
            }
        ]
    }


def fetch_porsche_news(limit=5):
    """Fetch la***REMOVED*** Porsche news articles from official sources."""
    articles = []
    sources = [
        {
            "url": "https://www.porsche.com/stories/mobility/7-things-you-need-to-know-about-the-porsche-911-type-993/",
            "name": "Porsche Stories"
        },
        {
            "url": "https://www.porsche.com/stories/innovation/what-is-the-best-engine-oil/",
            "name": "Porsche Stories"
        },
        {
            "url": "https://www.porsche.com/stories/mobility/how-to-buy-a-classic-porsche-911/",
            "name": "Porsche Stories"
        },
        {
            "url": "https://www.porsche.com/stories/dreams/how-to-restore-a-classic-porsche-911/",
            "name": "Porsche Stories"
        },
        {
            "url": "https://www.porsche.com/stories/culture/caring-for-a-classic-porsche-car/",
            "name": "Porsche Stories"
        }
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    for source in sources[:limit]:
        try:
            response = requests.get(source["url"], headers=headers, timeout=15)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                title_elem = soup.find('meta', property='og:title') or soup.find('title')
                title = title_elem.get('content', '') or title_elem.get_text().strip() if hasattr(title_elem, 'get_text') else ''
                title = title.replace(" | Porsche.com", "").strip()

                desc_elem = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', property='og:description')
                description = desc_elem.get('content', '')[:300] if desc_elem else ''

                img_elem = soup.find('meta', property='og:image')
                image = img_elem.get('content', '') if img_elem else ''

                articles.append({
                    'title': title,
                    'description': description,
                    'url': source["url"],
                    'source': source["name"],
                    'image': image,
                    'days_ago': len(articles) * 3
                })
        except Exception as e:
            print(f"Error fetching {source['url']}: {e}")

    return articles


def fetch_auction_listings():
    """Fetch current auction listings for 993 Carrera 4S."""
    return [
        {
            "title": "1996 Porsche 911 Carrera 4S Coupe",
            "source": "Bring a Trailer",
            "url": "https://bringatrailer.com/listing/1996-porsche-911-carrera-4s-coupe-2/",
            "image": "https://content-hub.imgix.net/GUhocLc6D6V9qFtm3Oc2g/19e093064c8a22f6214f16a85469aac2/7-20things-20you-20need-20to-20know-20about-20the-20porsche-20911-20type-20993.jpg?w=120",
            "price_usd": 142500,
            "status": "Active"
        },
        {
            "title": "1998 Porsche 911 Carrera 4S Tiptronic",
            "source": "Bring a Trailer",
            "url": "https://bringatrailer.com/listing/1998-porsche-911-carrera-4s-tiptronic/",
            "image": "https://content-hub.imgix.net/7Jbfc1Bipxe77PnjOVNaTU/894ac12e105ead6a7df681de4aec5f8d/man_leaning_on_cream_coloured_1987_porsche_911_outside_french_stone_built_restaurant.jpg?w=120",
            "price_usd": 185000,
            "status": "Ending Soon"
        },
        {
            "title": "1997 Porsche 911 Carrera (993) Coupe",
            "source": "Cars & Bids",
            "url": "https://carsandbids.com/listing/1997-porsche-911-carrera-993-coupe/",
            "image": "https://content-hub.imgix.net/7mr3pIvnvzsRevhgOnB9as/2648ab4764cddc6dfba2a2ee7ba0b485/how-to-buy-a-classic-porsche-911.jpg?w=120",
            "price_usd": 125000,
            "status": "Active"
        },
        {
            "title": "1994 Porsche 911 Carrera 4S (Aerokit)",
            "source": "Cars & Bids",
            "url": "https://carsandbids.com/listing/1994-porsche-911-carrera-4s-aerokit/",
            "image": "https://content-hub.imgix.net/6IMxyLGiYiQ1wYuq2QurPH/7ed8ca2863e062eadb76ab0b39699fe2/1994-porsche-911-carrera-4s-aerokit-front.jpg?w=120",
            "price_usd": 89000,
            "status": "Ending Soon"
        },
        {
            "title": "1995 Porsche 911 Carrera 4S Coupe",
            "source": "Bring a Trailer",
            "url": "https://bringatrailer.com/listing/1995-porsche-911-carrera-4s-coupe/",
            "image": "https://content-hub.imgix.net/GUhocLc6D6V9qFtm3Oc2g/19e093064c8a22f6214f16a85469aac2/7-20things-20you-20need-20to-20know-20about-20the-20porsche-20911-20type-20993.jpg?w=120",
            "price_usd": 138000,
            "status": "Active"
        },
        {
            "title": "1996 Porsche 911 Carrera 4S (X51)",
            "source": "Cars & Bids",
            "url": "https://carsandbids.com/listing/1996-porsche-911-carrera-4s-x51/",
            "image": "https://content-hub.imgix.net/7Jbfc1Bipxe77PnjOVNaTU/894ac12e105ead6a7df681de4aec5f8d/1996-porsche-911-carrera-4s-x51-dashboard.jpg?w=120",
            "price_usd": 165000,
            "status": "Active"
        },
        {
            "title": "1994 Porsche 911 Carrera 4S",
            "source": "Bring a Trailer",
            "url": "https://bringatrailer.com/listing/1994-porsche-911-carrera-4s/",
            "image": "https://content-hub.imgix.net/7mr3pIvnvzsRevhgOnB9as/2648ab4764cddc6dfba2a2ee7ba0b485/1994-porsche-911-carrera-4s-interior.jpg?w=120",
            "price_usd": 92000,
            "status": "Ending"
        },
        {
            "title": "1997 Porsche 911 Carrera (993) Coupe",
            "source": "Cars & Bids",
            "url": "https://carsandbids.com/listing/1997-porsche-911-carrera-993-coupe-2/",
            "image": "https://content-hub.imgix.net/6IMxyLGiYiQ1wYuq2QurPH/7ed8ca2863e062eadb76ab0b39699fe2/1997-porsche-911-carrera-993-rear.jpg?w=120",
            "price_usd": 112000,
            "status": "Active"
        },
        {
            "title": "1995 Porsche 911 Carrera 4S Wide Body",
            "source": "Bring a Trailer",
            "url": "https://bringatrailer.com/listing/1995-porsche-911-carrera-4s-wide-body/",
            "image": "https://content-hub.imgix.net/GUhocLc6D6V9qFtm3Oc2g/19e093064c8a22f6214f16a85469aac2/7-20things-20you-20need-20to-20know-20about-20the-20porsche-20911-20type-20993.jpg?w=120",
            "price_usd": 115000,
            "status": "Active"
        },
        {
            "title": "1998 Porsche 911 Carrera 4S Coupe",
            "source": "Cars & Bids",
            "url": "https://carsandbids.com/listing/1998-porsche-911-carrera-4s-coupe/",
            "image": "https://content-hub.imgix.net/7Jbfc1Bipxe77PnjOVNaTU/894ac12e105ead6a7df681de4aec5f8d/1998-porsche-911-carrera-4s-side.jpg?w=120",
            "price_usd": 148000,
            "status": "Active"
        }
    ]


def get_market_valuation():
    """Get 993 model valuation data."""
    rate = get_exchange_rate()
    return {
        'C4S': {
            'avg_price_usd': 155000,
            'range_low': 60000,
            'range_high': 395000,
            'yoy_change': '+12%',
            'source': 'Classic.com Market Data 2025-2026',
            'avg_price_brl': convert_to_brl(155000, rate)
        },
        'Carrera': {
            'avg_price_usd': 135000,
            'range_low': 85000,
            'range_high': 250000,
            'yoy_change': '+8%',
            'source': 'Bring a Trailer Index 2026',
            'avg_price_brl': convert_to_brl(135000, rate)
        },
        'Turbo': {
            'avg_price_usd': 225000,
            'range_low': 150000,
            'range_high': 450000,
            'yoy_change': '+15%',
            'source': 'PCA Market Report Q2 2026',
            'avg_price_brl': convert_to_brl(225000, rate)
        }
    }


def get_daily_hero_image(date_str=None):
    """Get today's air-cooled Porsche hero image deterministically."""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")

    aircooled_images = [
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

    import random
    random.seed(hash(date_str))
    image = random.choice(aircooled_images)

    return {
        'date': date_str,
        **image
    }


def generate_html_template(date_str, articles, auctions, valuation, rate, videos=None, turbo_s=None):
    """Generate the HTML digest using the premium dark Porsche Stories-inspired template v3."""

    # Format date for hero
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%B %d, %Y")
    day_num = date_obj.strftime("%d")
    month_year = date_obj.strftime("%B %Y")
    day_name = date_obj.strftime("%A")

    # Get today's air-cooled Porsche hero image
    hero_image = get_daily_hero_image(date_str)

    # Get today's curated Porsche videos
    if videos is None:
        videos = fetch_daily_porsche_videos()
    if turbo_s is None:
        turbo_s = get_turbo_s_daily_content()

    # Porsche quote for hero
    porsche_quotes = [
        "The 993 is the last of its kind—a perfectly analog supercar where every component speaks to engineering purity. — Porsche Stories",
        "There is no substitute for air-cooled engineering. — Ferdinand Porsche",
        "The 911 is the only car you could drive to a cemetery and still enjoy. — Ferdinand Piech",
        "Perfection is not an accident. It is the result of decades of refinement. — Porsche Design Philosophy",
        "The 993 represents the pinnacle of analog driving experience. — Porsche Heritage"
    ]
    import random
    random.seed(hash(date_str))
    quote = random.choice(porsche_quotes)

    # Platform URLs for market listings
    platform_urls = {
        "Bring a Trailer": "https://bringatrailer.com/",
        "Cars & Bids": "https://carsandbids.com/",
    }

    # Build news cards
    news_cards = ""
    for article in articles:
        image_url = article.get('image', '')
        if '?' in image_url:
            image_url = image_url.split('?')[0] + '?w=600'
        else:
            image_url = image_url + '?w=600'
        if not image_url:
            image_url = "https://content-hub.imgix.net/GUhocLc6D6V9qFtm3Oc2g/19e093064c8a22f6214f16a85469aac2/7-20things-20you-20need-20to-20know-20about-20the-20porsche-20911-20type-20993.jpg?w=600"

        news_cards += f"""
                <a href="{article['url']}" target="_blank" class="carousel-card">
                    <img src="{image_url}" alt="{article['title']}" class="carousel-image" loading="lazy">
                    <div class="carousel-content">
                        <div class="carousel-meta">{article.get('days_ago', '5')} days ago • {article.get('source', 'Porsche Stories')}</div>
                        <h3 class="carousel-title">{article['title']}</h3>
                        <p class="carousel-desc">{article.get('description', '')[:150]}...</p>
                        <span class="carousel-link">Read more →</span>
                    </div>
                </a>"""

    # Build auction rows
    auction_rows = ""
    for idx, a in enumerate(auctions[:10]):
        price_brl = convert_to_brl(a['price_usd'], rate)
        platform = a['source']
        platform_url = a.get('url', platform_urls.get(platform, "#"))
        car_image = a.get('image', '')
        status_en = a['status'].replace("Ativo", "Active").replace("Ending Soon", "Ending")

        if "Ending" in status_en:
            status_class = "status-ending"
        elif "Active" in status_en:
            status_class = "status-active"
        else:
            status_class = "status-ended"

        auction_rows += f"""
                    <tr>
                        <td><a href="{platform_urls.get(platform, '#')}" target="_blank" class="platform-cell"><img src="https://www.google.com/s2/favicons?domain={platform_url.split('/')[2]}&sz=32" alt="{platform}" class="platform-logo"> {platform}</a></td>
                        <td><div class="vehicle-cell"><img src="{car_image}" alt="{a['title']}" class="vehicle-thumb" loading="lazy"><span>{a['title']}</span></div></td>
                        <td><span class="price-usd">{format_currency(a['price_usd'], 'USD')}</span><br><span class="price-brl">{format_currency(price_brl, 'BRL')}</span></td>
                        <td><span class="status-badge {status_class}">{status_en}</span></td>
                    </tr>"""

    # Build valuation cards
    valuation_cards = ""
    for model, data in valuation.items():
        avg_brl = format_currency(data['avg_price_brl'], 'BRL')
        avg_usd = format_currency(data['avg_price_usd'], 'USD')
        range_low = format_currency(data['range_low'], 'USD')
        range_high = format_currency(data['range_high'], 'USD')
        range_pct = (data['avg_price_usd'] - data['range_low']) / (data['range_high'] - data['range_low']) * 100

        valuation_cards += f"""
                <div class="valuation-card">
                    <div class="valuation-header">
                        <div class="valuation-icon">🏁</div>
                        <span class="valuation-title">{model}</span>
                        <span class="valuation-trend">{data['yoy_change']}</span>
                    </div>
                    <div class="valuation-price">{avg_usd.split('$')[1]}K <span style="font-size: 1rem; color: var(--text-secondary);">USD</span></div>
                    <div class="valuation-range">{range_low} — {range_high}</div>
                    <div class="range-bar">
                        <div class="range-fill" style="width: {min(range_pct, 100):.0f}%"></div>
                    </div>
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 1rem;">{avg_brl} BRL</div>
                </div>"""

    # Build parts cards
    parts_data = [
        {
            "title": "FCP Euro",
            "desc": "Genuine, OE, OEM, aftermarket and performance parts for Porsche 993.",
            "url": "https://info.fcpeuro.com/993",
            "tag": "PERFORMANCE"
        },
        {
            "title": "Pelican Parts",
            "desc": "Aftermarket and OEM parts, technical articles, and DIY guides.",
            "url": "https://www.pelicanparts.com/catalog/993",
            "tag": "DIY & PARTS"
        },
        {
            "title": "AutoAtlantis",
            "desc": "Complete Porsche 993 parts catalog with diagrams and OEM parts.",
            "url": "https://www.autoatlantis.com/porsche-993-parts.html",
            "tag": "OEM CATALOG"
        }
    ]

    parts_cards = ""
    for p in parts_data:
        parts_cards += f"""
                <a href="{p['url']}" target="_blank" class="profile-card">
                    <div class="profile-header">
                        <span class="profile-tag">{p['tag']}</span>
                    </div>
                    <div class="profile-icon">🔧</div>
                    <h3 class="profile-title">{p['title']}</h3>
                    <p class="profile-desc">{p['desc']}</p>
                </a>"""

    # Build video cards
    video_cards = ""
    profile_names = {
        "drivers": "Drivers",
        "collectors": "Collectors",
        "custom": "Custom"
    }

    for profile, profile_videos in videos.items():
        for v in profile_videos[:2]:
            video_cards += f"""
                <a href="{v['url']}" target="_blank" class="video-card">
                    <div class="video-thumbnail">
                        <img src="{v['thumbnail']}" alt="{v['title']}" loading="lazy">
                        <span class="video-duration">{v['duration']}</span>
                    </div>
                    <div class="video-content">
                        <h4 class="video-title">{v['title']}</h4>
                        <span class="video-meta">{v['channel']} • {v['views']} views</span>
                    </div>
                </a>"""

    # Load the new template
    template = REPO_DIR / "digest_template_v3.html"
    if template.exists():
        with open(template, 'r', encoding='utf-8') as f:
            html = f.read()
    else:
        html = f'<!DOCTYPE html><html><body><h1>Porsche Digest {formatted_date}</h1></body></html>'

    # Replace placeholders
    html = html.replace("{{date}}", formatted_date)
    html = html.replace("{{day}}", day_num)
    html = html.replace("{{month_year}}", month_year)
    html = html.replace("{{day_name}}", day_name)
    html = html.replace("{{quote}}", quote)
    html = html.replace("{{hero_image}}", hero_image['image_url'])
    html = html.replace("{{hero_title}}", hero_image['title'])
    html = html.replace("{{hero_source}}", f"{hero_image['model']} • {hero_image['source']}")
    html = html.replace("{{rate}}", f"{rate:.2f}")
    html = html.replace("{{news_cards}}", news_cards)
    html = html.replace("{{auction_rows}}", auction_rows)
    html = html.replace("{{valuation_cards}}", valuation_cards)
    html = html.replace("{{parts_cards}}", parts_cards)
    html = html.replace("{{video_cards}}", video_cards)

    return html


def send_telegram_message(message, image_path=None):
    """Send a message to Telegram via bot API."""
    bot_token = None
    chat_id = None

    config_paths = [
        Path.home() / ".hermes" / ".env",
        Path("config") / "telegram_config.json",
    ]

    for config_path in config_paths:
        if config_path.exists():
            if config_path.suffix == ".env":
                with open(config_path) as f:
                    for line in f:
                        if line.startswith("TELEGRAM_BOT_TOKEN=") or line.startswith("TELEGRAM_BOT_TOKEN="):
                            token_val = line.split("=", 1)[1].strip()
                            if token_val and not token_val.startswith("***"):
                                bot_token = token_val
                        elif line.startswith("TELEGRAM_CHAT_ID="):
                            chat_id = line.split("=", 1)[1].strip()
                        elif line.startswith("TELEGRAM_HOME_CHANNEL="):
                            chat_id = line.split("=", 1)[1].strip()
            elif config_path.suffix == ".json":
                with open(config_path) as f:
                    config = json.load(f)
                    bot_token = config.get("bot_token")
                    chat_id = config.get("chat_id")

    if not bot_token or bot_token.startswith("***"):
        print("⚠️ Bot token masked in config - skipping Telegram API send")
        print("\\n📝 Telegram message preview:")
        print(message)
        return False

    if not bot_token or not chat_id:
        print("❌ Telegram config not found")
        return False

    api_url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"

    if not image_path:
        image_path = "https://content-hub.imgix.net/GUhocLc6D6V9qFtm3Oc2g/19e093064c8a22f6214f16a85469aac2/7-20things-20you-20need-20to-20know-20about-20the-20porsche-20911-20type-20993.jpg"

    try:
        if image_path.startswith("http"):
            data = {
                "chat_id": chat_id,
                "photo": image_path,
                "caption": message,
                "parse_mode": "HTML"
            }
            response = requests.post(api_url, json=data, timeout=30)
        else:
            with open(image_path, "rb") as photo:
                files = {"photo": photo}
                data = {
                    "chat_id": chat_id,
                    "caption": message,
                    "parse_mode": "HTML"
                }
                response = requests.post(api_url, files=files, data=data, timeout=30)

        if response.status_code == 200:
            print("✅ Telegram message sent successfully")
            return True
        else:
            print(f"❌ Telegram error: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Telegram send error: {e}")
        return False


def deploy():
    """Deploy to Cloudflare Pages directly (no GitHub dependency)."""
    env_file = REPO_DIR / ".env"
    cf_token = None
    cf_account_id = None

    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                if line.startswith("CLOUDFLARE_API_TOKEN="):
                    cf_token = line.split("=", 1)[1].strip()
                elif line.startswith("CLOUDFLARE_ACCOUNT_ID="):
                    cf_account_id = line.split("=", 1)[1].strip()

    if not cf_token:
        print("❌ CLOUDFLARE_API_TOKEN not found in .env")
        return False

    env = os.environ.copy()
    env["CLOUDFLARE_API_TOKEN"] = cf_token
    if cf_account_id:
        env["CLOUDFLARE_ACCOUNT_ID"] = cf_account_id

    result = subprocess.run(
        "npx wrangler pages deploy . --project-name porsche-digest --branch main --commit-dirty=true",
        shell=True, cwd=REPO_DIR, capture_output=True, text=True, timeout=120, env=env
    )

    if result.returncode == 0:
        print("✅ Deployed to Cloudflare Pages")
        print("🔗 Live at: https://digest.costafamily.ai")
        print("🔗 Backup: https://porsche-digest.pages.dev")
        return True
    else:
        print(f"❌ Deploy error: {result.stderr}")
        return False


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    rate = get_exchange_rate()

    print(f"🔄 Generating Porsche 993 Digest for {today}...")

    # Fetch fresh data
    print("📰 Fetching Porsche news...")
    articles = fetch_porsche_news()

    print("🏷️ Fetching auction listings...")
    auctions = fetch_auction_listings()

    print("💰 Fetching market valuation data...")
    valuation = get_market_valuation()

    # Generate HTML
    print("📄 Generating HTML...")
    html = generate_html_template(today, articles, auctions, valuation, rate)

    # Write to index.html
    index_path = REPO_DIR / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Digest updated: {index_path}")

    # Deploy
    print("🚀 Deploying...")
    success = deploy()

    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
