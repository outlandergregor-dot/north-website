# NORTH Website

Official website for NORTH productivity app.

## 🌐 Domain Strategy

- **Primary Domain:** yournorth.app
- **Secondary Domain:** yournorthapp.com (redirects to yournorth.app)

## 📧 Professional Email Addresses

- captain@yournorth.app - Feature requests and feedback
- support@yournorth.app - Technical support
- hello@yournorth.app - General inquiries and partnerships
- privacy@yournorth.app - Privacy concerns
- legal@yournorth.app - Legal matters

## 📁 Website Structure

```
/
├── index.html          # Landing page with features and download CTAs
├── support.html        # FAQ and contact form
├── privacy.html        # Privacy Policy (GDPR/CCPA compliant)
├── terms.html          # Terms of Service and EULA
├── styles.css          # Global styles
├── script.js           # Interactive functionality
└── assets/
    ├── favicon.png
    ├── apple-touch-icon.png
    ├── og-image.png
    ├── app-screenshot-1.png
    ├── app-store-badge.svg
    └── google-play-badge.svg
```

## 🚀 Deployment Instructions

### Option 1: Vercel (Recommended)

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy from this directory:
   ```bash
   cd /home/ubuntu/north-website
   vercel --prod
   ```

3. Add custom domain in Vercel dashboard:
   - Go to Project Settings → Domains
   - Add `yournorth.app`
   - Vercel will provide DNS records

### Option 2: Netlify

1. Install Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Deploy:
   ```bash
   cd /home/ubuntu/north-website
   netlify deploy --prod
   ```

3. Add custom domain in Netlify dashboard

### Option 3: GitHub Pages

1. Create GitHub repository
2. Push website files
3. Enable GitHub Pages in repository settings
4. Add custom domain

## 🔧 DNS Configuration

After deploying to Vercel/Netlify, configure DNS in Namecheap:

### For yournorth.app (Primary Domain)

**A Records:**
```
Type: A Record
Host: @
Value: [Vercel/Netlify IP from deployment]
TTL: Automatic
```

**CNAME Record (if using Vercel/Netlify CNAME):**
```
Type: CNAME Record
Host: @
Value: cname.vercel-dns.com (or Netlify equivalent)
TTL: Automatic
```

**WWW Redirect:**
```
Type: CNAME Record
Host: www
Value: yournorth.app
TTL: Automatic
```

### For yournorthapp.com (Redirect Domain)

**URL Redirect:**
```
Type: URL Redirect Record
Host: @
Value: https://yournorth.app
Redirect Type: Permanent (301)
```

**WWW Redirect:**
```
Type: URL Redirect Record
Host: www
Value: https://yournorth.app
Redirect Type: Permanent (301)
```

### Email Configuration

**Option 1: Email Forwarding (Simple)**
In Namecheap dashboard → Email Forwarding:
```
captain@yournorth.app → [your-personal-email]
support@yournorth.app → [your-personal-email]
hello@yournorth.app → [your-personal-email]
privacy@yournorth.app → [your-personal-email]
legal@yournorth.app → [your-personal-email]
```

**Option 2: Google Workspace / Custom Email (Professional)**
1. Sign up for Google Workspace or similar service
2. Add MX records provided by email service
3. Verify domain ownership
4. Create email accounts

## 📋 Pre-Launch Checklist

- [ ] Deploy website to Vercel/Netlify
- [ ] Configure DNS for yournorth.app
- [ ] Set up redirect from yournorthapp.com
- [ ] Configure email forwarding/hosting
- [ ] Add real app screenshots to `/assets/`
- [ ] Add App Store and Google Play download links
- [ ] Test all pages on mobile and desktop
- [ ] Verify Privacy Policy and Terms links work
- [ ] Test contact form submission
- [ ] Set up SSL certificate (automatic with Vercel/Netlify)
- [ ] Submit sitemap to Google Search Console
- [ ] Add Google Analytics (optional)

## 🎨 Assets Needed

Before launch, replace placeholder assets with real ones:

1. **App Screenshots** (1242x2688px for iPhone):
   - Home screen with 1-3-5 tasks
   - Navigator guidance screen
   - Calendar week view
   - Win Log with streak
   - Sunday Compass
   - Voice Assistant / Driving Mode

2. **Store Badges**:
   - Download official badges from Apple and Google
   - [Apple App Store Badge](https://developer.apple.com/app-store/marketing/guidelines/)
   - [Google Play Badge](https://play.google.com/intl/en_us/badges/)

3. **Favicon & Icons**:
   - 32x32px favicon.png
   - 180x180px apple-touch-icon.png
   - 1200x630px og-image.png (for social sharing)

## 🔗 App Store Submission

When submitting to App Store and Google Play, provide these URLs:

- **Privacy Policy URL:** https://yournorth.app/privacy.html
- **Terms of Service URL:** https://yournorth.app/terms.html
- **Support URL:** https://yournorth.app/support.html
- **Marketing URL:** https://yournorth.app

## 📞 Support

For website issues, contact: support@yournorth.app
