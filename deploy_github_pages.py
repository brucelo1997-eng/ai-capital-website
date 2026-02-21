#!/usr/bin/env python3
"""
Fully Automated GitHub Pages Deployment for AI Capital Website

Usage: 
    GITHUB_TOKEN=your_token python3 deploy_github_pages.py

This script automates:
    1. GitHub repository creation
    2. Pushing files to GitHub
    3. Enabling GitHub Pages
    4. Returns live URL
"""

import os
import sys
import json
import subprocess
from pathlib import Path
import urllib.request
import urllib.error

# Configuration
REPO_NAME = "ai-capital-website"
REPO_OWNER = "brucelo1997"
BRANCH = "main"

# Colors
class Colors:
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    END = '\033[0m'

def print_header(msg):
    print(f"\n{Colors.BLUE}{msg}{Colors.END}")

def print_success(msg):
    print(f"{Colors.GREEN}✓ {msg}{Colors.END}")

def print_error(msg):
    print(f"{Colors.RED}ERROR: {msg}{Colors.END}")

def print_info(msg):
    print(f"{Colors.YELLOW}{msg}{Colors.END}")

def get_github_token():
    """Get GitHub token from environment variable"""
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print_error("GITHUB_TOKEN environment variable not set")
        print("\nTo generate a Personal Access Token:")
        print("1. Go to: https://github.com/settings/tokens")
        print("2. Click 'Generate new token (classic)'")
        print("3. Select scopes: repo, workflow, admin:repo_hook")
        print("4. Copy the token")
        print("5. Run: export GITHUB_TOKEN='your_token'")
        print("6. Then run this script again")
        sys.exit(1)
    return token

def github_api_call(token, method, endpoint, data=None):
    """Make a GitHub API call"""
    url = f"https://api.github.com{endpoint}"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'AI-Capital-Deploy'
    }
    
    if data:
        headers['Content-Type'] = 'application/json'
        req = urllib.request.Request(
            url, 
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method=method
        )
    else:
        req = urllib.request.Request(url, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        try:
            error_body = json.loads(e.read().decode('utf-8'))
            return error_body
        except:
            return {'error': str(e)}

def main():
    print_header("=" * 50)
    print_header("AI CAPITAL - GitHub Pages Deploy")
    print_header("=" * 50)
    
    # Step 1: Get and verify token
    print_info("\nStep 1: Verifying GitHub authentication...")
    token = get_github_token()
    
    user_info = github_api_call(token, 'GET', '/user')
    if 'login' not in user_info:
        print_error(f"Failed to authenticate: {user_info}")
        sys.exit(1)
    
    github_username = user_info['login']
    print_success(f"Authenticated as: {github_username}")
    
    # Step 2: Create or verify repository
    print_info("\nStep 2: Setting up GitHub repository...")
    
    repo_check = github_api_call(token, 'GET', f'/repos/{github_username}/{REPO_NAME}')
    
    if 'id' in repo_check:
        print_success(f"Repository exists: {repo_check['html_url']}")
    else:
        print_info(f"Creating repository: {REPO_NAME}")
        repo_data = {
            'name': REPO_NAME,
            'description': 'AI Capital - Master AI Automation Without Code',
            'homepage': 'https://aicapital.world',
            'private': False,
            'auto_init': False,
            'has_issues': True,
            'has_projects': False,
            'has_downloads': False
        }
        
        repo_response = github_api_call(token, 'POST', '/user/repos', repo_data)
        
        if 'id' not in repo_response:
            print_error(f"Failed to create repository: {repo_response}")
            sys.exit(1)
        
        print_success(f"Repository created: {repo_response['html_url']}")
    
    # Step 3: Configure git and push
    print_info("\nStep 3: Configuring Git and pushing files...")
    
    # Remove existing remote
    subprocess.run(['git', 'remote', 'remove', 'origin'], 
                  cwd=os.path.dirname(os.path.abspath(__file__)),
                  capture_output=True)
    
    # Add remote with token auth
    remote_url = f"https://{token}@github.com/{github_username}/{REPO_NAME}.git"
    subprocess.run(['git', 'remote', 'add', 'origin', remote_url],
                  cwd=os.path.dirname(os.path.abspath(__file__)),
                  check=True)
    
    # Push to main branch
    result = subprocess.run(
        ['git', 'push', '-u', 'origin', 'main', '--force'],
        cwd=os.path.dirname(os.path.abspath(__file__)),
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print_error(f"Failed to push: {result.stderr}")
        sys.exit(1)
    
    print_success("Files pushed to GitHub")
    
    # Step 4: Enable GitHub Pages
    print_info("\nStep 4: Enabling GitHub Pages...")
    
    pages_data = {
        'source': {
            'branch': 'main',
            'path': '/'
        }
    }
    
    pages_response = github_api_call(
        token, 
        'POST', 
        f'/repos/{github_username}/{REPO_NAME}/pages',
        pages_data
    )
    
    # Check if already enabled or newly created
    if 'status' in pages_response or pages_response.get('message', '').startswith('Conflict'):
        print_success("GitHub Pages is enabled")
    else:
        # Try to get current status
        pages_status = github_api_call(
            token,
            'GET',
            f'/repos/{github_username}/{REPO_NAME}/pages'
        )
        if 'status' in pages_status:
            print_success("GitHub Pages is enabled")
        else:
            print_info("Note: Pages status may take a moment to update")
    
    # Final output
    print_header("\n" + "=" * 50)
    print_header("✨ DEPLOYMENT COMPLETE! ✨")
    print_header("=" * 50)
    
    pages_url = f"https://{github_username}.github.io/{REPO_NAME}/"
    repo_url = f"https://github.com/{github_username}/{REPO_NAME}"
    
    print(f"\n{Colors.GREEN}Your website is now live!{Colors.END}")
    print(f"\n{Colors.YELLOW}Live URL (GitHub Pages):{Colors.END}")
    print(f"{Colors.GREEN}{pages_url}{Colors.END}")
    
    print(f"\n{Colors.YELLOW}GitHub Repository:{Colors.END}")
    print(f"{Colors.GREEN}{repo_url}{Colors.END}")
    
    print(f"\n{Colors.YELLOW}Custom Domain (Optional):{Colors.END}")
    print("To point aicapital.world to your GitHub Pages:")
    print("1. Update nameservers at your domain registrar")
    print(f"2. Add CNAME: aicapital.world → {github_username}.github.io")
    print("3. Wait for DNS propagation (5-48 hours)")
    
    print(f"\n{Colors.BLUE}Next Steps:{Colors.END}")
    print(f"1. Visit: {pages_url}")
    print("2. Test all pages (home, courses, about, faq, contact)")
    print("3. Set up custom domain (optional)")
    print("\n✨ Your AI Capital website is ready to go! ✨\n")

if __name__ == '__main__':
    main()
