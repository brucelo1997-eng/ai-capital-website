# AI Capital - Fully Automated GitHub Pages Deployment

**Status:** Ready for deployment ✅

## What's Prepared

- ✅ Website files (HTML, CSS, JS) - Complete and production-ready
- ✅ Git repository - Initialized and committed
- ✅ GitHub Actions workflow - Automatic deployment configured
- ✅ Deployment scripts - Python and Bash versions ready

## The Challenge

GitHub requires authentication to create repositories and push code. The **one-time setup** required is getting a GitHub Personal Access Token (PAT). Once you provide it, **everything else is completely automated**.

## 🚀 Quick Start (5 Minutes)

### Step 1: Get Your GitHub Token (2 minutes)

1. **Go to:** https://github.com/settings/tokens
2. **Click:** "Generate new token (classic)"
3. **Configure:**
   - Name: `ai-capital-deploy`
   - Expiration: 90 days (or longer)
   - Scopes: Check these boxes:
     - ✅ `repo` (full control of repositories)
     - ✅ `workflow` (GitHub Actions)
     - ✅ `admin:repo_hook` (manage webhooks)
4. **Click:** "Generate token"
5. **Copy:** The token to your clipboard (you won't see it again!)

### Step 2: Deploy (1 command, 30 seconds)

**Choose ONE method:**

#### Option A: Python (Recommended)
```bash
cd /Users/Bruce/.openclaw/workspace/ai-capital-website
GITHUB_TOKEN="paste_your_token_here" python3 deploy_github_pages.py
```

#### Option B: Bash
```bash
cd /Users/Bruce/.openclaw/workspace/ai-capital-website
GITHUB_TOKEN="paste_your_token_here" bash GITHUB_DEPLOY.sh
```

### Step 3: Done! 🎉

The script will:
1. ✅ Create GitHub repository: `ai-capital-website`
2. ✅ Push all files to GitHub
3. ✅ Enable GitHub Pages
4. ✅ **Print your live URL**

**Result:** Your website goes live at:
```
https://brucelo1997.github.io/ai-capital-website/
```

## What Gets Automated

Once you provide the token, these steps are **fully automatic**:

- Repository creation via GitHub API
- File pushing via Git
- GitHub Pages enablement via API
- Workflow configuration for future deployments
- Everything verified and reported back

## How It Works

### Local Setup (Already Done ✅)

```
ai-capital-website/
├── .git/                      # Git repository
├── .github/
│   └── workflows/
│       └── deploy.yml         # GitHub Actions auto-deploy
├── index.html                 # Home page
├── courses.html              # Courses
├── about.html                # About
├── faq.html                  # FAQ
├── contact.html              # Contact
├── style.css                 # Styling
├── script.js                 # Interactivity
├── deploy_github_pages.py    # Deployment script
├── GITHUB_DEPLOY.sh          # Alternative deployment
└── ...
```

### Automated Deployment Flow

```
Token provided
    ↓
GitHub API: Create repository
    ↓
Git: Push files to main branch
    ↓
GitHub API: Enable Pages
    ↓
GitHub Actions: Watches for commits
    ↓
Future pushes: Auto-deploy via Actions
    ↓
Live URL ready
```

## After Deployment

### Immediate (0 minutes)
- ✅ Website live at `https://brucelo1997.github.io/ai-capital-website/`
- ✅ All pages accessible (home, courses, about, faq, contact)
- ✅ HTTPS enabled automatically

### Custom Domain (Optional - 5 minutes)
To use **aicapital.world**:

1. **Add CNAME in your domain registrar:**
   - Name: `aicapital.world`
   - Value: `brucelo1997.github.io`

2. **Let DNS propagate** (5 minutes to 48 hours)

3. **Verify:** Visit `https://aicapital.world` - it works!

### Future Updates (Automatic)

Any time you commit new files:
```bash
cd ai-capital-website
git add .
git commit -m "Update: your changes"
git push origin main
```

**GitHub Actions automatically redeploys** - no manual steps needed!

## Troubleshooting

### Token Issues

**Error:** `Failed to authenticate with GitHub`
- Ensure token is correct and copied fully
- Token might have expired - generate a new one

**Error:** `Repository already exists`
- If repo already created, script uses it
- Token still pushes files

### Pushing Files

**Error:** `Could not read from remote repository`
- Token might be invalid
- Check internet connection

### Pages Not Showing

**Error:** `404 on https://brucelo1997.github.io/ai-capital-website/`
- Pages enabled but needs ~1 minute to build
- Refresh page
- Check GitHub Actions tab in repository

## Technical Details

### What's in the Scripts?

**deploy_github_pages.py:**
- ✅ HTTP/2 GitHub API calls
- ✅ Robust error handling
- ✅ User-friendly output
- ✅ Cross-platform (Python 3+)

**GITHUB_DEPLOY.sh:**
- ✅ Pure Bash script
- ✅ Uses curl for API calls
- ✅ Git CLI for pushing
- ✅ Great for CI/CD pipelines

Both scripts:
- ✅ Do the same thing
- ✅ Fully automated (token only input)
- ✅ Verify each step
- ✅ Report status clearly

### GitHub Actions Workflow

The `.github/workflows/deploy.yml` file:
- Watches for pushes to `main` branch
- Automatically rebuilds Pages
- Keeps pages always up-to-date
- No manual rebuild ever needed

## Security Notes

### Token Safety
- ✅ Token only used once
- ✅ Never stored in repository
- ✅ You can revoke it anytime (GitHub > Settings > Tokens)
- ✅ Consider short expiration (90 days)

### Repository Security
- ✅ Repository is public (GitHub Pages requirement)
- ✅ No sensitive data in repository
- ✅ Website files only

## File Structure After Deployment

```
GitHub: brucelo1997/ai-capital-website
├── main branch (your files)
├── gh-pages branch (auto-generated by Pages)
└── Workflows run on each commit
```

The `gh-pages` branch is created automatically and contains the published version.

## Quick Reference

| Task | Command |
|------|---------|
| Deploy | `GITHUB_TOKEN="..." python3 deploy_github_pages.py` |
| Check status | Visit `https://github.com/brucelo1997/ai-capital-website` |
| Update content | Edit HTML, commit, push - auto-deploys |
| Custom domain | Update DNS, GitHub Pages shows it |
| View live | `https://brucelo1997.github.io/ai-capital-website/` |

## Support

Each script provides detailed output showing:
- ✅ What's being done
- ✅ Confirmation of each step
- ✅ Final URLs
- ✅ Any errors with solutions

## Summary

**You need:** GitHub Personal Access Token (2 minutes to create)

**You get:**
- ✅ Live website in <1 minute
- ✅ HTTPS enabled
- ✅ Custom domain ready
- ✅ Auto-deploy on commits
- ✅ Free hosting forever
- ✅ No manual deploys needed

**Everything else is fully automated.** 🎉
