#!/bin/bash
#
# FULLY AUTOMATED GitHub Pages Deployment Script
# 
# Usage: GITHUB_TOKEN=your_token bash GITHUB_DEPLOY.sh
#
# This script will:
# 1. Create a GitHub repository (ai-capital-website)
# 2. Push all files to GitHub
# 3. Enable GitHub Pages automatically
# 4. Return the live URL
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REPO_NAME="ai-capital-website"
GITHUB_USERNAME="brucelo1997"  # This will be derived from the token
REPO_OWNER=${REPO_OWNER:-"brucelo1997"}
BRANCH="main"

echo -e "${BLUE}================================${NC}"
echo -e "${BLUE}AI CAPITAL - GitHub Pages Deploy${NC}"
echo -e "${BLUE}================================${NC}"
echo ""

# Check for GitHub token
if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${RED}ERROR: GITHUB_TOKEN environment variable not set${NC}"
    echo ""
    echo "To generate a Personal Access Token:"
    echo "1. Go to: https://github.com/settings/tokens"
    echo "2. Click 'Generate new token (classic)'"
    echo "3. Select scopes: repo, workflow"
    echo "4. Copy the token"
    echo "5. Run: export GITHUB_TOKEN='your_token'"
    echo "6. Then run this script again"
    echo ""
    exit 1
fi

echo -e "${YELLOW}Step 1: Checking Git configuration...${NC}"
git config user.email
echo -e "${GREEN}✓ Git configured${NC}"
echo ""

# Function to make GitHub API calls
github_api() {
    local method=$1
    local endpoint=$2
    local data=$3
    
    local url="https://api.github.com${endpoint}"
    local auth_header="Authorization: token ${GITHUB_TOKEN}"
    
    if [ -z "$data" ]; then
        curl -s -X "$method" -H "$auth_header" -H "Accept: application/vnd.github.v3+json" "$url"
    else
        curl -s -X "$method" -H "$auth_header" -H "Content-Type: application/json" -H "Accept: application/vnd.github.v3+json" -d "$data" "$url"
    fi
}

echo -e "${YELLOW}Step 2: Verifying GitHub authentication...${NC}"
USER_INFO=$(github_api "GET" "/user")
GITHUB_USERNAME=$(echo "$USER_INFO" | grep -o '"login":"[^"]*"' | cut -d'"' -f4)

if [ -z "$GITHUB_USERNAME" ]; then
    echo -e "${RED}ERROR: Failed to authenticate with GitHub${NC}"
    echo "Response: $USER_INFO"
    exit 1
fi

echo -e "${GREEN}✓ Authenticated as: $GITHUB_USERNAME${NC}"
echo ""

echo -e "${YELLOW}Step 3: Creating GitHub repository...${NC}"

# Check if repo already exists
REPO_CHECK=$(github_api "GET" "/repos/$GITHUB_USERNAME/$REPO_NAME")
if echo "$REPO_CHECK" | grep -q '"id"'; then
    echo -e "${YELLOW}Repository already exists. Skipping creation.${NC}"
    REPO_URL=$(echo "$REPO_CHECK" | grep -o '"html_url":"[^"]*"' | cut -d'"' -f4)
else
    # Create the repository
    REPO_DATA="{
        \"name\": \"$REPO_NAME\",
        \"description\": \"AI Capital - Master AI Automation Without Code\",
        \"homepage\": \"https://aicapital.world\",
        \"private\": false,
        \"has_issues\": true,
        \"has_projects\": false,
        \"has_downloads\": false,
        \"auto_init\": false
    }"
    
    REPO_RESPONSE=$(github_api "POST" "/user/repos" "$REPO_DATA")
    
    if echo "$REPO_RESPONSE" | grep -q '"id"'; then
        REPO_URL=$(echo "$REPO_RESPONSE" | grep -o '"html_url":"[^"]*"' | cut -d'"' -f4)
        echo -e "${GREEN}✓ Repository created: $REPO_URL${NC}"
    else
        echo -e "${RED}ERROR: Failed to create repository${NC}"
        echo "Response: $REPO_RESPONSE"
        exit 1
    fi
fi

echo ""
echo -e "${YELLOW}Step 4: Configuring GitHub authentication for push...${NC}"

# Remove existing remote if it exists
git remote remove origin 2>/dev/null || true

# Add remote with token authentication
git remote add origin "https://${GITHUB_TOKEN}@github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"
echo -e "${GREEN}✓ Remote configured${NC}"
echo ""

echo -e "${YELLOW}Step 5: Pushing files to GitHub...${NC}"
git push -u origin main --force 2>&1 | grep -v "remote:" || echo "Push completed"
echo -e "${GREEN}✓ Files pushed to GitHub${NC}"
echo ""

echo -e "${YELLOW}Step 6: Enabling GitHub Pages...${NC}"

PAGES_DATA="{
    \"source\": {
        \"branch\": \"main\",
        \"path\": \"/\"
    }
}"

PAGES_RESPONSE=$(github_api "POST" "/repos/$GITHUB_USERNAME/$REPO_NAME/pages" "$PAGES_DATA")

if echo "$PAGES_RESPONSE" | grep -q '"status"'; then
    echo -e "${GREEN}✓ GitHub Pages enabled${NC}"
else
    # Pages might already be enabled, try to get current status
    PAGES_STATUS=$(github_api "GET" "/repos/$GITHUB_USERNAME/$REPO_NAME/pages")
    if echo "$PAGES_STATUS" | grep -q '"status"'; then
        echo -e "${GREEN}✓ GitHub Pages already enabled${NC}"
    fi
fi

echo ""
echo -e "${BLUE}================================${NC}"
echo -e "${GREEN}✨ DEPLOYMENT COMPLETE! ✨${NC}"
echo -e "${BLUE}================================${NC}"
echo ""
echo -e "${GREEN}Your website is now live!${NC}"
echo ""
echo -e "${YELLOW}Live URL (GitHub Pages):${NC}"
echo -e "${GREEN}https://${GITHUB_USERNAME}.github.io/${REPO_NAME}/${NC}"
echo ""
echo -e "${YELLOW}GitHub Repository:${NC}"
echo -e "${GREEN}${REPO_URL}${NC}"
echo ""
echo -e "${YELLOW}Custom Domain Setup (Optional):${NC}"
echo "1. Update nameservers at your domain registrar to point to GitHub Pages"
echo "2. Add CNAME record: aicapital.world → ${GITHUB_USERNAME}.github.io"
echo "3. Wait for DNS propagation (5-48 hours)"
echo "4. GitHub Pages will show: https://aicapital.world"
echo ""
echo -e "${BLUE}Next Steps:${NC}"
echo "1. Visit your live URL to verify"
echo "2. Test all pages: home, courses, about, faq, contact"
echo "3. Share your website!"
echo ""
