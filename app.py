from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# 🌟 FUCKING PREMIUM DATA 🌟
luxury_coffees = [
    {
        "id": 1, 
        "name": "💎 DIAMOND DUST CAPPUCCINO", 
        "price": 49.99, 
        "description": "Ethiopian Yirgacheffe with 24k gold leaf & crushed diamonds", 
        "emoji": "☕💎",
        "category": "imperial",
        "ingredients": ["Rare Ethiopian beans", "24k gold leaf", "Diamond dust", "Crystal water"]
    },
    {
        "id": 2, 
        "name": "🪷 BLACK TRUFFLE VELVET", 
        "price": 89.99, 
        "description": "Italian espresso with French Perigord truffle infusion", 
        "emoji": "🍄🖤",
        "category": "royal",
        "ingredients": ["Perigord black truffle", "Italian espresso", "Velvet cream", "Himalayan salt"]
    },
    {
        "id": 3, 
        "name": "🌹 SAFFRON ROSE KINGDOM", 
        "price": 67.99, 
        "description": "Persian saffron threads with organic Damask rose petals", 
        "emoji": "🌹👑",
        "category": "royal", 
        "ingredients": ["Persian saffron", "Damask roses", "Arabian coffee", "Rose quartz syrup"]
    }
]

luxury_pastries = [
    {
        "id": 4,
        "name": "🐟 CAVIAR CROISSANT",
        "price": 125.99,
        "description": "French butter croissant with Imperial beluga caviar",
        "emoji": "🥐🐟",
        "category": "imperial",
        "ingredients": ["Beluga caviar", "French butter", "Gold leaf", "Truffle oil"]
    },
    {
        "id": 5,
        "name": "🍄 TRUFFLE VOLCANO",
        "price": 78.99, 
        "description": "72-layer pastry with wild mushroom & black truffle lava",
        "emoji": "🌋🍄",
        "category": "royal",
        "ingredients": ["Black truffle", "Wild mushrooms", "72-layer pastry", "Truffle lava"]
    }
]

