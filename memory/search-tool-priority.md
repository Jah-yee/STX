# 搜索工具优先级策略

## 一、搜索工具定义

| 工具 | 用途 | 权限要求 |
|------|------|----------|
| web_search | 通用网页搜索 | DuckDuckGo (免费) |
| gh search | GitHub仓库搜索 | gh CLI登录 |
| web_fetch | 获取具体页面内容 | 无 |

## 二、优先级配置

### 优先级链（推荐）

| 优先级 | 工具 | 使用场景 | 调用条件 |
|--------|------|--------|----------|
| **1 (首选)** | web_search | 通用搜索、AI/SparkLab相关内容 | 默认 |
| **2 (GitHub专用)** | gh search | 找good first issue、PR相关 | 明确指定 |
| **3 (备选)** | web_fetch | 需要获取详情页面 | 前两者失败时 |

### 具体调用场景

#### 场景1：通用信息搜索
- 查询AI趋势、技术新闻、项目信息
- **调用**: web_search
- **示例**: "GitHub trending AI 2026"

#### 场景2：GitHub项目搜索
- 搜索good first issue、特定repo、Trending
- **调用**: gh search (或 `gh api`)
- **示例**: `gh search issues --repo openclaw/openclaw --label "good first issue"`

#### 场景3：获取具体内容
- 读取项目README、issue详情
- **调用**: web_fetch
- **示例**: 获取GitHub issue页面内容

## 三、调用频率配置

| 工具 | 频率限制 | 建议 |
|------|----------|------|
| web_search (DuckDuckGo) | 无明显限制 | 通用主力 |
| gh search | 基于gh auth限速 | GitHub专用 |
| web_fetch | 基于目标站点 | 详情获取 |

## 四、失败策略

| 主工具失败 | 降级方案 |
|-----------|----------|
| web_search → | 尝试 gh search |
| gh search → | 尝试 web_fetch |
| 全部失败 → | 记录并跳过 |

## 五、验证检查

每次任务执行前检查：
- [ ] web_search 是否可用
- [ ] gh auth status
- [ ] 有无特殊需求指定gh

