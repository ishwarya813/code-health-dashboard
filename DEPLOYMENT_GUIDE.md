# 🚀 GitHub Pages Deployment Guide

## ✅ Repository Status
- **Repository**: code-health-dashboard (already cloned)
- **GitHub URL**: https://github.com/ishwarya813/code-health-dashboard

## 📋 Step-by-Step Setup

### Step 1: Push All Files to GitHub

Run these commands to push everything to your repository:

```bash
cd c:\Users\IshwaryaKannan\Downloads\code_health_file

# Add all new files
git add .

# Commit changes
git commit -m "🚀 Add automated dashboard with GitHub Actions"

# Push to GitHub
git push origin main
```

### Step 2: Enable GitHub Pages

1. Go to: **https://github.com/ishwarya813/code-health-dashboard/settings/pages**

2. Under **"Source"**:
   - Select: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)**
   - Click **Save**

3. Wait 1-2 minutes for deployment

4. Your dashboard will be live at:
   **https://ishwarya813.github.io/code-health-dashboard/**

### Step 3: Verify GitHub Actions

1. Go to: **https://github.com/ishwarya813/code-health-dashboard/actions**

2. You should see the workflow run triggered by your push

3. Click on the workflow to see the execution logs

### Step 4: Test Manual Update (Optional)

1. Go to **Actions** tab
2. Click **Update Code Health Dashboard** workflow
3. Click **Run workflow** → Select **main** branch → Click **Run workflow**
4. Watch it execute and update your dashboard

---

## 🤖 GitHub Actions Workflow Details

### Automation Schedule

**File**: `.github/workflows/update-dashboard.yml`

```yaml
# Runs every Monday at 9 AM UTC
schedule:
  - cron: '0 9 * * 1'

# Also runs on:
# - Manual trigger (workflow_dispatch)
# - Push to main branch (when Python files change)
```

### What It Does

1. **Checks out code** from your repository
2. **Sets up Python** environment (3.11)
3. **Installs dependencies** (radon, gitpython)
4. **Runs analysis** (`scripts/analyze_code_health.py`)
   - Calculates cyclomatic complexity
   - Tracks function/method metrics
   - Analyzes git commit history
5. **Updates dashboard** (`scripts/update_dashboard.py`)
   - Updates `index.html` with new metrics
   - Updates timestamp
   - Updates charts and tables
6. **Commits changes** back to repository
7. **Pushes to GitHub** (triggers Pages deployment)

### Permissions

The workflow has `contents: write` permission to commit changes back to the repo.

---

## 📊 Tracked Metrics

### 1. Cyclomatic Complexity Trend
- **Source**: AST analysis of Python files
- **Calculation**: Average complexity across all functions
- **Display**: 4-week line chart
- **Updates**: Every workflow run

### 2. Test Coverage by Module
- **Source**: Currently simulated (configure with actual coverage tools)
- **Display**: Horizontal bar chart
- **Color coding**:
  - 🟢 Green: > 70% (healthy)
  - 🟡 Yellow: 40-70% (watch)
  - 🔴 Red: < 40% (action needed)

### 3. Code Churn Hotspots
- **Source**: Git log analysis (last 30 days)
- **Calculation**: Count of commits touching each file
- **Display**: Table with top files
- **Updates**: Based on actual git history

### 4. This Sprint's Win
- **Source**: Comparison of complexity trends
- **Display**: Highlighted success section
- **Updates**: When complexity improves

---

## 🔧 Customization

### Change Update Frequency

Edit `.github/workflows/update-dashboard.yml`:

```yaml
schedule:
  # Daily at 9 AM UTC
  - cron: '0 9 * * *'
  
  # Monday and Friday at 9 AM UTC
  - cron: '0 9 * * 1,5'
  
  # Every 6 hours
  - cron: '0 */6 * * *'
```

### Add Real Test Coverage

Replace simulation in `scripts/analyze_code_health.py`:

```python
def get_real_test_coverage() -> Dict[str, int]:
    """Parse actual coverage report"""
    import xml.etree.ElementTree as ET
    
    tree = ET.parse('coverage.xml')
    root = tree.getroot()
    
    coverage = {}
    for package in root.findall('.//package'):
        for class_elem in package.findall('class'):
            filename = class_elem.get('filename')
            line_rate = float(class_elem.get('line-rate'))
            coverage[filename] = int(line_rate * 100)
    
    return coverage
```

### Modify Dashboard Styling

Edit `index.html` to change:
- Colors
- Chart types
- Layout
- Thresholds

---

## 📁 File Structure

```
code-health-dashboard/
├── index.html                    # 🎨 Main dashboard (auto-updated)
├── metrics.json                  # 📊 Generated metrics (auto-created)
├── README.md                     # 📖 Project documentation
├── DEPLOYMENT_GUIDE.md          # 📋 This file
├── python/                       # 🐍 Code to analyze
│   ├── customer_servlet.py
│   ├── invoice_dao.py
│   └── payment_processor.py
├── scripts/                      # 🤖 Automation scripts
│   ├── analyze_code_health.py   # Analyzes code metrics
│   └── update_dashboard.py      # Updates HTML dashboard
└── .github/
    └── workflows/
        └── update-dashboard.yml  # ⚙️ GitHub Actions workflow
```

---

## 🐛 Troubleshooting

### Dashboard Not Updating

**Problem**: Dashboard shows old data

**Solutions**:
1. Check Actions tab - is workflow running?
2. Check workflow logs for errors
3. Verify GitHub Pages is enabled
4. Clear browser cache (Ctrl+F5)

### Workflow Failing

**Problem**: GitHub Actions workflow shows errors

**Solutions**:
1. Check Python file syntax errors
2. Verify scripts/ directory exists
3. Check repository permissions
4. Review workflow logs for specific error

### Pages Not Loading

**Problem**: 404 error on GitHub Pages URL

**Solutions**:
1. Wait 2-3 minutes after enabling Pages
2. Check Settings → Pages shows green checkmark
3. Verify `index.html` exists in root
4. Check branch name is correct (main)

### Metrics Look Wrong

**Problem**: Charts show unexpected data

**Solutions**:
1. Run scripts locally: `python scripts/analyze_code_health.py`
2. Check `metrics.json` file contents
3. Verify Python files are in `python/` directory
4. Check git history exists for churn analysis

---

## 🎯 Next Steps

1. ✅ Push files to GitHub
2. ✅ Enable GitHub Pages
3. ✅ Wait for first automated run (or trigger manually)
4. ✅ Share dashboard URL with team
5. 🎉 Watch it update automatically every Monday!

---

## 📞 Quick Commands Reference

```bash
# Local testing
python scripts/analyze_code_health.py
python scripts/update_dashboard.py

# Git operations
git add .
git commit -m "Update dashboard"
git push origin main

# View local dashboard
start index.html  # Windows
open index.html   # Mac
xdg-open index.html  # Linux
```

---

**Dashboard URL**: https://ishwarya813.github.io/code-health-dashboard/

**Last Updated**: November 18, 2025
