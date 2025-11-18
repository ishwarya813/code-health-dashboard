[1]
Analyze this Java codebase and provide a code health baseline including:

1. Cyclomatic complexity by module
   - Identify methods/classes with complexity > 15
   - Rank top 5 most complex components

2. Test coverage gaps on critical paths
   - Identify files with < 40% test coverage
   - Flag untested business logic

3. Code smell density
   - Duplicated code blocks
   - Long methods (> 50 lines)
   - God classes (> 500 lines)
   - Deep nesting (> 3 levels)

4. Security vulnerability count
   - SQL injection risks
   - Input validation gaps
   - Authentication/authorization issues

5. Dependencies with known CVEs
   - Outdated dependencies
   - Security vulnerabilities in dependencies

Please provide:
- A summary table with scores for each category
- Top 3 priority areas for improvement
- Specific file/method locations for each issue

[2]
Why is PaymentProcessor flagged as high complexity? 

Provide:
- Specific complexity contributors (nesting, branches, loops)
- Business logic vs infrastructure concerns mix
- Recommendations for refactoring approaches

[3] -- DB creation

Create a standalone HTML dashboard that displays code health metrics with the following components:

1. Line chart showing complexity trends over the last 4 weeks:
   - Week 1: 38
   - Week 2: 35
   - Week 3: 32
   - Week 4: 30

2. Horizontal bar chart showing test coverage by module:
   - AuthService: 85%
   - PaymentProcessor: 42%
   - InvoiceDAO: 28%
   - CustomerServlet: 12%

3. Table of code churn hotspots (last 30 days):
   - InvoiceDAO.java: 47 changes
   - BillingProcessor.java: 31 changes
   - PaymentProcessor.java: 23 changes
   - AuthService.java: 12 changes

4. Highlighted "This Sprint's Win" section:
   - "Reduced complexity in PaymentProcessor from 42 → 28"

Requirements:
- Use Chart.js or similar lightweight charting library (CDN)
- Color code: Green (healthy), Yellow (watch), Red (action needed)
- Mobile responsive
- Include a last updated timestamp
- Add a section for "Next Priority" (empty, to be filled in)

Style: Clean, professional, easy to read at a glance