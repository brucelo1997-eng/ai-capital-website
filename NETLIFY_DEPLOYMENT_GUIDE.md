# AI Capital Website - Netlify Deployment Guide

## ⚡ Quick Deploy (5 Minutes)

This guide will walk you through deploying your AI Capital website to Netlify and pointing your custom domain (aicapital.world) in less than 5 minutes.

---

## Step 1: Prepare Your Files (30 seconds)

Your website files are already organized and ready:
- `index.html` - Home page
- `courses.html` - Courses page
- `about.html` - About page
- `faq.html` - FAQ page
- `contact.html` - Contact page
- `style.css` - All styling
- `script.js` - Interactive features

**No changes needed.** These files are production-ready!

---

## Step 2: Create a Netlify Account (1 minute)

1. Go to [netlify.com](https://netlify.com)
2. Click **"Sign up"** (top right)
3. Choose **"Sign up with GitHub"** or use email
4. Complete the signup process

**Pro tip:** Using GitHub makes future deploys even easier with automatic updates.

---

## Step 3: Deploy to Netlify (1 minute)

### Option A: Drag & Drop Deploy (Easiest)

1. Go to [netlify.com](https://netlify.com) and log in
2. Look for **"Want to deploy a new site without connecting to Git? Drag and drop your site folder here"**
3. Select the entire `ai-capital-website` folder containing all 5 HTML files and the CSS/JS files
4. Netlify will automatically generate a temporary domain
5. ✅ **Your site is live!**

### Option B: GitHub Deploy (Recommended for Updates)

1. Create a new GitHub repository
2. Push your `ai-capital-website` folder to GitHub
3. Go to [netlify.com](https://netlify.com) and click **"New site from Git"**
4. Connect your GitHub account
5. Select your repository
6. Click **"Deploy"**
7. ✅ **Your site is live, and future pushes to GitHub auto-deploy!**

---

## Step 4: Point Your Custom Domain (2 minutes)

### If You Own aicapital.world Already:

1. In Netlify dashboard, go to your deployed site
2. Click **"Domain settings"**
3. Click **"Add domain"**
4. Enter: `aicapital.world`
5. Netlify will show you nameserver details
6. Go to your domain registrar (GoDaddy, Namecheap, etc.)
7. Update your nameservers to Netlify's nameservers:
   - `dns1.p01.nsone.net`
   - `dns2.p01.nsone.net`
   - `dns3.p01.nsone.net`
   - `dns4.p01.nsone.net`
8. Wait 24-48 hours for DNS propagation (usually 5-10 minutes)
9. ✅ **aicapital.world now points to your site!**

### If You Need to Buy aicapital.world:

1. Go to a domain registrar (GoDaddy, Namecheap, Google Domains)
2. Search for and buy `aicapital.world`
3. Follow the steps above to point to Netlify

---

## Step 5: Enable HTTPS (30 seconds - Automatic!)

Netlify automatically provides free SSL/HTTPS certificates. Your site will automatically be HTTPS-enabled.

✅ **Done!** Your site is secure and ready for production.

---

## Verification Checklist

- [ ] Netlify account created
- [ ] Website deployed (you have a Netlify URL)
- [ ] Custom domain pointing to Netlify
- [ ] DNS has propagated (test at [whatsmydns.net](https://www.whatsmydns.net/))
- [ ] aicapital.world loads in browser
- [ ] All 5 pages load correctly
- [ ] Mobile design looks good on phone
- [ ] Links between pages work
- [ ] Buttons link to correct URLs

---

## Testing Your Site

### Quick Tests:

1. **Homepage**: aicapital.world
2. **Courses Page**: aicapital.world/courses.html
3. **About Page**: aicapital.world/about.html
4. **FAQ Page**: aicapital.world/faq.html (click to expand answers)
5. **Contact Page**: aicapital.world/contact.html (test form)

### Mobile Responsive Check:

1. Open your site on a phone
2. Test navigation menu
3. Verify cards and buttons display properly
4. Check text readability

### Interactive Features:

1. **FAQ accordion** - Click questions to expand/collapse answers
2. **Contact form** - Fill out and submit (you'll get a success message)
3. **Navigation** - Click menu items to navigate between pages
4. **External links** - "Enroll Now" buttons link to Teachable courses

---

## What's Included

### Design Features:
- ✅ Professional, modern design
- ✅ Light theme with blue branding (#0066cc)
- ✅ Fully mobile responsive
- ✅ Consistent navigation across all pages
- ✅ Interactive elements (FAQ accordion, forms)

### Pages:
- ✅ **Home** - Hero section with featured course
- ✅ **Courses** - All 3 course offerings with descriptions
- ✅ **About** - Mission, teaching approach, core values
- ✅ **FAQ** - 8 accordion Q&A items
- ✅ **Contact** - Email form + newsletter signup

### Performance:
- ✅ No external CDN dependencies (self-contained)
- ✅ Fast loading (all CSS/JS included)
- ✅ Optimized for mobile
- ✅ Ready for production

---

## Troubleshooting

### Site Shows 404 on Custom Domain
- **Wait 24-48 hours** for DNS to propagate
- Check DNS settings in domain registrar
- Verify nameservers match Netlify's values

### Pages Don't Load (e.g., /courses.html shows 404)
- Go to Netlify **Build settings**
- In **Publish directory**, make sure it's blank or points to the root folder
- Re-deploy if needed

### Mobile Design Looks Off
- This site is fully responsive
- Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
- Test in incognito/private mode

### Contact Form Not Working
- Forms require backend setup
- For now, it provides user feedback and validates input
- To actually receive emails, connect Netlify Forms or use third-party service

---

## Next Steps (Optional Enhancements)

Once your site is live, you can:

1. **Connect a form backend** - Use Netlify Forms (free tier available) to receive contact submissions
2. **Add analytics** - Track visitors and behavior
3. **Enable auto-deployment** - Push changes to GitHub, auto-deploy to Netlify
4. **Add email notifications** - Get alerted when someone submits a form

---

## Support & Resources

- **Netlify Documentation**: [docs.netlify.com](https://docs.netlify.com)
- **Netlify Community**: [community.netlify.com](https://community.netlify.com)
- **Domain Help**: Contact your domain registrar's support

---

## Timeline

- **5 minutes**: Full deployment with custom domain
- **24-48 hours**: Full DNS propagation (usually faster)
- **Result**: Your AI Capital website live at aicapital.world

---

## Your Site is Production-Ready! 🎉

No additional configuration needed. Just deploy and go live.

**Happy launching!**
