# Layout and Density

## Shell

Use a stable product shell with navigation outside a rounded light work surface. The prototype may simplify global navigation, but it must still feel embedded in NORM rather than displayed on a blank page.

Recommended desktop values:

```css
--norm-content-max: 1240px;
--norm-content-laptop: 875px;
--norm-content-min: 640px;
--norm-surface-radius: 24px;
--norm-card-radius: 16px;
--norm-space-1: 8px;
--norm-space-2: 16px;
--norm-space-3: 24px;
--norm-space-4: 32px;
```

Use these as MVP HTML tokens, not as claims about the production design-token API.

## Page anatomy

1. Page title and meaningful count.
2. Optional contextual action or AI entry point.
3. Quick filters or attention zones.
4. Optional search and advanced filter control.
5. Main registry/dashboard/content.
6. Floating action dock when the scenario has a persistent next action.

## Density

- Default to compact but readable business density.
- Use 24px card padding on desktop and 16px on compact/mobile layouts.
- Use 16px between registry cards; reduce to 8px on mobile.
- Keep card metadata in aligned groups so a registry can be scanned vertically.
- Hide or collapse secondary fields on small screens instead of shrinking everything.

## Floating action dock

The bottom action dock is a signature NORM pattern. Use it when a primary action or AI/chat must remain available while the user explores a long surface.

- Float above content near the lower edge.
- Combine one primary contextual action with optional assistant/chat access.
- Use a rounded surface and restrained elevation.
- Do not cover important content; reserve bottom space.
- On narrow screens reduce the dock to essential actions.
- Do not use it when no persistent action exists.
