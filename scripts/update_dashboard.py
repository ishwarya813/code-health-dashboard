"""
Update the dashboard HTML with fresh metrics from metrics.json
"""

import json
import re
from pathlib import Path
from datetime import datetime

def load_metrics():
    """Load metrics from JSON file"""
    metrics_file = Path(__file__).parent.parent / 'metrics.json'
    
    if not metrics_file.exists():
        print("⚠️  No metrics.json found, using default values")
        return None
    
    with open(metrics_file, 'r') as f:
        return json.load(f)

def update_html_metrics(html_content, metrics):
    """Update the HTML content with new metrics"""
    if not metrics:
        return html_content
    
    # Update complexity data
    complexity_values = [item['complexity'] for item in metrics['complexity_trend']]
    complexity_str = str(complexity_values)
    
    html_content = re.sub(
        r'const complexityData = \[[\d,\s]+\];',
        f'const complexityData = {complexity_str};',
        html_content
    )
    
    # Update test coverage data
    coverage_js = "const coverageData = [\n"
    for module in metrics['test_coverage']:
        coverage_js += f"            {{ module: '{module['name']}', coverage: {module['coverage']} }},\n"
    coverage_js += "        ];"
    
    html_content = re.sub(
        r'const coverageData = \[[\s\S]*?\];',
        coverage_js,
        html_content
    )
    
    # Update code churn table
    churn_html = ""
    for item in metrics['code_churn']:
        changes = item['changes']
        badge_class = 'badge-red' if changes > 30 else 'badge-yellow' if changes > 15 else 'badge-green'
        badge_text = 'High Activity' if changes > 30 else 'Moderate Activity' if changes > 15 else 'Normal Activity'
        
        churn_html += f"""                    <tr>
                        <td><strong>{item['file']}</strong></td>
                        <td><span class="change-count">{changes}</span></td>
                        <td><span class="badge {badge_class}">{badge_text}</span></td>
                    </tr>
"""
    
    html_content = re.sub(
        r'<tbody>[\s\S]*?</tbody>',
        f'<tbody>\n{churn_html}                </tbody>',
        html_content
    )
    
    # Update timestamp placeholder to use actual timestamp
    html_content = re.sub(
        r"document\.getElementById\('timestamp'\)\.textContent = new Date\(\)\.toLocaleString\(\);",
        f"document.getElementById('timestamp').textContent = '{datetime.now().strftime('%B %d, %Y at %I:%M %p')}';",
        html_content
    )
    
    return html_content

def main():
    """Main function to update dashboard"""
    print("📊 Updating dashboard with new metrics...")
    
    # Load metrics
    metrics = load_metrics()
    
    # Read current HTML
    dashboard_file = Path(__file__).parent.parent / 'index.html'
    
    if not dashboard_file.exists():
        print("❌ index.html not found!")
        return
    
    with open(dashboard_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Update metrics
    updated_html = update_html_metrics(html_content, metrics)
    
    # Write back to file
    with open(dashboard_file, 'w', encoding='utf-8') as f:
        f.write(updated_html)
    
    print("✅ Dashboard updated successfully!")

if __name__ == '__main__':
    main()
