import requests
from bs4 import BeautifulSoup
import ssl
import whois
from urllib.parse import urlparse
import re
import datetime
import os
import subprocess

def check_tor_connection():
    """Check if Tor is properly configured and running"""
    try:
        # Use a reliable Tor check service
        response = requests.get(
            'https://check.torproject.org/api/ip',  # API endpoint
            proxies={'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'},
            timeout=10
        )
        data = response.json()
        return data.get('IsTor', False)
    except:
        # Fallback check
        try:
            response = requests.get(
                'http://ifconfig.me/ip',
                proxies={'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'},
                timeout=10
            )
            # If we get an IP response through Tor, it's working
            return bool(response.text.strip())
        except:
            return False

def analyze_website(url):
    try:
        # Parse URL to get domain
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        # Configure proxies for Tor
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }

        # Enhanced headers for better compatibility
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

        print(f"Connecting to: {url}")
        print(f"Using Tor proxy: socks5h://127.0.0.1:9050")

        # Fetch the webpage
        response = requests.get(url, proxies=proxies, headers=headers, timeout=60)
        response.raise_for_status()

        print(" Successfully fetched webpage")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        all_text = soup.get_text(separator=' ', strip=True)

        # Enhanced security analysis
        security_patterns = {
            'exploits': r'\b(CVE-\d{4}-\d+|exploit|zero-?day|vulnerability|remote code execution)\b',
            'malware': r'\b(malware|ransomware|trojan|botnet|keylogger|spyware)\b',
            'financial_crime': r'\b(carding|cvv|fullz|dump|bank\s+login|credit\s+card)\b',
            'hacking_services': r'\b(hack(ing)?\s+service|DDoS\s+for\s+hire|penetration\s+testing)\b',
            'credentials': r'\b(credentials|logins|passwords?|leaked\s+data|data\s+breach)\b',
            'drugs_related': r'\b(drugs|substances|pharmaceutical|opioid)\b',
            'weapons': r'\b(weapons|firearms|arms|ammunition)\b',
            'fraud': r'\b(fraud|scam|phishing|social\s+engineering)\b'
        }

        findings = {}
        for category, pattern in security_patterns.items():
            matches = re.findall(pattern, all_text, re.IGNORECASE)
            if matches:
                findings[category] = list(set(matches))

        # Calculate risk score
        risk_weights = {
            'exploits': 10, 'malware': 9, 'financial_crime': 8,
            'weapons': 8, 'fraud': 7, 'hacking_services': 6,
            'credentials': 5, 'drugs_related': 4
        }

        risk_score = sum(risk_weights.get(cat, 0) * len(items) for cat, items in findings.items())
        risk_score = min(risk_score, 100)

        # Generate hypotheses
        hypotheses = []
        if 'exploits' in findings:
            hypotheses.append("This site may be discussing or distributing exploit tools")
        if 'malware' in findings:
            hypotheses.append("Potential malware distribution or discussion detected")
        if risk_score > 70:
            hypotheses.append("HIGH RISK: Multiple security threats detected")
        if not findings:
            hypotheses.append("No obvious security threats detected in text content")

        # Save results to file
        safe_domain = domain.replace('.', '_')
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"analysis_{safe_domain}_{timestamp}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("DARK WEB SITE ANALYSIS REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"URL: {url}\n")
            f.write(f"Analysis Time: {datetime.datetime.now()}\n")
            f.write(f"Risk Score: {risk_score}/100\n")
            f.write(f"Text Length: {len(all_text)} characters\n\n")

            f.write("SECURITY FINDINGS:\n")
            f.write("-" * 30 + "\n")
            for category, items in findings.items():
                f.write(f"{category.upper()}: {', '.join(items)}\n")

            f.write("\nHYPOTHESES:\n")
            f.write("-" * 20 + "\n")
            for hypo in hypotheses:
                f.write(f"• {hypo}\n")

            f.write("\n" + "=" * 50 + "\n")
            f.write("FULL TEXT CONTENT:\n")
            f.write("=" * 50 + "\n")
            f.write(all_text)

        # Print summary
        print(f"\n ANALYSIS COMPLETE!")
        print(f" Report saved to: {filename}")
        print(f" Risk Score: {risk_score}/100")
        print(f" Findings: {len(findings)} categories")
        print(f" Text length: {len(all_text)} characters")

        if findings:
            print(f" Security issues detected:")
            for category, items in findings.items():
                print(f"   • {category}: {len(items)} instances")
        else:
            print(" No security issues detected")

        print(f" Hypotheses: {hypotheses[0] if hypotheses else 'None'}")

        return filename

    except requests.exceptions.RequestException as e:
        print(f" Network error: {e}")
        return None
    except Exception as e:
        print(f" Analysis error: {e}")
        return None

def main():
    print(" DARK WEB ANALYSIS TOOL")
    print("=" * 50)

    # Check Tor connection
    print(" Checking Tor connection...")
    if check_tor_connection():
        print(" Tor is working correctly!")
    else:
        print(" Tor connection failed. Please ensure Tor is running:")
        print("   tor &")
        return

    # Get URL from user
    print("\n💡 Try these test URLs:")
    print("   • http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion")  # DuckDuckGo
    print("   • http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/")  # Hidden Wiki

    url = input("\nEnter website URL: ").strip()

    if not url:
        print(" Please enter a valid URL")
        return

    # Analyze the website
    print(f"\n Starting analysis of: {url}")
    result = analyze_website(url)

    if result:
        print(f"\n Analysis completed successfully!")
        print(f" Check the detailed report in: {result}")
    else:
        print("\n Analysis failed. The site may be offline or inaccessible.")

if __name__ == "__main__":
    main()