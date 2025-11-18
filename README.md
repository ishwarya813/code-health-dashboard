# 📊 Code Health Dashboard

A live, automated dashboard tracking code health metrics for Python projects.

## 🌐 Live Dashboard

View the dashboard at: **https://ishwarya813.github.io/code-health-dashboard/**

## 📈 Tracked Metrics

- **Cyclomatic Complexity Trends** - Weekly average complexity tracking
- **Test Coverage by Module** - Coverage percentage for each component
- **Code Churn Hotspots** - Files with most changes in last 30 days
- **This Sprint's Wins** - Recent improvements and achievements

## 🚀 Setup Instructions

### 1. Enable GitHub Pages

1. Go to your repository settings: `https://github.com/ishwarya813/code-health-dashboard/settings/pages`
2. Under "Source", select **Deploy from a branch**
3. Choose branch: **main** and folder: **/ (root)**
4. Click **Save**
5. Your dashboard will be live at: `https://ishwarya813.github.io/code-health-dashboard/`

### 2. Automated Weekly Updates

The dashboard automatically updates **every Monday at 9 AM UTC** via GitHub Actions.

**What it does:**
- Analyzes Python code for complexity metrics
- Tracks git commit history for churn analysis
- Updates test coverage data
- Regenerates dashboard with latest metrics
- Commits changes back to the repository

### 3. Manual Trigger

To manually trigger an update:

1. Go to **Actions** tab in your repository
2. Select **Update Code Health Dashboard** workflow
3. Click **Run workflow** button
4. Select branch and click **Run workflow**

## 🛠️ Local Development

### Run Analysis Locally

```bash
# Install dependencies
pip install radon gitpython

# Run analysis
python scripts/analyze_code_health.py

# Update dashboard
python scripts/update_dashboard.py

# View locally
# Open index.html in your browser
```

### File Structure

```
code-health-dashboard/
├── index.html                          # Main dashboard (auto-updated)
├── metrics.json                        # Generated metrics data
├── python/                            # Code to analyze
│   ├── customer_servlet.py
│   ├── invoice_dao.py
│   └── payment_processor.py
├── scripts/                           # Automation scripts
│   ├── analyze_code_health.py        # Code analysis
│   └── update_dashboard.py           # Dashboard updater
└── .github/
    └── workflows/
        └── update-dashboard.yml       # GitHub Actions workflow
```

## 📅 Automation Schedule

- **Weekly Updates**: Every Monday at 9:00 AM UTC
- **On Code Changes**: Triggered when Python files are modified
- **Manual**: Via GitHub Actions UI anytime

## 🎨 Customization

### Modify Update Frequency

Edit `.github/workflows/update-dashboard.yml`:

```yaml
schedule:
  - cron: '0 9 * * 1'  # Change this cron expression
  # Examples:
  # '0 9 * * *'        # Daily at 9 AM
  # '0 9 * * 1,4'      # Monday and Thursday at 9 AM
  # '0 */6 * * *'      # Every 6 hours
```

### Add New Metrics

1. Update `scripts/analyze_code_health.py` to calculate new metrics
2. Save to `metrics.json`
3. Update `scripts/update_dashboard.py` to inject into HTML
4. Modify `index.html` template as needed

## 🔧 Troubleshooting

### Dashboard Not Updating

1. Check GitHub Actions workflow status in **Actions** tab
2. Verify GitHub Pages is enabled and deploying from correct branch
3. Check workflow logs for errors
4. Ensure repository has write permissions for GitHub Actions

### Metrics Not Accurate

1. Verify Python files exist in `python/` directory
2. Check `metrics.json` for valid data
3. Run analysis scripts locally to debug
4. Check git history is available (for churn analysis)

## 📊 Dashboard Features

- **Responsive Design** - Works on desktop, tablet, and mobile
- **Real-time Charts** - Interactive Chart.js visualizations
- **Color Coding** - Green (healthy), Yellow (watch), Red (action needed)
- **Automatic Updates** - No manual intervention needed
- **Git Integration** - Tracks actual repository activity

## 🤝 Contributing

To improve the dashboard:

1. Fork the repository
2. Make changes to analysis scripts or dashboard template
3. Test locally
4. Submit a pull request

## 📝 License

MIT License - Feel free to use and modify for your projects!

---

**Last Updated**: Auto-updated by GitHub Actions every Monday
