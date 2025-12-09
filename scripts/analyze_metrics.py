"""
Analyze code metrics and save to JSON file
This script analyzes your codebase and generates metrics for the dashboard
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

def analyze_complexity():
    """
    Analyze cyclomatic complexity of the codebase
    Replace this with actual analysis using tools like radon, lizard, etc.
    """
    # Example: Using radon for Python
    # from radon.complexity import cc_visit
    # complexity = cc_visit(code_string)
    
    # For now, simulate decreasing complexity trend
    today = datetime.now()
    weeks = []
    base_complexity = 30
    
    for i in range(4):
        week_date = today - timedelta(weeks=i)
        complexity = base_complexity + (i * 2)  # Decreasing trend
        weeks.insert(0, {
            'week': f'Week {4-i}',
            'complexity': complexity,
            'date': week_date.strftime('%Y-%m-%d')
        })
    
    return weeks

def analyze_test_coverage():
    """
    Analyze test coverage by module
    Replace with actual pytest-cov or coverage.py results
    """
    # Example: Run pytest with coverage
    # pytest --cov=. --cov-report=json
    
    # Simulated data
    modules = [
        {'name': 'AuthService', 'coverage': 85},
        {'name': 'PaymentProcessor', 'coverage': 42},
        {'name': 'InvoiceDAO', 'coverage': 28},
        {'name': 'CustomerServlet', 'coverage': 12}
    ]
    
    return modules

def analyze_code_churn():
    """
    Analyze code churn using git history
    """
    import subprocess
    
    try:
        # Get file change counts from last 30 days
        result = subprocess.run(
            ['git', 'log', '--since=30.days.ago', '--pretty=format:', '--name-only'],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Count occurrences
        files = result.stdout.strip().split('\n')
        file_counts = {}
        
        for file in files:
            if file and file.endswith(('.py', '.java', '.js', '.ts')):
                file_counts[file] = file_counts.get(file, 0) + 1
        
        # Get top 4
        sorted_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)[:4]
        
        churn_data = [
            {'file': file, 'changes': count} for file, count in sorted_files
        ]
        
    except subprocess.CalledProcessError:
        # Fallback to simulated data if git fails
        churn_data = [
            {'file': 'InvoiceDAO.java', 'changes': 47},
            {'file': 'BillingProcessor.java', 'changes': 31},
            {'file': 'PaymentProcessor.java', 'changes': 23},
            {'file': 'AuthService.java', 'changes': 12}
        ]
    
    return churn_data

def main():
    """Main function to analyze all metrics and save to JSON"""
    print("🔍 Analyzing code metrics...")
    
    # Collect metrics
    metrics = {
        'last_updated': datetime.now().isoformat(),
        'complexity_trend': analyze_complexity(),
        'test_coverage': analyze_test_coverage(),
        'code_churn': analyze_code_churn()
    }
    
    # Save to JSON file
    output_dir = Path(__file__).parent.parent
    output_file = output_dir / 'metrics.json'
    
    with open(output_file, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    print(f"✅ Metrics saved to {output_file}")
    print(f"   - Complexity trend: {len(metrics['complexity_trend'])} weeks")
    print(f"   - Test coverage: {len(metrics['test_coverage'])} modules")
    print(f"   - Code churn: {len(metrics['code_churn'])} files")

if __name__ == '__main__':
    main()
