# api-security-header-scanner
Open-source tool to check website security headers and detect exposed API keys
# 🔒 API Security & Header Scanner

**Automated security checker for exposed API keys, weak headers, and common vulnerabilities.**

A lightweight Python script that scans websites for:
- Exposed API keys (Stripe, AWS, OpenAI, etc.)
- Missing security headers (CSP, HSTS, X-Frame-Options)
- Insecure configurations
- Common OWASP vulnerabilities

Perfect for bug bounty hunters, security researchers, and developers who want to quickly audit a site before launch.

---

## 🚀 Quick Start
```bash
# Clone the repo
git clone https://github.com/CyberCheckerdev/api-security-header-scanner.git
cd api-security-header-scanner

# Install dependencies
pip install requests beautifulsoup4

# Run scan
python scanner.py https://example.com
```

---

## 📋 What It Checks

### Security Headers
- ✅ Content-Security-Policy (CSP)
- ✅ Strict-Transport-Security (HSTS)
- ✅ X-Frame-Options (Clickjacking protection)
- ✅ X-Content-Type-Options
- ✅ X-XSS-Protection
- ✅ Referrer-Policy

### API Key Exposure
Detects exposed keys for:
- Stripe (`sk_live_`, `pk_live_`)
- AWS (`AKIA`, `aws_access_key`)
- OpenAI (`sk-proj-`)
- Google Maps, SendGrid, Twilio, and 20+ more services

### Common Vulnerabilities
- Mixed content warnings (HTTP resources on HTTPS)
- Directory listing enabled
- Exposed `.env` and `.git` files
- Weak SSL/TLS configuration

---

## 🛠️ Example Output
```
🔍 Scanning: https://example.com

✅ HTTPS: Enabled
✅ HSTS: max-age=31536000
❌ CSP: Missing (High Risk)
❌ X-Frame-Options: Missing (Clickjacking Risk)

🔑 API Keys Found:
❌ Stripe Live Key: sk_live_51Hxxx... (Line 42 in main.js)
❌ AWS Access Key: AKIAI5xxx... (Exposed in HTML)

⚠️  Configuration Issues:
❌ .env file publicly accessible
✅ robots.txt configured correctly

Security Score: 4/10 (Critical Issues Found)
```

---

## 🎯 For Deep Scans & Automated Monitoring

This script provides a quick manual check, but for **continuous monitoring, automated scanning, and compliance reports**, check out:

👉 **[CyberChecker.com](https://cyber-checker.com)** — Full security audit in 60 seconds

Features the open-source scanner doesn't have:
- Real-time monitoring (alerts when new vulnerabilities appear)
- Supabase RLS policy checker
- WordPress plugin vulnerability database
- Compliance reports (GDPR, OWASP Top 10)
- Historical tracking (see security improvements over time)
- API for CI/CD integration

**Free tier available** — no credit card required.

---

## 📦 Installation

### Requirements
- Python 3.7+
- `requests` library
- `beautifulsoup4` library

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💡 Usage Examples

### Basic Scan
```bash
python scanner.py https://yourwebsite.com
```

### Export to JSON
```bash
python scanner.py https://yourwebsite.com --output json > report.json
```

### Scan Multiple URLs
```bash
python scanner.py --file urls.txt
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

Areas where contributions are needed:
- Additional API key patterns
- More security header checks
- CMS-specific vulnerability checks (WordPress, Drupal, etc.)
- Performance optimizations

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file

---

## ⚠️ Disclaimer

This tool is for **educational and authorized security testing only**. Only scan websites you own or have explicit permission to test. Unauthorized scanning may be illegal in your jurisdiction.

---

## 🔗 Links

- **Website:** [CyberChecker.com](https://cyber-checker.com)
- **Blog:** [Security Guides & Tutorials](https://cyber-checker.com/blog)
- **Issues:** [Report bugs or request features](https://github.com/CyberCheckerdev/api-security-header-scanner/issues)

---

## 🏆 Featured In

- Awesome Security Tools
- Bug Bounty Tools List
- InfoSec Resources 2026

---

**Built with ❤️ for the security community**
