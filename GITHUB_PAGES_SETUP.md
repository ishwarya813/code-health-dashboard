# GitHub Pages Setup Guide for Code Health Dashboard

## ✅ Status Check
- **Repository**: code-health-dashboard (exists on GitHub)
- **Local Clone**: Not found - needs to be cloned

---

## 📋 Step-by-Step Setup Instructions

### Step 1: Clone Your Repository

Open PowerShell and run:

```powershell
# Navigate to your preferred directory
cd "$env:USERPROFILE\Documents"

# Clone your repository
git clone https://github.com/YOUR_USERNAME/code-health-dashboard.git

# Navigate into the repository
cd code-health-dashboard
```

**Replace `YOUR_USERNAME`** with your actual GitHub username.

---

### Step 2: Copy Dashboard Files to Repository

```powershell
# Copy the dashboard HTML file
Copy-Item "c:\Users\IshwaryaKannan\OneDrive - Atmosera\Documents\w2 tue -code health\code_health_code1\code_health_dashboard.html" -Destination ".\index.html"

# Copy the GitHub Actions workflow
New-Item -ItemType Directory -Path ".\.github\workflows" -Force
Copy-Item "c:\Users\IshwaryaKannan\OneDrive - Atmosera\Documents\w2 tue -code health\code_health_code1\.github\workflows\update-dashboard.yml" -Destination ".\.github\workflows\"

# Copy the update script
New-Item -ItemType Directory -Path ".\scripts" -Force
Copy-Item "c:\Users\IshwaryaKannan\OneDrive - Atmosera\Documents\w2 tue -code health\code_health_code1\scripts\update_dashboard.py" -Destination ".\scripts\"

# Copy Python source files (for analysis)
New-Item -ItemType Directory -Path ".\python" -Force
Copy-Item "c:\Users\IshwaryaKannan\OneDrive - Atmosera\Documents\w2 tue -code health\code_health_code1\python\*" -Destination ".\python\" -Recurse
```

**Note**: We rename `code_health_dashboard.html` to `index.html` so it serves as the homepage.

---

### Step 3: Create README for Your Repository

```powershell
@"
# Code Health Dashboard 📊

Live dashboard tracking code quality metrics for our project.

## 🔗 View Dashboard
👉 **[View Live Dashboard](https://YOUR_USERNAME.github.io/code-health-dashboard/)**

## 📈 Metrics Tracked
- Cyclomatic complexity trends
- Test coverage by module
- Code churn hotspots
- Sprint achievements

## 🔄 Updates
Dashboard automatically updates every Monday at 9 AM UTC via GitHub Actions.

## 🛠️ Technologies
- Chart.js for visualizations
- GitHub Pages for hosting
- GitHub Actions for automation
- Python (radon, pytest) for metrics collection
"@ | Out-File -FilePath ".\README.md" -Encoding utf8
```

**Replace `YOUR_USERNAME`** with your GitHub username.

---

### Step 4: Commit and Push Files

```powershell
# Add all files
git add .

# Commit
git commit -m "🚀 Initial dashboard setup with GitHub Actions automation"

# Push to GitHub
git push origin main
```

**Note**: If your default branch is `master` instead of `main`, use `git push origin master`.

---

### Step 5: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/YOUR_USERNAME/code-health-dashboard`

2. Click **Settings** (⚙️ tab at the top)

3. Scroll down to **Pages** section in the left sidebar

4. Under **Source**, select:
   - **Branch**: `main` (or `master`)
   - **Folder**: `/ (root)`

5. Click **Save**

6. Wait 1-2 minutes for deployment

7. Your dashboard will be available at:
   ```
   https://YOUR_USERNAME.github.io/code-health-dashboard/
   ```

---

### Step 6: Configure GitHub Actions Permissions

1. In your repository, go to **Settings** → **Actions** → **General**

2. Scroll to **Workflow permissions**

3. Select: **"Read and write permissions"**

4. Check: **"Allow GitHub Actions to create and approve pull requests"**

5. Click **Save**

This allows the automated workflow to commit dashboard updates.

---

## 🤖 Automated Weekly Updates

The dashboard automatically updates using GitHub Actions:

### Schedule
- **Every Monday at 9:00 AM UTC**
- Manual trigger available via Actions tab

