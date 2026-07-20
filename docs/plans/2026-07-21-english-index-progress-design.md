# English Homepage Study Progress — Design Doc

Date: 2026-07-21

## Overview

Add mark-complete and statistics functionality to all three English grade index pages (english7/8/9/index.html). Pure client-side, localStorage-based, no backend.

## Data Model

Each grade stores independently in localStorage:

```
key: `eng7-progress` | `eng8-progress` | `eng9-progress`
```

```json
{
  "completed": {
    "st01": "2026-07-21",
    "u01": "2026-07-22",
    "u02": "2026-07-22"
  },
  "lastStudyDate": "2026-07-22"
}
```

- `completed`: unit id → date string mapping
- `lastStudyDate`: most recent marking date, for "最近学习" display
- Empty localStorage = no units completed, progress = 0/0

## Components

### 1. Stats Panel (below hero, above nav-links)

```
┌─────────────────────────────────────────────┐
│ 📊 学习进度               2026-07-22 更新    │
│                                              │
│ ████████████████████░░░░░░  18 / 24  (75%)  │
│                                              │
│ 📗 七上  12/12  ████████████████████  100%   │
│ 📘 七下  6/12   ████████░░░░░░░░░░░░  50%    │
└─────────────────────────────────────────────┘
```

- Light background card, rounded corners, subtle shadow
- Overall progress bar (thick) at top
- Per-semester progress bars (thin) below
- Last study date in top-right of panel

### 2. Unit Cards

All three grades use JS data arrays to render cards (Grade 7 migrates from hardcoded HTML to JS-driven).

Each card:
- `<a>` element linking to unit page (click to navigate)
- Toggle button in **top-right corner** (click to mark/unmark, stopPropagation)
- Completed: ✅ green checkmark, green left border
- Uncompleted: ○ gray circle, default gray left border
- Re-rendered on every toggle; no page reload

### 3. Semester Headers

Real-time progress: `已完成 <strong>5</strong> / 12 单元`

Updates on every toggle via `renderProgress()`.

## Interaction Flow

1. Page load → `initProgress()`
   - Read localStorage, or create empty record
   - Render all cards with status classes
   - Render stats panel
   - Update semester headers

2. Click toggle button → `toggleComplete(unitId)`
   - If completed → remove from `completed`, clear date
   - If not completed → add to `completed` with today's date
   - Update `lastStudyDate`
   - Save to localStorage
   - Re-render that card
   - Re-render stats panel
   - Update semester headers

## Grade Config (per page)

```js
var CONFIG = {
  key: 'eng7-progress',          // localStorage key
  themeKey: 'eng7-theme',        // existing theme key
  semesters: [
    { id: 's1', label: '📗 七年级上册', sub: 'Starter 1–3 + Unit 1–9' },
    { id: 's2', label: '📘 七年级下册', sub: 'Unit 1–12' }
  ],
  units: {
    s1: [
      { id: 'st01', label: 'S1', title: 'Good morning!', topic: '字母·问候' },
      ...
    ],
    s2: [...]
  }
};
```

Grade 8 has 2 semesters (u01-u08, b2u01-b2u08). Grade 9 has 1 semester (u01-u14).

## Visual Changes

- New `.progress-panel` class for stats panel
- New `.unit-card.completed` state (green left border, checkmark)
- New `.unit-card .toggle-btn` absolute positioned top-right
- Existing `.unit-card` stays largely the same
- Responsive: progress panel stacks on mobile

## Grade 7 Migration

Current: hardcoded `<a class="unit-card done">` × 24 cards
Target: JS-generated from `CONFIG.units` (same pattern as Grade 8/9)
The 24 hardcoded cards are replaced with empty `<div class="unit-grid" id="s1-grid">` containers.

## Files Changed

- `english7/index.html` — add stats panel, JS config, replace hardcoded cards
- `english8/index.html` — add stats panel, JS config
- `english9/index.html` — add stats panel, JS config
- `english7/css/english.css` — add `.progress-panel`, `.unit-card.completed`, `.toggle-btn` styles (if not already in base.css)
- `english8/css/english8.css` — same
- `english9/css/english9.css` — same
