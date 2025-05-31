#!/usr/bin/env python3
"""
CryptoBuddy - Your AI-Powered Cryptocurrency Advisor
A rule-based chatbot that provides crypto investment advice based on 
profitability and sustainability factors.
"""

import re
import random
from crypto_data import crypto_db, get_most_sustainable, get_trending_cryptos, get_low_energy_cryptos, get_high_market_cap_cryptos

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.greeting_messages = [
            f"Hey there! I'm {self.name}, your crypto sidekick! 🚀",
            f"Welcome to {self.name}! Ready to explore the crypto universe? 🌟",
            f"Hi! {self.name} here to help you navigate the wild world of crypto! 💎"
        ]
        self.conversation_active = True
        
    def display_welcome(self):
        """Display welcome message and available commands"""
        print("=" * 60)
        print(random.choice(self.greeting_messages))
        print("=" * 60)
        print("\n🤖 What I can help you with:")
        print("• Find trending cryptocurrencies")
        print("• Recommend sustainable crypto options")
        print("• Analyze crypto profitability")
        print("• Provide general crypto advice")
        print("• Show all available cryptocurrencies")
        print("\n💡 Try asking me things like:")
        print("- 'Which crypto is trending up?'")
        print("- 'What's the most sustainable coin?'")
        print("- 'Show me all cryptos'")
        print("- 'Help me choose a crypto for long-term investment'")
        print("\n📝 Type 'help' for commands or 'quit' to exit")
        print("-" * 60)

    def normalize_input(self, user_input):
        """Normalize user input for better matching"""
        return user_input.lower().strip()

    def analyze_query(self, query):
        """Analyze user query and determine intent"""
        query = self.normalize_input(query)
        
        # Define keyword patterns for different intents
        intents = {
            'sustainable': ['sustainable', 'eco', 'green', 'environment', 'energy', 'eco-friendly'],
            'trending': ['trending', 'rising', 'growing', 'up', 'bullish', 'hot'],
            'profitable': ['profitable', 'profit', 'gain', 'money', 'invest', 'buy'],
            'all_cryptos': ['all', 'list', 'show', 'available', 'what cryptos'],
            'specific_crypto': list(crypto_db.keys()) + [crypto_db[k]['symbol'].lower() for k in crypto_db.keys()],
            'help': ['help', 'commands', 'what can you do'],
            'long_term': ['long-term', 'long term', 'future', 'hold'],
            'risky': ['risky', 'risk', 'volatile', 'dangerous']
        }
        
        detected_intents = []
        for intent, keywords in intents.items():
            if any(keyword in query for keyword in keywords):
                detected_intents.append(intent)
                
        return detected_intents

    def get_crypto_info(self, crypto_name):
        """Get detailed information about a specific cryptocurrency"""
        if crypto_name in crypto_db:
            crypto = crypto_db[crypto_name]
            sustainability_percentage = (crypto['sustainability_score'] / crypto['max_sustainability']) * 100
            
            info = f"\n🪙 **{crypto_name} ({crypto['symbol']})**\n"
            info += f"📈 Price Trend: {crypto['price_trend'].title()}\n"
            info += f"💰 Market Cap: {crypto['market_cap'].title()}\n"
            info += f"⚡ Energy Use: {crypto['energy_use'].title()}\n"
            info += f"🌱 Sustainability: {crypto['sustainability_score']}/10 ({sustainability_percentage:.0f}%)\n"
            info += f"⚠️ Risk Level: {crypto['risk_level'].title()}\n"
            info += f"📝 Description: {crypto['description']}\n"
            
            return info
        return f"Sorry, I don't have information about {crypto_name} in my database."

    def recommend_sustainable_crypto(self):
        """Recommend the most sustainable cryptocurrency"""
        most_sustainable = get_most_sustainable()
        crypto = crypto_db[most_sustainable]
        
        response = f"🌱 For sustainability, I recommend **{most_sustainable}**!\n\n"
        response += f"Here's why:\n"
        response += f"• Sustainability score: {crypto['sustainability_score']}/10\n"
        response += f"• Energy use: {crypto['energy_use']}\n"
        response += f"• {crypto['description']}\n\n"
        response += "💚 It's eco-friendly and has great long-term potential!"
        
        return response

    def recommend_trending_cryptos(self):
        """Recommend trending cryptocurrencies"""
        trending = get_trending_cryptos()
        
        if not trending:
            return "🤔 No cryptocurrencies are showing strong upward trends right now."
        
        response = "🚀 Here are the trending cryptocurrencies:\n\n"
        for crypto in trending:
            data = crypto_db[crypto]
            response += f"• **{crypto}** ({data['symbol']}) - {data['description'][:50]}...\n"
        
        response += "\n📈 These cryptos are showing upward price momentum!"
        return response

    def recommend_for_investment(self):
        """Provide balanced investment recommendation"""
        # Find cryptos that are both trending and have decent sustainability
        trending = get_trending_cryptos()
        sustainable_options = [crypto for crypto in crypto_db if crypto_db[crypto]['sustainability_score'] >= 6]
        
        balanced_options = list(set(trending) & set(sustainable_options))
        
        if balanced_options:
            recommended = balanced_options[0]  # Take the first match
            crypto = crypto_db[recommended]
            
            response = f"💡 For balanced investment, I suggest **{recommended}**!\n\n"
            response += f"Why it's a good choice:\n"
            response += f"✅ Price trend: {crypto['price_trend']}\n"
            response += f"✅ Sustainability score: {crypto['sustainability_score']}/10\n"
            response += f"✅ Market position: {crypto['market_cap']} market cap\n"
            response += f"✅ Energy efficiency: {crypto['energy_use']} energy use\n\n"
            response += f"📝 {crypto['description']}"
        else:
            response = "🤔 Based on current data, consider diversifying between:\n"
            response += f"• **{get_most_sustainable()}** (most sustainable)\n"
            response += f"• **{trending[0] if trending else 'Bitcoin'}** (trending option)\n"
        
        return response

    def show_all_cryptos(self):
        """Display all available cryptocurrencies"""
        response = "🪙 Available Cryptocurrencies in my database:\n\n"
        
        for crypto_name, data in crypto_db.items():
            sustainability_bar = "🟢" * data['sustainability_score'] + "⚪" * (10 - data['sustainability_score'])
            trend_emoji = "📈" if data['price_trend'] == "rising" else "📊"
            
            response += f"{trend_emoji} **{crypto_name}** ({data['symbol']})\n"
            response += f"   Sustainability: {sustainability_bar} {data['sustainability_score']}/10\n"
            response += f"   Trend: {data['price_trend'].title()} | Cap: {data['market_cap'].title()}\n\n"
        
        return response

    def show_help(self):
        """Display help information"""
        help_text = """
🤖 **CryptoBuddy Commands & Features:**

**Ask me about:**
• Sustainable cryptocurrencies: "What's the most eco-friendly crypto?"
• Trending cryptos: "Which cryptos are rising?"
• Investment advice: "What should I invest in?"
• Specific cryptos: "Tell me about Bitcoin" or "What is ADA?"
• All options: "Show me all cryptos"

**Sample Questions:**
• "Which crypto is best for long-term holding?"
• "What's trending up right now?"
• "Show me sustainable options"
• "Tell me about Ethereum"
• "What crypto should I buy?"

**Commands:**
• 'help' - Show this help message
• 'quit' or 'exit' - End conversation
• 'list' or 'all' - Show all cryptocurrencies

💡 **Tip:** I understand natural language, so feel free to ask in your own words!
        """
        return help_text

    def generate_response(self, user_input):
        """Generate appropriate response based on user input"""
        if not user_input.strip():
            return "🤔 I didn't catch that. Could you ask me something about crypto?"
        
        intents = self.analyze_query(user_input)
        query = self.normalize_input(user_input)
        
        # Handle specific commands
        if any(cmd in query for cmd in ['quit', 'exit', 'bye', 'goodbye']):
            self.conversation_active = False
            return "👋 Thanks for chatting! Remember: crypto is risky—always do your own research! 💎🚀"
        
        if 'help' in intents:
            return self.show_help()
        
        if 'all_cryptos' in intents:
            return self.show_all_cryptos()
        
        # Check for specific cryptocurrency mentions
        for crypto_name in crypto_db.keys():
            if crypto_name.lower() in query or crypto_db[crypto_name]['symbol'].lower() in query:
                return self.get_crypto_info(crypto_name)
        
        # Handle intent-based responses
        if 'sustainable' in intents:
            return self.recommend_sustainable_crypto()
        
        if 'trending' in intents:
            return self.recommend_trending_cryptos()
        
        if 'profitable' in intents or 'long_term' in intents:
            return self.recommend_for_investment()
        
        # Default response for unmatched queries
        responses = [
            "🤔 That's interesting! Could you be more specific? Try asking about trending cryptos or sustainable options.",
            "💡 I can help you with crypto advice! Ask me about sustainable coins, trending options, or specific cryptocurrencies.",
            "🚀 Want to know about crypto trends, sustainability, or get investment advice? Just ask!",
        ]
        
        return random.choice(responses)

    def add_disclaimer(self, response):
        """Add risk disclaimer to investment advice"""
        disclaimers = [
            "\n⚠️ **Disclaimer:** Crypto investments are highly risky. Always do your own research!",
            "\n📚 **Remember:** This is educational content only. Consult financial advisors for investment decisions!",
            "\n🚨 **Risk Warning:** Cryptocurrency markets are volatile. Never invest more than you can afford to lose!"
        ]
        
        # Add disclaimer to investment-related responses
        investment_keywords = ['recommend', 'invest', 'buy', 'suggest', 'choose']
        if any(keyword in response.lower() for keyword in investment_keywords):
            response += random.choice(disclaimers)
        
        return response

    def chat(self):
        """Main chat loop"""
        self.display_welcome()
        
        while self.conversation_active:
            try:
                user_input = input(f"\n💬 You: ").strip()
                
                if not user_input:
                    continue
                    
                response = self.generate_response(user_input)
                response = self.add_disclaimer(response)
                
                print(f"\n🤖 {self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n👋 {self.name}: Goodbye! Stay safe in the crypto world! 🚀")
                break
            except Exception as e:
                print(f"\n🚨 {self.name}: Oops! Something went wrong. Let's try again!")
                print(f"Error: {str(e)}")

def main():
    """Main function to run the chatbot"""
    print("🚀 Initializing CryptoBuddy...")
    bot = CryptoBuddy()
    bot.chat()

if __name__ == "__main__":
    main()