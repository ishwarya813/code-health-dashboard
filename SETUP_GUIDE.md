# 🚀 Quick Setup Guide for GitHub Pages

## Status Check ✅

- ✓ Repository folder created: `code-health-dashboard`
- ✓ Git initialized
- ✓ Dashboard copied as `index.html`
- ✓ GitHub Actions workflow created
- ✓ Python automation scripts created
- ✓ README and documentation added

---

## 📋 Next Steps

### Step 1: Update Remote URL

Replace `YOUR_USERNAME` with your actual GitHub username:

```powershell
cd "C:\Users\IshwaryaKannan\OneDrive - Atmosera\Desktop\code-health-dashboard"
git remote set-url origin https://github.com/YOUR_USERNAME/code-health-dashboard.git
```

### Step 2: Initial Commit and Push

```powershell
git add .
git commit -m "Initial commit: Add code health dashboard with automation"
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your GitHub repository: `https://github.com/YOUR_USERNAME/code-health-dashboard`
2. Click **Settings** tab
3. Scroll down to **Pages** section (left sidebar)
4. Under **Source**:
   - Branch: Select `main`
   - Folder: Select `/ (root)`
   - Click **Save**
5. Wait 1-2 minutes for deployment
6. Your dashboard will be live at: `https://YOUR_USERNAME.github.io/code-health-dashboard/`

### Step 4: Configure GitHub Actions Permissions

1. In your repo, go to **Settings** → **Actions** → **General**
2. Scroll to **Workflow permissions**
3. Select **Read and write permissions**
4. Check ✓ **Allow GitHub Actions to create and approve pull requests**
5. Click **Save**

### Step 5: Test the Automation

Option A - Wait for Monday 9 AM UTC (automatic run)

Option B - Manual trigger (immediate):
1. Go to **Actions** tab in GitHub
2. Click **Update Code Health Dashboard** workflow
3. Click **Run workflow** → **Run workflow** button
4. Watch it execute (takes ~1-2 minutes)

---

## 🔧 Customization

### Change Schedule

Edit `.github/workflows/update-dashboard.yml`:

```yaml
on:
  schedule:
    # Change this cron expression
    # Currently: Every Monday at 9 AM UTC
    - cron: '0 9 * * 1'
    
    # Examples:
    # Daily at 8 AM UTC: '0 8 * * *'
    # Every 6 hours: '0 */6 * * *'
    # Wed & Fri at 10 AM: '0 10 * * 3,5'
```

### Analyze Your Own Code

Edit `scripts/analyze_metrics.py` to point to your codebase:

```python
def analyze_complexity():
    # Clone your source repo
    import subprocess
    subprocess.run(['git', 'clone', 'https://github.com/YOUR_ORG/your-repo.git', 'source'])
    
    # Run radon analysis
    from radon.complexity import cc_visit
    # ... analyze code
```

---

## 📊 File Structure

```
code-health-dashboard/
├── index.html                          # Your dashboard (auto-updated)
├── README.md                           # Documentation
├── .gitignore                          # Git ignore rules
├── .github/
│   └── workflows/
│       └── update-dashboard.yml        # GitHub Actions workflow
└── scripts/
    ├── analyze_metrics.py              # Collects code metrics
    └── update_dashboard.py             # Updates dashboard HTML
```

---

## 🎯 How It Works

1. **Every Monday at 9 AM UTC**, GitHub Actions triggers
2. **Python scripts analyze** your code metrics:
   - Cyclomatic complexity (using radon)
   - Test coverage (using pytest-cov)
   - Code churn (using git log)
3. **Dashboard is updated** with fresh data
4. **Changes are committed** automatically
5. **GitHub Pages deploys** the updated dashboard

---

## 🔍 Troubleshooting

### Dashboard not updating?

1. Check **Actions** tab for workflow run status
2. Click on failed run to see error logs
3. Verify write permissions are enabled

### Metrics not accurate?

- Modify `scripts/analyze_metrics.py` for your specific codebase
- Test locally first: `python scripts/analyze_metrics.py`

### Page not loading?

- Verify GitHub Pages is enabled in Settings
- Check that `index.html` exists in the repo
- Wait 1-2 minutes after first push

---

## 📞 Need Help?

Check the workflow logs:
1. Go to **Actions** tab
2. Click on the latest workflow run
3. Expand the steps to see detailed logs

---

## ✅ Verification Checklist

Before pushing, verify:
- [ ] Updated remote URL with correct username
- [ ] All files are present (check with `ls` or `Get-ChildItem`)
- [ ] `.github/workflows/update-dashboard.yml` exists
- [ ] `scripts/` folder has both Python files
- [ ] `index.html` has the dashboard content

Ready to push? Run the commands in Step 2!
