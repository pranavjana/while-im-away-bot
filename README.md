# **While I'm Away**

## **Overview**
**"While I'm Away"** is a Telegram bot designed to keep you connected to your loved ones even when you can't be there. It offers mood-based, heartfelt messages that adapt to how the user feels—whether they need a bit of support, motivation, a laugh, or a loving reminder. With **"While I'm Away"**, distance no longer has to mean disconnected.

---

## **Features**

- **Sentiment-Based Responses**: Uses TextBlob to understand user sentiment and provide appropriate responses.
  - **Supportive Messages**: When times are tough, receive comforting words.
  - **Motivational Messages**: Find encouragement and positivity when you're feeling good or striving for more.
  - **Funny or Romantic Messages**: Lighten the mood with humor or express affection to brighten someone's day.

- **Interactive Menu**: The bot provides an easy-to-use menu that allows users to choose from categories such as:
  - **Supportive**
  - **Motivational**
  - **Funny**
  - **Romantic**

- **Neutral Sentiment Handling**: When a user's input is neutral, the bot responds with:
  
  > "Thank you for sharing how you're feeling! I'll be back soon, but in the meantime, I'm here to keep you company. If you'd like something to brighten your day, pick one of these options: Supportive, Motivational, Funny, Romantic."

- **Customizable Messages**: Easily expand or modify message categories to create the perfect experience tailored to your needs.

---

## **How It Works**
1. **User Interaction**: The user tells the bot how they feel.
2. **Sentiment Analysis**: The bot uses **TextBlob** to determine the sentiment of the user's input (positive, negative, or neutral).
   - **Positive**: Motivational or cheerful messages.
   - **Negative**: Supportive and empathetic responses.
   - **Neutral**: A comforting response with an interactive menu for further uplifting options.
3. **Interactive Options**: Users can choose from predefined categories to receive specific messages based on what they need most at that moment.

---

## **Getting Started**

### **Prerequisites**
- Python 3.6 or above
- A Telegram account to set up and interact with the bot

### **Installation**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/while-im-away.git
   ```
2. **Navigate to the Project Directory**
   ```bash
   cd while-im-away
   ```
3. **Install Required Libraries**
   Use `pip` to install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables**
   Create a `.env` file to store your Telegram bot token:
   ```plaintext
   TELEGRAM_TOKEN=your-telegram-bot-token
   ```

5. **Run the Bot**
   ```bash
   python bot.py
   ```

---

## **Configuration**
To modify or add to the predefined messages, navigate to the **`messages.py`** file. Messages are stored in a dictionary format, and you can easily add more categories or edit existing ones.

---

## **Usage**
Once the bot is up and running, simply open Telegram, find your bot, and start a conversation. Type in how you're feeling, and let the bot do the rest—offering appropriate messages to comfort or motivate you.

**Example Commands:**
- **"I'm having a rough day."** The bot will respond with a supportive message to lift your spirits.
- **"I feel great today!"** The bot will respond with a motivational message to keep your energy up.
- If your input is neutral, the bot will offer you categories to choose from.

---

## **Technologies Used**
- **Python**: The primary programming language.
- **TextBlob**: For sentiment analysis of user inputs.
- **Telegram Bot API**: To interact with users and send messages.

---



