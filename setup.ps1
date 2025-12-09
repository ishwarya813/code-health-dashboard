# Quick Setup Script for Code Health Dashboard
# Run this script to set up your GitHub repository

Write-Host "🚀 Code Health Dashboard Setup" -ForegroundColor Cyan
Write-Host "================================`n" -ForegroundColor Cyan

# Get GitHub username
$username = Read-Host "Enter your GitHub username"

if ([string]::IsNullOrWhiteSpace($username)) {
    Write-Host "❌ Username cannot be empty!" -ForegroundColor Red
    exit 1
}

Write-Host "`n📍 Setting up repository for user: $username" -ForegroundColor Green

# Navigate to repo directory
$repoPath = "C:\Users\IshwaryaKannan\OneDrive - Atmosera\Desktop\code-health-dashboard"
Set-Location $repoPath

# Update remote URL
Write-Host "`n🔗 Updating remote URL..." -ForegroundColor Yellow
git remote set-url origin "https://github.com/$username/code-health-dashboard.git"
git remote -v

# Check if there are files to commit
Write-Host "`n📦 Checking repository status..." -ForegroundColor Yellow
$status = git status --porcelain

if ($status) {
    Write-Host "✓ Files ready to commit" -ForegroundColor Green
    
    # Add all files
    Write-Host "`n➕ Adding files..." -ForegroundColor Yellow
    git add .
    
    # Show what will be committed
    Write-Host "`n📋 Files to be committed:" -ForegroundColor Cyan
    git status --short
    
    # Commit
    Write-Host "`n💾 Creating initial commit..." -ForegroundColor Yellow
    git commit -m "Initial commit: Add code health dashboard with automation"
    
    # Set main branch
    Write-Host "`n🌿 Setting main branch..." -ForegroundColor Yellow
    git branch -M main
    
    # Ask before pushing
    Write-Host "`n⚠️  Ready to push to GitHub!" -ForegroundColor Yellow
    $confirm = Read-Host "Push to https://github.com/$username/code-health-dashboard? (yes/no)"
    
    if ($confirm -eq "yes" -or $confirm -eq "y") {
        Write-Host "`n🚀 Pushing to GitHub..." -ForegroundColor Yellow
        git push -u origin main
        
        Write-Host "`n✅ SUCCESS! Your dashboard has been pushed to GitHub!" -ForegroundColor Green
        Write-Host "`n📝 Next Steps:" -ForegroundColor Cyan
        Write-Host "   1. Go to: https://github.com/$username/code-health-dashboard" -ForegroundColor White
        Write-Host "   2. Click Settings → Pages" -ForegroundColor White
        Write-Host "   3. Under Source, select 'main' branch and '/ (root)' folder" -ForegroundColor White
        Write-Host "   4. Click Save" -ForegroundColor White
        Write-Host "   5. Wait 1-2 minutes, then visit:" -ForegroundColor White
        Write-Host "      https://$username.github.io/code-health-dashboard/" -ForegroundColor Yellow
        Write-Host "`n   📖 See SETUP_GUIDE.md for more details" -ForegroundColor Gray
    } else {
        Write-Host "`n⏸️  Push cancelled. Run 'git push -u origin main' when ready." -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠️  No changes to commit. Repository may already be set up." -ForegroundColor Yellow
}

Write-Host "`n✨ Setup script complete!" -ForegroundColor Cyan
