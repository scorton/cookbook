# 🌐 Dark Web Analysis Tool

A Python-based tool for analyzing dark web (.onion) websites and regular websites for security-related content. This tool extracts text data, detects security patterns, calculates risk scores, and generates comprehensive analysis reports.

## 🎯 Purpose

This tool is designed to collect and analyze text data from websites (including dark web .onion sites) to identify potential cybersecurity issues such as:
- Exploit discussions and vulnerabilities (CVEs)
- Malware and ransomware mentions
- Financial crimes (carding, credit card fraud)
- Hacking services and DDoS-for-hire
- Credential leaks and data breaches
- Weapons, drugs, and fraud-related content

## ✨ Features

- ✅ **Tor Integration**: Seamlessly connects to .onion sites through Tor SOCKS5 proxy
- ✅ **Automated Tor Check**: Verifies Tor connection before analysis
- ✅ **Pattern Detection**: Uses regex patterns to identify 8+ security-related categories
- ✅ **Risk Scoring**: Calculates a risk score (0-100) based on detected threats
- ✅ **Comprehensive Reports**: Saves detailed analysis reports with timestamps
- ✅ **Text Extraction**: Extracts and saves all text content from websites
- ✅ **Hypothesis Generation**: Provides insights about detected threats
- ✅ **User-Friendly Output**: Color-coded console output with emojis

## 📋 Requirements

### System Requirements
- Python 3.7+
- Tor service running on port 9050
- macOS, Linux, or Windows

### Python Dependencies
```bash
requests
beautifulsoup4
python-whois
PySocks  # For SOCKS proxy support
```

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/EngrAhmadofficial/cyber_analysis_scrripts.git
cd cyber_analysis_scrripts
```

### 2. Create Virtual Environment (Recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install requests beautifulsoup4 python-whois PySocks
```

### 4. Install and Start Tor

**macOS:**
```bash
brew install tor
tor &
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt-get install tor
sudo service tor start
```

**Verify Tor is Running:**
```bash
lsof -i :9050  # Should show tor process listening on port 9050
```

## 💻 Usage

### Basic Usage
```bash
python website_analysis.py
```

The tool will:
1. Check if Tor is running and properly configured
2. Prompt you to enter a URL (.onion or regular website)
3. Fetch and analyze the website content
4. Generate a detailed report file

### Example Session
```
🌐 DARK WEB ANALYSIS TOOL
==================================================
🔍 Checking Tor connection...
✅ Tor is working correctly!

💡 Try these test URLs:
   • http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion
   • http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/

Enter website URL: http://example.onion

🚀 Starting analysis of: http://example.onion
🔍 Connecting to: http://example.onion
🌐 Using Tor proxy: socks5h://127.0.0.1:9050
✅ Successfully fetched webpage

✅ ANALYSIS COMPLETE!
📁 Report saved to: analysis_example_onion_20251125_200219.txt
🎯 Risk Score: 45/100
🔍 Findings: 3 categories
📝 Text length: 12345 characters
🚨 Security issues detected:
   • exploits: 2 instances
   • malware: 1 instances
   • credentials: 3 instances
```

## 📊 Output Files

The tool generates detailed report files with the naming convention:
```
analysis_<domain>_<timestamp>.txt
```

### Report Structure
```
DARK WEB SITE ANALYSIS REPORT
==================================================
URL: http://example.onion
Analysis Time: 2025-11-25 20:02:19
Risk Score: 45/100
Text Length: 12345 characters

SECURITY FINDINGS:
------------------------------
EXPLOITS: CVE-2024-1234, exploit, vulnerability
CREDENTIALS: passwords, leaked data

HYPOTHESES:
--------------------
• This site may be discussing or distributing exploit tools
• Potential credential leak discussion detected

==================================================
FULL TEXT CONTENT:
==================================================
[Complete extracted text from the website]
```

## 🔍 Detected Categories

The tool scans for these security-related patterns:

| Category | Weight | Keywords |
|----------|--------|----------|
| Exploits | 10 | CVE-*, exploit, zero-day, vulnerability, RCE |
| Malware | 9 | malware, ransomware, trojan, botnet, keylogger |
| Financial Crime | 8 | carding, CVV, fullz, dump, bank login |
| Weapons | 8 | weapons, firearms, arms, ammunition |
| Fraud | 7 | fraud, scam, phishing, social engineering |
| Hacking Services | 6 | hacking service, DDoS for hire, pentesting |
| Credentials | 5 | credentials, logins, passwords, data breach |
| Drugs | 4 | drugs, substances, pharmaceutical, opioid |

## ⚙️ Configuration

### Tor Proxy Settings
Default configuration uses:
- **Host**: 127.0.0.1
- **Port**: 9050
- **Protocol**: SOCKS5h

To modify, edit the `proxies` dictionary in `website_analysis.py`:
```python
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}
```

## 🛡️ Security & Ethics

### ⚠️ Important Disclaimers

1. **Educational Purpose Only**: This tool is for cybersecurity research and educational purposes only.
2. **Legal Compliance**: Only analyze websites you have permission to access. Unauthorized access may be illegal.
3. **Tor Usage**: Be aware of your local laws regarding Tor usage and dark web access.
4. **Data Privacy**: Collected data may contain sensitive information. Handle responsibly.
5. **No Warranty**: This tool is provided as-is without any warranty.

### Best Practices

- Always use this tool in a controlled, legal environment
- Do not use for illegal activities or unauthorized access
- Respect website terms of service and robots.txt
- Be mindful of rate limiting and server load
- Secure your analysis reports appropriately

## 🐛 Troubleshooting

### Tor Connection Failed
```bash
# Check if Tor is running
lsof -i :9050

# Start Tor if not running
tor &

# Check Tor logs
tail -f /usr/local/var/log/tor.log
```

### Permission Denied (403) Error
- Ensure you have proper access to the target website
- Some sites may block automated requests
- Try adjusting User-Agent headers

### Module Not Found Errors
```bash
# Reinstall dependencies
pip install --upgrade requests beautifulsoup4 python-whois PySocks
```

### Timeout Errors
- .onion sites can be slow; increase timeout in the code
- Verify your Tor connection is stable
- The site might be offline

## 📝 Example Use Cases

1. **Cybersecurity Research**: Analyze forums discussing vulnerabilities
2. **Threat Intelligence**: Monitor dark web marketplaces for emerging threats
3. **Academic Study**: Research patterns in underground communities
4. **Security Awareness**: Understand dark web content for training purposes

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available for educational purposes. Use responsibly and ethically.

## 👤 Author

**Ahmad Mirza** (EngrAhmadofficial)
- GitHub: [@EngrAhmadofficial](https://github.com/EngrAhmadofficial)

## 🔗 Resources

- [Tor Project](https://www.torproject.org/)
- [OWASP Web Security](https://owasp.org/)
- [CVE Database](https://cve.mitre.org/)
- [Dark Web Research Ethics](https://www.darkowl.com/blog-content/ethics-of-dark-web-research)

---

**⚠️ Remember**: With great power comes great responsibility. Use this tool ethically and legally.

