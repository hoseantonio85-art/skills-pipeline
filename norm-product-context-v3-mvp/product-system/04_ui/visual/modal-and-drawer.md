# Modal and Drawer Rules

## Decision

- Choose Object Modal for a self-contained object opened from a list or another object.
- Choose Drawer for a dependent task that should not replace the parent context.
- Choose a regular modal for short decisions, confirmations or focused forms.
- Choose a page when the work has its own long-lived navigation context.

## Modal anatomy

- Small: focused confirmation or short content.
- Medium: ordinary form or structured task.
- Large: complex form or substantial content.
- Object: near-fullscreen object surface; NORM reference width is about 1320px.

Keep header stable, body scrollable and footer stable when it exists. Read-only Object View normally has no footer. Create/edit actions belong in the footer. Do not invent arbitrary widths for every feature.

## Drawer anatomy

Use a stable header, scrollable content and optional fixed footer. A filter drawer commonly uses two actions: reset and apply. A drawer inside Object Modal remains visually subordinate to the object.

## Nested layers

Preserve the state of every underlying layer. Avoid stacking several scrims. Escape and close affect only the top layer. Make the return destination obvious.

These are MVP UX/visual rules. Detailed production focus management and component API belong to the later UI Kit implementation stage.