### What Gets Updated
1. **Cyclomatic Complexity**: Analyzed via `radon`
2. **Test Coverage**: Calculated via `pytest-cov`
3. **Code Churn**: Git log analysis (last 30 days)
4. **Timestamp**: Current date/time

### Workflow File Location
`.github/workflows/update-dashboard.yml`

### Manual Trigger
1. Go to **Actions** tab in your repository
2. Select **"Update Code Health Dashboard"** workflow
3. Click **"Run workflow"** button
4. Select branch and click **"Run workflow"**

---

## 🧪 Testing the Automation

### Test Immediately (Don't Wait for Monday)

```powershell
# Trigger via GitHub CLI (if installed)
gh workflow run update-dashboard.yml

# OR push a commit to trigger the workflow
git commit --allow-empty -m "Test automation"
git push
```

### View Workflow Logs
1. Go to **Actions** tab in your repository
2. Click on the latest workflow run
3. Click on the job name to see detailed logs

---

## 📊 Customizing Metrics

### Update Complexity Thresholds
Edit `scripts/update_dashboard.py`:

```python
def calculate_complexity_trend(current_complexity):
    # Customize your trend calculation
    week4 = current_complexity
    week3 = round(week4 + 2)  # Adjust these values
    week2 = round(week3 + 3)
    week1 = round(week2 + 3)
    return [week1, week2, week3, week4]
```

### Change Update Schedule
Edit `.github/workflows/update-dashboard.yml`:

```yaml
schedule:
  - cron: '0 9 * * 1'  # Every Monday at 9 AM UTC
  
  # Examples:
  # - cron: '0 0 * * *'    # Daily at midnight
  # - cron: '0 9 * * 1,4'  # Monday and Thursday at 9 AM
  # - cron: '0 */6 * * *'  # Every 6 hours
```

Cron format: `minute hour day month weekday`

---

## 🔍 Troubleshooting

### Dashboard Not Showing
1. Check if GitHub Pages is enabled (Settings → Pages)
2. Verify `index.html` exists in root directory
3. Wait 2-3 minutes after pushing changes
4. Check browser console for JavaScript errors

### GitHub Actions Failing
1. Go to **Actions** tab and view error logs
2. Common issues:
   - Missing dependencies: Check `pip install` step
   - Permission denied: Enable write permissions (Step 6 above)
   - Python files not found: Ensure `python/` directory exists

### Metrics Not Updating
1. Verify workflow ran successfully (Actions tab)
2. Check if there were changes to commit
3. Ensure `scripts/update_dashboard.py` has correct file paths
4. Review workflow artifacts for analysis reports

---

## 📦 Required Files Structure

```
code-health-dashboard/
├── index.html                          # Main dashboard (renamed from code_health_dashboard.html)
├── README.md                           # Repository documentation
├── .github/
│   └── workflows/
│       └── update-dashboard.yml        # Automation workflow
├── scripts/
│   └── update_dashboard.py             # Metrics updater script
└── python/                             # Source code to analyze
    ├── payment_processor.py
    ├── customer_servlet.py
    └── invoice_dao.py
```

---

## 🎯 Next Steps

After setup:

1. ✅ Visit your live dashboard URL
2. ✅ Test manual workflow trigger
3. ✅ Customize metrics thresholds for your team
4. ✅ Share dashboard URL with your team
5. ✅ Set up Slack/Teams notifications for metric changes (optional)

---

## 💡 Pro Tips

### Custom Domain (Optional)
1. Add a `CNAME` file with your domain: `dashboard.yourcompany.com`
2. Configure DNS settings at your domain provider
3. Enable HTTPS in GitHub Pages settings

### Metric History Tracking
Store historical data in a JSON file:

```yaml
# Add to workflow
- name: Store historical metrics
  run: |
    echo '{"date":"'$(date +%Y-%m-%d)'","complexity":'$COMPLEXITY'}' >> metrics_history.json
    git add metrics_history.json
```

### Email Notifications
Add to workflow for failures:

```yaml
- name: Send notification on failure
  if: failure()
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 587
    username: ${{ secrets.EMAIL_USERNAME }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: Dashboard Update Failed
    body: Check the workflow logs for details
    to: team@company.com
```

---

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Radon (Complexity Tool)](https://radon.readthedocs.io/)
- [Chart.js Documentation](https://www.chartjs.org/)

---

**Need Help?** Check the [Issues](https://github.com/YOUR_USERNAME/code-health-dashboard/issues) or contact the team.
