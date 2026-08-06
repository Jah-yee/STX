# Issue #16815 - Open Dashboard to the Side

## Status: ✅ PR Created

**PR:** https://github.com/microsoft/aspire/pull/17864
**Branch:** `fix/issue-16815-open-dashboard-to-side` on fork `Jah-yee/aspire`

## Changes Made

### 1. `extension/package.json`
- Added `aspire-vscode.openDashboardToSide` command definition (icon: globe)
- Added to commandPalette (same condition as openDashboard)
- Added to view/item/context with "inline" group, alongside openDashboard

### 2. `extension/package.nls.json`
- Added `"command.openDashboardToSide": "Open Aspire Dashboard to the Side"`

### 3. `extension/src/extension.ts`
- Registered command: `registerInstrumentedCommand('aspire-vscode.openDashboardToSide', 'tree', (element) => appHostTreeProvider.openDashboardToSide(element))`
- Added registration to context.subscriptions

### 4. `extension/src/views/AspireAppHostTreeProvider.ts`
- Implemented `openDashboardToSide(element?: TreeElement): Promise<void>`
- Uses `simpleBrowser.api.open` with `ViewColumn.Beside` to open in VS Code side panel
- Same URL resolution logic as `openDashboard` (AppHostItem, WorkspaceResourcesItem, etc.)

## Technical Notes
- Used `simpleBrowser.api.open` (from VS Code's simple-browser extension API) instead of `simpleBrowser.show` directly
- This is the same API used by the debugger's integrated browser feature
- ViewColumn.Beside opens the dashboard in the adjacent editor group (side-by-side)
- preserveFocus: true keeps focus in the current editor while dashboard opens

## GitHub Identity Used
- Author: Jah-yee <jydu_seven@users.noreply.github.com> (noreply email to bypass GH007 privacy blocking)

## Notes
- No tests were added (existing test coverage for openDashboard does not test browser behavior, just the quick pick logic)
- PR targets `main` branch
- 100+ open PRs in microsoft/aspire (many release hotfixes) - competition is low for a straightforward feature PR
