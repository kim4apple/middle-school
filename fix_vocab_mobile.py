#!/usr/bin/env python3
"""Rewrite mobile table CSS for appendix-vocab.html to work on both mobile and desktop."""
import re

FILES = ['english8/appendix-vocab.html', 'english9/appendix-vocab.html']

# Replace the 700px block
OLD_700 = """@media (max-width: 700px) {
  .vocab-table thead { display: none; }
  .vocab-table th:nth-child(3), .vocab-table th:nth-child(6) { display: none; }
  .vocab-table .ex-cell { display: none; }
  .vocab-table .ipa-cell { display: inline; }
  .vocab-unit summary .sum-content span { font-size: 13px; }
}"""

NEW_700 = """@media (max-width: 700px) {
  .vocab-table th:nth-child(3), .vocab-table th:nth-child(6) { display: none; }
  .vocab-table .ipa-cell, .vocab-table .ex-cell { display: none; }
}"""

# Full rewrite of the main 640px block's table section
OLD_640_FULL = """@media (max-width: 640px) {
  .wrapper { padding: 16px 10px 40px; }
  #sidebarShowBtn { z-index: 100; }""".split('\n')[0]

# We need to replace the entire SECOND @media (max-width: 640px) block
# Let me find it by reading the file

NEW_640 = """@media (max-width: 640px) {
  .wrapper { padding: 16px 10px 40px; }
  #sidebarShowBtn { z-index: 100; }
  .hero h1 { font-size: 22px; }
  .hero .tagline { font-size: 12px; }
  .hero .badge { font-size: 10px; padding: 3px 10px; }
  .top-bar { flex-direction: column; align-items: stretch; gap: 8px; }
  .view-toggle { justify-content: center; }
  .view-toggle button { font-size: 11px; padding: 5px 10px; }
  #unitFilter { font-size: 12px; padding: 6px 10px; }
  .back-link { font-size: 12px; margin-bottom: 16px; }

  /* ── Vocab unit cards ── */
  .vocab-unit summary { font-size: 13px; padding: 8px 10px; }
  .vocab-unit summary .unit-progress { font-size: 10px; white-space: nowrap; }
  .vocab-unit summary .unit-progress .pct { min-width: 20px; }
  .vocab-unit summary .unit-progress .srs-due { font-size: 9px; padding: 1px 5px; white-space: nowrap; }
  .vocab-unit summary .sum-content span { max-width: 55%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; display: inline-block; vertical-align: middle; }

  /* ── Table → Card layout ── */
  .vocab-table { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 14px; }
  .vocab-table thead { display: none; }
  .vocab-table tbody { display: block; }
  .vocab-table tr { display: block; padding: 12px; margin-bottom: 6px; border: 1px solid var(--border); border-radius: 10px; background: var(--bg); }
  .vocab-table td { display: inline; padding: 0; border: none; white-space: normal; font-size: 14px; vertical-align: baseline; }
  .vocab-table tr:last-child td { border: none; }
  .vocab-table .cb-cell { display: inline-block; float: left; margin: 2px 10px 0 0; width: auto; }
  .vocab-table .cb-cell input { width: 18px; height: 18px; }
  .vocab-table .word-cell { display: inline; font-size: 16px; font-weight: 700; color: var(--accent); }
  .vocab-table .word-cell .speak-indicator { font-size: 12px; }
  .vocab-table .word-cell .wrong-tag { font-size: 10px; padding: 1px 6px; vertical-align: middle; margin-left: 4px; }
  .vocab-table .ipa-cell { display: inline; font-size: 12px; color: var(--text-secondary); margin-left: 6px; }
  .vocab-table .pos-cell { display: inline; font-size: 11px; color: var(--accent); text-transform: uppercase; margin-left: 4px; }
  .vocab-table .def-cell { display: block; font-size: 14px; color: var(--text); margin-top: 6px; padding-left: 0 !important; max-width: 100%; overflow: visible; white-space: normal; }
  .vocab-table .ex-cell { display: none; }
  .vocab-table .mastered td { opacity: 0.55; }
  .vocab-table .wrong-row { background: #fef2f2; border-color: #fecaca; }

  /* ── Other views ── */
  .flashcard .front .big-word { font-size: 24px; }
  .flashcard .back .back-def { font-size: 20px; }
  .flashcard .front, .flashcard .back { padding: 24px 16px; min-height: 240px; }
  .flashcard-nav button { padding: 8px 16px; font-size: 13px; }
  .flashcard-header { flex-direction: column; align-items: flex-start; }
  .dictation-card .dict-chinese { font-size: 22px; }
  .dictation-input-wrap input { font-size: 16px; padding: 10px 12px; }
  .dictation-input-wrap { max-width: 100%; }
  .dictation-nav button { padding: 8px 16px; font-size: 13px; }
  .quiz-question { font-size: 20px; }
  .quiz-option { font-size: 14px; padding: 10px 12px; }
  .quiz-header .q-progress { font-size: 12px; }
  .stats-grid { grid-template-columns: 1fr 1fr; gap: 8px; }
  .stat-card .stat-value { font-size: 22px; }
  .stat-card { padding: 14px; }
  .stats-wrong-list { max-height: 200px; }
  .stats-units .su-row { padding: 6px 8px; }
  .stats-units .su-label { font-size: 11px; min-width: 0; }
}"""

