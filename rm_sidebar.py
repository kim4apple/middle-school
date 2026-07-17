#!/usr/bin/env python3
"""Remove sidebar from appendix-vocab.html files."""
import re

for prefix in ['english8', 'english9']:
    path = f'{prefix}/appendix-vocab.html'
    with open(path) as f:
        html = f.read()
    
    # 1. Remove sidebarShowBtn button
    html = html.replace('<button id="sidebarShowBtn">☰ 侧栏</button>\n\n', '')
    html = html.replace('<button id="sidebarShowBtn">☰ 菜单</button>\n\n', '')
    
    # 2. Remove <nav id="sidebar">...</nav>
    m = re.search(r'<nav id="sidebar">.*?</nav>', html, re.DOTALL)
    if m:
        html = html.replace(m.group(0), '')
        print(f'  sidebar nav removed')
    
    # 3. Remove sidebar toggle JS section
    start = html.find('SIDEBAR TOGGLE')
    end = html.find('THEME TOGGLE', start)
    if start >= 0 and end >= 0:
        old = html[start:end]
        html = html.replace(old, '/* ── Sidebar removed ── */')
        print(f'  sidebar JS removed')
    
    # 4. Remove wrapper margin-left (no sidebar to account for)
    html = html.replace(
        '.wrapper { flex: 1; max-width: 960px; margin: 0 auto; padding: 32px 24px 60px; margin-left: var(--sidebar-width); }',
        '.wrapper { flex: 1; max-width: 960px; margin: 0 auto; padding: 32px 24px 60px; }', 1)
    html = html.replace('body:has(#sidebar.hidden) .wrapper { margin-left: 0; }', '')
    
    # 5. Remove sidebarShowBtn CSS
    html = html.replace(
        '#sidebarShowBtn { position: fixed; top: 12px; left: 12px; z-index: 99; background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 6px; padding: 6px 10px; cursor: pointer; font-size: 14px; color: var(--text); box-shadow: var(--shadow); display: none; align-items: center; gap: 4px; }\nbody:has(#sidebar.hidden) #sidebarShowBtn { display: flex; }', '')
    
    # 6. Remove sidebarShowBtn from mobile CSS
    html = html.replace('  #sidebarShowBtn { z-index: 100; }', '')
    
    # 7. Also need to remove sidebar-related body styles
    # The body has `display: flex` which is for sidebar + content layout
    # But we still want flex for wrapper layout
    
    with open(path, 'w') as f:
        f.write(html)
    print(f'✅ {prefix} complete')