# 🎨 FUCKING LUXURY STYLES 🎨
LUXURY_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Inter:wght@300;400;500&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Inter', sans-serif;
        background: #000000;
        color: #f0f0f0;
        overflow-x: hidden;
        line-height: 1.6;
    }
    
    .imperial-bg {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #2d1b0e 100%);
        position: relative;
    }
    
    .imperial-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 215, 0, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(120, 119, 198, 0.05) 0%, transparent 50%);
        animation: pulse 8s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 0.8; }
    }
    
    .luxury-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 20px;
        position: relative;
        z-index: 2;
    }
    
    /* 🏰 FUCKING HERO SECTION 🏰 */
    .imperial-hero {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-content h1 {
        font-family: 'Cinzel', serif;
        font-size: 6rem;
        font-weight: 900;
        background: linear-gradient(45deg, #D4AF37, #FFD700, #CFB53B, #D4AF37);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s ease-in-out infinite;
        margin-bottom: 1rem;
        text-shadow: 0 0 60px rgba(212, 175, 55, 0.5);
        letter-spacing: 3px;
    }
    
    @keyframes shimmer {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .hero-subtitle {
        font-size: 1.8rem;
        color: #b8b8b8;
        margin-bottom: 3rem;
        font-weight: 300;
        letter-spacing: 4px;
        text-transform: uppercase;
    }
    
    /* 💎 FUCKING BUTTONS 💎 */
    .imperial-btn {
        background: linear-gradient(135deg, #D4AF37 0%, #FFD700 50%, #CFB53B 100%);
        color: #000000;
        padding: 22px 48px;
        border: none;
        border-radius: 50px;
        font-size: 1.3rem;
        font-weight: 700;
        text-decoration: none;
        display: inline-block;
        margin: 15px 20px;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        box-shadow: 
            0 8px 32px rgba(212, 175, 55, 0.3),
            0 0 0 1px rgba(212, 175, 55, 0.1);
        position: relative;
        overflow: hidden;
        letter-spacing: 1px;
    }
    
    .imperial-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: 0.6s;
    }
    
    .imperial-btn:hover::before {
        left: 100%;
    }
    
    .imperial-btn:hover {
        transform: translateY(-8px) scale(1.05);
        box-shadow: 
            0 20px 40px rgba(212, 175, 55, 0.5),
            0 0 30px rgba(212, 175, 55, 0.3),
            inset 0 0 20px rgba(255, 255, 255, 0.1);
    }
    
    /* 👑 FUCKING NAVIGATION 👑 */
    .imperial-nav {
        position: fixed;
        top: 0;
        width: 100%;
        background: rgba(10, 10, 10, 0.95);
        backdrop-filter: blur(20px);
        z-index: 10000;
        padding: 1.2rem 0;
        border-bottom: 1px solid rgba(212, 175, 55, 0.2);
    }
    
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .nav-logo {
        font-family: 'Cinzel', serif;
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(45deg, #D4AF37, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .nav-links a {
        color: #e8e8e8;
        text-decoration: none;
        margin: 0 2rem;
        font-weight: 400;
        transition: all 0.3s ease;
        position: relative;
        font-size: 1.1rem;
    }
    
    .nav-links a::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(45deg, #D4AF37, #FFD700);
        transition: width 0.3s ease;
    }
    
    .nav-links a:hover::after {
        width: 100%;
    }
    
    .nav-links a:hover {
        color: #D4AF37;
    }
    
    /* 🏆 FUCKING MENU CARDS 🏆 */
    .imperial-section {
        padding: 120px 0;
        position: relative;
    }
    
    .section-title {
        font-family: 'Cinzel', serif;
        font-size: 4rem;
        text-align: center;
        margin-bottom: 5rem;
        background: linear-gradient(45deg, #D4AF37, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 3px;
        background: linear-gradient(45deg, #D4AF37, #FFD700);
    }
    
    .imperial-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
        gap: 3rem;
        margin-top: 4rem;
    }
    
    .imperial-card {
        background: linear-gradient(145deg, #1a1a1a, #222222);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 25px;
        padding: 3rem;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        position: relative;
        overflow: hidden;
    }
    
    .imperial-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #D4AF37, #FFD700, #D4AF37);
        background-size: 200% 100%;
        animation: shimmer 2s linear infinite;
    }
    
    .imperial-card:hover {
        transform: translateY(-15px) scale(1.02);
        border-color: #D4AF37;
        box-shadow: 
            0 25px 50px rgba(0,0,0,0.5),
            0 0 80px rgba(212, 175, 55, 0.2);
    }
    
    .item-emoji {
        font-size: 4rem;
        margin-bottom: 1.5rem;
        text-shadow: 0 0 30px rgba(212, 175, 55, 0.5);
    }
    
    .item-name {
        font-family: 'Cinzel', serif;
        font-size: 2rem;
        color: #D4AF37;
        margin-bottom: 1rem;
        letter-spacing: 1px;
    }
    
    .item-price {
        font-size: 2.5rem;
        font-weight: 700;
        color: #FFD700;
        margin: 1.5rem 0;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
    }
    
    .item-description {
        color: #b8b8b8;
        font-size: 1.1rem;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }
    
    .item-ingredients {
        color: #888;
        font-size: 0.9rem;
        font-style: italic;
        margin-bottom: 1.5rem;
    }
    
    .item-category {
        display: inline-block;
        padding: 8px 20px;
        background: rgba(212, 175, 55, 0.1);
        color: #D4AF37;
        border-radius: 20px;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        border: 1px solid rgba(212, 175, 55, 0.3);
    }
    
    /* 🌟 FUCKING FOOTER 🌟 */
    .imperial-footer {
        background: #0a0a0a;
        padding: 4rem 0 2rem;
        border-top: 1px solid rgba(212, 175, 55, 0.2);
        text-align: center;
    }
    
    .footer-content {
        opacity: 0.7;
        font-size: 0.9rem;
    }
    
    /* 📱 FUCKING RESPONSIVE 📱 */
    @media (max-width: 768px) {
        .hero-content h1 {
            font-size: 3.5rem;
        }
        
        .imperial-grid {
            grid-template-columns: 1fr;
        }
        
        .nav-links {
            display: none;
        }
    }
</style>
"""

# 🏰 FUCKING HTML TEMPLATES 🏰
def generate_homepage():
    return LUXURY_CSS + """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IMPERIAL CAFE | Beyond Luxury</title>
    </head>
    <body class="imperial-bg">
        <nav class="imperial-nav">
            <div class="luxury-container nav-content">
                <div class="nav-logo">👑 IMPERIAL</div>
                <div class="nav-links">
                    <a href="/">SANCTUARY</a>
                    <a href="/menu">MANIFESTO</a>
                    <a href="/reservations">AUDIENCE</a>
                    <a href="/contact">COUNCIL</a>
                </div>
            </div>
        </nav>

        <section class="imperial-hero">
            <div class="hero-content">
                <h1>IMPERIAL CAFE</h1>
                <p class="hero-subtitle">WHERE ROYALTY BREWS & LEGENDS SIP</p>
                <div class="hero-buttons">
                    <a href="/menu" class="imperial-btn">EXPLORE THE MANIFESTO</a>
                    <a href="/reservations" class="imperial-btn" style="background: transparent; border: 3px solid #D4AF37; color: #D4AF37;">REQUEST AUDIENCE</a>
                </div>
            </div>
        </section>

        <footer class="imperial-footer">
            <div class="luxury-container footer-content">
                <p>© 2024 IMPERIAL CAFE. CRAFTED FOR THOSE WHO DEMAND EXCELLENCE.</p>
                <p>🏰 THE ROYAL DISTRICT | ⏰ 24/7 EXCLUSIVITY</p>
            </div>
        </footer>
    </body>
    </html>
    """

def generate_menu_page():
    coffee_cards = ""
    for coffee in luxury_coffees:
        ingredients = " • ".join(coffee['ingredients'])
        coffee_cards += f"""
        <div class="imperial-card">
            <div class="item-emoji">{coffee['emoji']}</div>
            <h3 class="item-name">{coffee['name']}</h3>
            <div class="item-price">${coffee['price']}</div>
            <p class="item-description">{coffee['description']}</p>
            <p class="item-ingredients">{ingredients}</p>
            <span class="item-category">{coffee['category']}</span>
        </div>
        """
    
    pastry_cards = ""
    for pastry in luxury_pastries:
        ingredients = " • ".join(pastry['ingredients'])
        pastry_cards += f"""
        <div class="imperial-card">
            <div class="item-emoji">{pastry['emoji']}</div>
            <h3 class="item-name">{pastry['name']}</h3>
            <div class="item-price">${pastry['price']}</div>
            <p class="item-description">{pastry['description']}</p>
            <p class="item-ingredients">{ingredients}</p>
            <span class="item-category">{pastry['category']}</span>
        </div>
        """
    
    return LUXURY_CSS + f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MANIFESTO | IMPERIAL CAFE</title>
    </head>
    <body class="imperial-bg">
        <nav class="imperial-nav">
            <div class="luxury-container nav-content">
                <div class="nav-logo">👑 IMPERIAL</div>
                <div class="nav-links">
                    <a href="/">SANCTUARY</a>
                    <a href="/menu">MANIFESTO</a>
                    <a href="/reservations">AUDIENCE</a>
                    <a href="/contact">COUNCIL</a>
                </div>
            </div>
        </nav>

        <section class="imperial-section">
            <div class="luxury-container">
                <h2 class="section-title">ROYAL BREWS</h2>
                <div class="imperial-grid">
                    {coffee_cards}
                </div>
                
                <h2 class="section-title" style="margin-top: 8rem;">IMPERIAL PASTRIES</h2>
                <div class="imperial-grid">
                    {pastry_cards}
                </div>
            </div>
        </section>

        <footer class="imperial-footer">
            <div class="luxury-container footer-content">
                <p>© 2024 IMPERIAL CAFE. EACH ITEM CRAFTED WITH ROYAL PRECISION.</p>
            </div>
        </footer>
    </body>
    </html>
    """

# 👑 FUCKING ROUTES 👑
@app.route('/')
def imperial_home():
    return render_template_string(generate_homepage())

@app.route('/menu')
def imperial_menu():
    return render_template_string(generate_menu_page())

@app.route('/reservations')
def imperial_reservations():
    reservations_html = LUXURY_CSS + """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AUDIENCE | IMPERIAL CAFE</title>
    </head>
    <body class="imperial-bg">
        <nav class="imperial-nav">
            <div class="luxury-container nav-content">
                <div class="nav-logo">👑 IMPERIAL</div>
                <div class="nav-links">
                    <a href="/">SANCTUARY</a>
                    <a href="/menu">MANIFESTO</a>
                    <a href="/reservations">AUDIENCE</a>
                    <a href="/contact">COUNCIL</a>
                </div>
            </div>
        </nav>

        <section class="imperial-hero" style="min-height: 80vh;">
            <div class="hero-content">
                <h1>REQUEST AUDIENCE</h1>
                <p class="hero-subtitle">YOUR ROYAL EXPERIENCE AWAITS</p>
                <p style="color: #b8b8b8; margin-bottom: 3rem; max-width: 600px; font-size: 1.2rem;">
                    For reservations and exclusive events, contact our Royal Concierge<br>
                    <span style="color: #D4AF37; font-size: 1.5rem; display: block; margin-top: 1rem;">📞 +1 (888) IMPERIAL</span>
                </p>
                <a href="/menu" class="imperial-btn">PERUSE THE MANIFESTO WHILE YOU WAIT</a>
            </div>
        </section>
    </body>
    </html>
    """
    return render_template_string(reservations_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)