OLD_360 = """@media (max-width: 360px) {
  .hero h1 { font-size: 18px; }
  .view-toggle button { font-size: 9px; padding: 3px 6px; }
  .vocab-table { font-size: 11px; }
  .vocab-table .word-cell { font-size: 13px; }
  .vocab-table .ipa-cell { display: none; }
  .vocab-table .pos-cell { font-size: 9px; }
  .vocab-table .def-cell { font-size: 11px; }
  .vocab-table tr { padding: 6px 4px; gap: 3px; }
  .vocab-table .cb-cell { flex: 0 0 24px; }
  .vocab-table .cb-cell input { width: 14px; height: 14px; }
  .vocab-unit summary { font-size: 11px; padding: 6px 8px; }
  .vocab-unit summary .sum-content span { max-width: 55%; font-size: 11px; }
  .vocab-unit summary .unit-progress .srs-due { display: none; }
  .vocab-table .def-cell { padding-left: 28px; }
}"""

NEW_360 = """@media (max-width: 360px) {
  .hero h1 { font-size: 18px; }
  .view-toggle button { font-size: 9px; padding: 3px 6px; }
  .vocab-table { font-size: 13px; }
  .vocab-table tr { padding: 10px 8px; }
  .vocab-table .word-cell { font-size: 15px; }
  .vocab-table .ipa-cell { display: none; }
  .vocab-table .pos-cell { font-size: 10px; }
  .vocab-table .def-cell { font-size: 13px; }
  .vocab-table .cb-cell input { width: 16px; height: 16px; }
  .vocab-unit summary { font-size: 12px; padding: 6px 8px; }
  .vocab-unit summary .sum-content span { max-width: 50%; font-size: 11px; }
  .vocab-unit summary .unit-progress .srs-due { display: none; }
}"""

if __name__ == '__main__':
    for path in FILES:
        with open(path) as f:
            html = f.read()
        
        html = html.replace(OLD_700, NEW_700, 1)
        
        # Find and replace the large 640px block
        # Find the second occurrence of "@media (max-width: 640px)"
        first = html.find('@media (max-width: 640px) {')
        if first >= 0:
            second = html.find('@media (max-width: 640px) {', first + 10)
            if second >= 0:
                # Find the closing brace of this block
                depth = 1
                end = second + 27  # after the opening brace
                while depth > 0 and end < len(html):
                    if html[end] == '{': depth += 1
                    elif html[end] == '}': depth -= 1
                    end += 1
                # Replace from second to end
                html = html[:second] + NEW_640 + html[end:]
        
        html = html.replace(OLD_360, NEW_360, 1)
        
        with open(path, 'w') as f:
            f.write(html)
        print(f'✅ {path}')
