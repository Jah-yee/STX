# PR攻关 - Issue #56948 分析

## 问题
`openclaw browser` 子命令在 v2026.3.28 丢失

## 分析过程

### Phase 1: 搜索Good First Issue
- 找到 issue #56948: browser子命令丢失
- 这是regression bug

### Phase 2: 代码考古

**关键发现**:
1. 浏览器扩展从 `src/browser/` 迁移到 `extensions/browser/` (commit 8eeb7f0829)
2. 迁移涉及大量文件重组 (~700 lines changed)
3. manifest配置: `enabledByDefault: true`
4. CLI注册正确: `api.registerCli(({ program }) => registerBrowserCli(program), { commands: ["browser"] });`

**关键变更 (v2026.3.24 -> v2026.3.28)**:
- `extbrowser/index.ts` 新增，导出BrowserPlugin
- `extensions/browser/openclaw.plugin.json` 新增
- 大量browser代码重组到 `extensions/browser/src/`

### Phase 3: 根因分析

**不是简单代码回退问题，原因**:
1. Browser extension代码完整存在
2. manifest配置正确
3. CLI注册逻辑正确
4. 找不到明显的regression代码

**可能是环境问题**:
- bundled plugin discovery
- OPENCLAW_BUNDLED_PLUGINS_DIR 环境变量
- 运行时插件加载顺序

## 结论

- 花费约15分钟深入分析
- 这是复杂的regression bug，需要live环境调试
- 代码本身没有明显问题，可能是bundled plugin discovery或环境配置问题

## 时间
2026-04-05 00:54 UTC