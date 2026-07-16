#!/usr/bin/env python3
"""Add wrong-answer tracking + spaced repetition countdown to all 24 unit HTML files."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = sorted(f for f in os.listdir(BASE) if f.endswith('.html') and f not in ['index.html', 'appendix-grammar.html'])

REVIEW_PANEL_HTML = '''<div id="wrongReviewPanel"></div>
'''

TRACKING_JS = r'''
  // ===== Wrong-answer tracking + review =====
  (function() {
    var unitId = location.pathname.split('/').pop().replace('.html', '') || 'unknown';
    var storageKey = 'eng7_wrong_' + unitId;
    var reviewPanel = document.getElementById('wrongReviewPanel');
    if (!reviewPanel) return;

    function getWrongIds() {
      return JSON.parse(localStorage.getItem(storageKey) || '[]');
    }
    function saveWrongIds(ids) {
      localStorage.setItem(storageKey, JSON.stringify(ids));
    }
    function escapeHtml(str) {
      var d = document.createElement('div');
      d.appendChild(document.createTextNode(str));
      return d.innerHTML;
    }

    function renderReview() {
      var ids = getWrongIds();
      var items = [];
      ids.forEach(function(id) {
        var el = document.querySelector('[data-qid="' + id + '"]');
        if (!el) return;
        var qBody = el.querySelector('.q-body');
        var qSolution = el.querySelector('.q-solution');
        var qText = qBody ? qBody.textContent.trim().replace(/🔊\s*$/, '') : id;
        var answer = qSolution ? qSolution.innerHTML : '答案未找到';
        items.push({ id: id, text: qText, answer: answer });
      });

      var header = reviewPanel.querySelector('.wrong-review-header');
      if (!header) {
        header = document.createElement('div');
        header.className = 'wrong-review-header';
        reviewPanel.appendChild(header);
      }
      header.innerHTML = '📋 错题本 <span id="wrongBadge">' + items.length + '</span>';

      var body = reviewPanel.querySelector('.wrong-review-body');
      if (!body) {
        body = document.createElement('div');
        body.className = 'wrong-review-body';
        reviewPanel.appendChild(body);
      }

      if (items.length === 0) {
        body.innerHTML = '<div class="wrong-review-empty">🎉 暂无错题记录！标记答错的题目会出现在这里。</div>';
        reviewPanel.classList.remove('visible');
      } else {
        reviewPanel.classList.add('visible');
        body.innerHTML = items.map(function(item) {
          return '<div class="wrong-review-item" data-qid="' + item.id + '">' +
            '<div class="q-text">' + escapeHtml(item.text) + '</div>' +
            '<div class="q-answer">' + item.answer + '</div>' +
            '<button class="mastered-btn">✅ 已掌握，移除</button>' +
          '</div>';
        }).join('');
        body.querySelectorAll('.mastered-btn').forEach(function(btn) {
          btn.addEventListener('click', function() {
            var item = this.closest('.wrong-review-item');
            var id = item.dataset.qid;
            var ids = getWrongIds().filter(function(i) { return i !== id; });
            saveWrongIds(ids);
            var el = document.querySelector('[data-qid="' + id + '"]');
            if (el) el.classList.remove('marked-wrong');
            renderReview();
            updateButtons();
          });
        });
      }
    }

    function updateButtons() {
      var ids = getWrongIds();
      document.querySelectorAll('.wrong-btn').forEach(function(btn) {
        var el = btn.closest('.exam-q');
        if (el) {
          var isWrong = ids.indexOf(el.dataset.qid) !== -1;
          el.classList.toggle('marked-wrong', isWrong);
          btn.textContent = isWrong ? '✅ 已标记' : '❌ 答错';
          btn.classList.toggle('marked', isWrong);
        }
      });
    }

    document.querySelectorAll('.exam-q').forEach(function(el, i) {
      if (!el.dataset.qid) el.dataset.qid = unitId + '_q' + (i + 1);
      if (el.querySelector('.wrong-btn')) return;
      var btn = document.createElement('button');
      btn.className = 'wrong-btn';
      btn.textContent = '❌ 答错';
      btn.title = '标记为答错题目，加入错题本复习';
      btn.addEventListener('click', function(e) {
        e.stopPropagation();
        var id = el.dataset.qid;
        var ids = getWrongIds();
        if (el.classList.contains('marked-wrong')) {
          ids = ids.filter(function(s) { return s !== id; });
        } else {
          if (ids.indexOf(id) === -1) ids.push(id);
        }
        saveWrongIds(ids);
        updateButtons();
        renderReview();
      });
      var toggle = el.querySelector('.q-toggle');
      if (toggle) {
        toggle.parentNode.insertBefore(btn, toggle.nextSibling);
      } else {
        el.querySelector('.q-solution').parentNode.insertBefore(btn, el.querySelector('.q-solution'));
      }
    });

    updateButtons();
    renderReview();
  })();

  // ===== Spaced Repetition Countdown =====
  (function() {
    document.querySelectorAll('.review-schedule .review-dot').forEach(function(el) {
      if (el.querySelector('.countdown')) return;
      var m = el.textContent.match(/(\d+)\s*天[后以]/);
      if (m) {
        var d = new Date();
        d.setDate(d.getDate() + parseInt(m[1], 10));
        var span = document.createElement('span');
        span.className = 'countdown';
        span.textContent = ' (' + (d.getMonth()+1) + '/' + d.getDate() + ')';
        el.appendChild(span);
      }
    });
  })();
'''

def process_file(fpath):
    with open(fpath) as f:
        content = f.read()
    modified = False

    # 1. Add review panel placeholder after .checklist
    if 'wrongReviewPanel' not in content:
        # Find </div>\n\n<div class="review-schedule"> - insert panel before review-schedule
        content = content.replace(
            '<div class="review-schedule">',
            REVIEW_PANEL_HTML + '<div class="review-schedule">',
            1
        )
        modified = True

    # 2. Add tracking JS before final </script>
    if 'Wrong-answer tracking' not in content:
        content = content.replace('</script>', TRACKING_JS + '</script>', 1)
        modified = True

    if modified:
        with open(fpath, 'w') as f:
            f.write(content)
        print(f"  ✓ {os.path.basename(fpath)}")
    else:
        print(f"  - {os.path.basename(fpath)} (unchanged)")

if __name__ == '__main__':
    print(f"Processing {len(FILES)} files...")
    for fname in FILES:
        process_file(os.path.join(BASE, fname))
    print("Done.")
