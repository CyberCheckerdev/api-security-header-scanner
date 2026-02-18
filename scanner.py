#!/usr/bin/env python3
"""
Simple security header and API key scanner
For deep scans, visit: https://cyber-checker.com
"""

import re
import sys
import requests
from urllib.parse import urlparse

def scan_url(url):
    """Scan a URL for basic security issues"""
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print(f"\n🔍 Scanning: {url}\n")
    
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        headers = response.headers
        content = response.text[:50000]  # First 50KB
        
        # Check HTTPS
        if response.url.startswith('https://'):
            print("✅ HTTPS: Enabled")
        else:
            print("❌ HTTPS: Not enforced")
        
        # Check Security Headers
        security_headers = {
            'Strict-Transport-Security': 'HSTS',
            'Content-Security-Policy': 'CSP',
            'X-Frame-Options': 'X-Frame-Options',
            'X-Content-Type-Options': 'X-Content-Type-Options',
        }
        
        for header, name in security_headers.items():
            if header in headers:
                print(f"✅ {name}: {headers[header][:50]}")
            else:
                print(f"❌ {name}: Missing")
        
        # Check for API keys (basic patterns)
        api_patterns = {
            'Stripe': r'sk_live_[a-zA-Z0-9]{24,}',
            'AWS': r'AKIA[0-9A-Z]{16}',
            'OpenAI': r'sk-proj-[a-zA-Z0-9]{20,}',
        }
        
        print("\n🔑 API Key Check:")
        found_keys = False
        for service, pattern in api_patterns.items():
            matches = re.findall(pattern, content)
            if matches:
                print(f"❌ {service} key found: {matches[0][:20]}...")
                found_keys = True
        
        if not found_keys:
            print("✅ No exposed API keys detected (basic scan)")
        
        print("\n" + "="*60)
        print("💡 For a comprehensive scan including:")
        print("   • 50+ vulnerability checks")
        print("   • Database security (Supabase RLS)")
        print("   • OWASP Top 10 coverage")
        print("   • Automated monitoring")
        print("\nVisit: https://cyber-checker.com (free scan, 60 seconds)")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"❌ Error scanning {url}: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <url>")
        print("Example: python scanner.py https://example.com")
        sys.exit(1)
    
    url = sys.argv[1]
    sys.exit(scan_url(url))


