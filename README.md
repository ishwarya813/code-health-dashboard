# Code Health Dashboard 📊

A beautiful, automated dashboard for tracking code health metrics including cyclomatic complexity, test coverage, and code churn.

## 🌐 Live Dashboard

Visit: `https://YOUR_USERNAME.github.io/code-health-dashboard/`

## 🚀 Features

- **Cyclomatic Complexity Trends** - Track complexity over time
- **Test Coverage by Module** - Monitor test coverage across codebase
- **Code Churn Hotspots** - Identify frequently changed files
- **Automated Weekly Updates** - GitHub Actions updates metrics every Monday at 9 AM
- **Color-Coded Metrics** - Quick visual health indicators
- **Mobile Responsive** - View on any device

## 📅 Automated Updates

This dashboard automatically updates every Monday at 9:00 AM UTC via GitHub Actions.

### Manual Update

You can also manually trigger an update:
1. Go to the **Actions** tab in GitHub
2. Select **Update Code Health Dashboard**
3. Click **Run workflow**

## 🛠️ Setup Instructions

### 1. Enable GitHub Pages

1. Go to repository **Settings** → **Pages**
2. Under **Source**, select branch: `gh-pages`
3. Click **Save**
4. Your dashboard will be live at: `https://YOUR_USERNAME.github.io/code-health-dashboard/`

### 2. Configure the Workflow

The workflow runs automatically, but you can customize:
- **Schedule**: Edit `.github/workflows/update-dashboard.yml` to change the cron schedule
- **Metrics**: Modify `scripts/analyze_metrics.py` to analyze your specific codebase
- **Dashboard**: Update `scripts/update_dashboard.py` to customize data presentation

### 3. Permissions

Ensure GitHub Actions has write permissions:
1. Go to **Settings** → **Actions** → **General**
2. Under **Workflow permissions**, select **Read and write permissions**
3. Click **Save**

## 📊 Customizing Metrics

### Analyze Your Own Code

Edit `scripts/analyze_metrics.py`:

```python
def analyze_complexity():
    # Use tools like radon, lizard, or sonarqube
    from radon.complexity import cc_visit
    # ... your analysis code
```

### Add New Metrics

1. Update `scripts/analyze_metrics.py` to collect new data
2. Save to `metrics.json`
3. Update `scripts/update_dashboard.py` to inject into HTML
4. Modify `index.html` to display the new metrics

## 🔧 Local Development

Test the scripts locally:

```bash
# Install dependencies
pip install radon pylint pytest pytest-cov

# Run analysis
python scripts/analyze_metrics.py

# Update dashboard
python scripts/update_dashboard.py

# View dashboard
open index.html  # Mac/Linux
start index.html  # Windows
```

## 📦 Dependencies

- **Python 3.11+** for analysis scripts
- **Chart.js** (CDN) for interactive charts
- **GitHub Actions** for automation

## 🤝 Contributing

Feel free to customize and enhance this dashboard for your team's needs!

## 📝 License

MIT License - Feel free to use and modify
