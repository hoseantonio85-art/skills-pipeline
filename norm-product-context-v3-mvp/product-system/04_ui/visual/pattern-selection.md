# Pattern Selection

## Card registry

Use for the primary collection of risks, measures, incidents and similar objects. Do not use a classic table as the main surface.

A row-card should expose:

- status or attention signal;
- object title and short meaning;
- two to four decision-relevant attributes;
- consequence, amount, owner or source when relevant;
- available action or clear click affordance.

Column-like alignment is allowed. The result must still behave as a meaningful card, not a raw database row. A compact table is allowed locally for field-change history or direct comparison of homogeneous values.

## Dashboard

Use when the primary task is overview, monitoring, comparison or discovery of attention zones. Every aggregate must lead to filtering, investigation or action. Combine summary with a registry or drill-down. Avoid decorative KPI walls.

## Filters

- Put frequent, comprehensible choices in quick filters/chips.
- Show counts or semantic states when they help choose a focus.
- Reveal search on demand when it is secondary.
- Open the full filter form in a drawer.
- Mark an active advanced filter with a compact visual signal.

## Object modal

Use for a standalone object opened from a collection when the user should retain collection context. NORM object modal may be near-fullscreen, up to about 1320px.

- Keep close/back actions stable.
- Allow previous/next navigation only for sequential review.
- Use a main content area and optional right rail.
- In read-only mode keep object actions in context and avoid an unnecessary footer.
- In create/edit mode keep commit actions in a stable footer.
- Scroll the body, not the entire header/footer shell.

## Drawer

Use for a subordinate task: advanced filters, selection, settings, contextual explanation or work inside an object modal. Preserve the parent surface and return state. Do not open a full independent object in a drawer.

## Summary and AI

Use summary when it reduces interpretation work, not as mandatory decoration. Show the situation, significance and next action before evidence. Label AI-generated conclusions and provide a useful fallback when they are unavailable.
