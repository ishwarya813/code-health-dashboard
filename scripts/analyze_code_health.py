#!/usr/bin/env python3
"""
Analyze code health metrics from the Python codebase
Outputs metrics to metrics.json for dashboard consumption
"""

import ast
import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List
import subprocess


def calculate_cyclomatic_complexity(node):
    """Calculate cyclomatic complexity for a function/method"""
    complexity = 1
    for child in ast.walk(node):
        if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
            complexity += 1
        elif isinstance(child, ast.BoolOp):
            complexity += len(child.values) - 1
    return complexity


def count_lines(node):
    """Count lines in a function/method"""
    if hasattr(node, 'end_lineno') and hasattr(node, 'lineno'):
        return node.end_lineno - node.lineno + 1
    return 0


def analyze_python_files(directory: str = 'python') -> Dict:
    """Analyze all Python files in the directory"""
    
    results = {
        'total_complexity': 0,
        'function_count': 0,
        'max_complexity': 0,
        'files': {},
        'high_complexity_functions': []
    }
    
    python_dir = Path(directory)
    if not python_dir.exists():
        return results
    
    for py_file in python_dir.glob('*.py'):
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                source = f.read()
            
            tree = ast.parse(source, filename=str(py_file))
            
            file_complexity = 0
            file_functions = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    complexity = calculate_cyclomatic_complexity(node)
                    lines = count_lines(node)
                    
                    file_complexity += complexity
                    results['function_count'] += 1
                    
                    func_info = {
                        'name': node.name,
                        'complexity': complexity,
                        'lines': lines,
                        'file': py_file.name
                    }
                    
                    file_functions.append(func_info)
                    
                    if complexity > results['max_complexity']:
                        results['max_complexity'] = complexity
                    
                    if complexity > 15:
                        results['high_complexity_functions'].append(func_info)
            
            results['files'][py_file.name] = {
                'complexity': file_complexity,
                'functions': file_functions
            }
            
            results['total_complexity'] += file_complexity
            
        except Exception as e:
            print(f"Error analyzing {py_file}: {e}")
    
    # Calculate average complexity
    if results['function_count'] > 0:
        results['avg_complexity'] = round(results['total_complexity'] / results['function_count'], 1)
    else:
        results['avg_complexity'] = 0
    
    return results


def get_git_churn(days: int = 30) -> List[Dict]:
    """Get git commit statistics for the last N days"""
    
    try:
        # Check if we're in a git repository
        subprocess.run(['git', 'rev-parse', '--git-dir'], 
                      capture_output=True, check=True)
        
        # Get commits from the last N days
        since_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        # Get file change statistics
        result = subprocess.run(
            ['git', 'log', f'--since={since_date}', '--name-only', '--pretty=format:'],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Count changes per file
        file_changes = {}
        for line in result.stdout.split('\n'):
            line = line.strip()
            if line and line.endswith('.py'):
                file_changes[line] = file_changes.get(line, 0) + 1
        
        # Sort by change count
        sorted_changes = sorted(file_changes.items(), key=lambda x: x[1], reverse=True)
        
        return [
            {'file': file, 'changes': count}
            for file, count in sorted_changes[:10]
        ]
    
    except subprocess.CalledProcessError:
        print("Not a git repository or git not available")
        return []
    except Exception as e:
        print(f"Error getting git churn: {e}")
        return []


def simulate_test_coverage() -> Dict[str, int]:
    """
    Simulate test coverage percentages
    In a real scenario, this would parse coverage reports
    """
    
    # For demo purposes, we'll use realistic but simulated values
    # In production, parse actual coverage.xml or .coverage files
    
    return {
        'customer_servlet.py': 12,
        'invoice_dao.py': 28,
        'payment_processor.py': 42,
        'auth_service.py': 85  # Simulated additional module
    }


def load_previous_metrics() -> Dict:
    """Load previous metrics to track trends"""
    
    metrics_file = Path('metrics.json')
    if metrics_file.exists():
        try:
            with open(metrics_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading previous metrics: {e}")
    
    return {}


def calculate_trends(current_metrics: Dict, previous_metrics: Dict) -> Dict:
    """Calculate weekly trends for the dashboard"""
    
    trends = {
        'complexity_history': []
    }
    
    # If we have previous data, append current to history
    if previous_metrics and 'trends' in previous_metrics:
        prev_trends = previous_metrics['trends']
        if 'complexity_history' in prev_trends:
            trends['complexity_history'] = prev_trends['complexity_history'][-3:]  # Keep last 3 weeks
    
    # Add current week's data
    trends['complexity_history'].append({
        'date': datetime.now().isoformat(),
        'avg_complexity': current_metrics.get('avg_complexity', 0)
    })
    
    return trends


def main():
    """Main analysis function"""
    
    print("🔍 Analyzing code health...")
    
    # Load previous metrics
    previous_metrics = load_previous_metrics()
    
    # Analyze Python code
    code_analysis = analyze_python_files('python')
    
    # Get git churn
    churn_data = get_git_churn(30)
    
    # Get test coverage
    coverage_data = simulate_test_coverage()
    
    # Calculate trends
    trends = calculate_trends(code_analysis, previous_metrics)
    
    # Compile all metrics
    metrics = {
        'timestamp': datetime.now().isoformat(),
        'avg_complexity': code_analysis['avg_complexity'],
        'max_complexity': code_analysis['max_complexity'],
        'function_count': code_analysis['function_count'],
        'high_complexity_count': len(code_analysis['high_complexity_functions']),
        'coverage': coverage_data,
        'churn': churn_data,
        'trends': trends,
        'files': code_analysis['files']
    }
    
    # Save metrics
    with open('metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)
    
    print(f"✅ Analysis complete!")
    print(f"   Average Complexity: {metrics['avg_complexity']}")
    print(f"   Max Complexity: {metrics['max_complexity']}")
    print(f"   High Complexity Functions: {metrics['high_complexity_count']}")
    print(f"   Files Analyzed: {len(code_analysis['files'])}")
    print(f"   Churn Hotspots: {len(churn_data)}")


if __name__ == '__main__':
    main()
