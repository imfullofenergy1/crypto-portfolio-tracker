# 🧠 Crypto Portfolio Tracker

A Flask web app that tracks your real-time crypto wallet balances (ETH + tokens) using the Etherscan API, and displays the data in a clean, responsive dashboard.
## 🔗 Live Demo

👉 [Check out the deployed app on Render](https://crypto-portfolio-tracker-1-uy2.onrender.com)

## ✅ Features
- Connects to your MetaMask or Trust Wallet address
- Fetches ETH and token balances from Etherscan
- Displays current token balances and USD value
- Clean UI with Flask and Jinja templates
- `.env` support for API key and wallet privacy

## 📸 Demo
Visit: `http://127.0.0.1:5000`  
You’ll see token balance and value for your specified wallet(s).

## 🧪 How to Run
```bash
git clone https://github.com/imfullofenergy1/crypto-portfolio-tracker.git
cd crypto-portfolio-tracker
cp .env.example .env  # Then edit it with your wallet address and Etherscan API key
pip install -r requirements.txt
python run.py
🔐 Environment Variables
Create a .env file with:

ini
Copy
Edit
ETHERSCAN_API_KEY=your_api_key
WALLET_ADDRESS=your_wallet_address
📁 Project Structure
arduino
Copy
Edit
app/
├── main.py
├── tracker.py
├── templates/
│   └── dashboard.html
.env
run.py
🌱 Future Roadmap
✅ Add multi-wallet support (in progress)

🔄 Kraken BTC tracking via API

🔄 Yield farming dashboard for Ethena

🔒 Add user authentication (optional)

🛠️ Tech Stack
Python 3.11

Flask

Etherscan API

dotenv

HTML + CSS + Jinja templates

🧠 Author
Omari Miller
GitHub

Feel free to fork, improve, and connect your own APIs 🔗

yaml
Copy
Edit

---

✅ Once you paste that into your `README.md`, save and commit it:

```bash
git add README.md
git commit -m "Updated README with project details"
git push
