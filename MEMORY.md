# MEMORY.md

## PR 成果

### 2026-04-13
- microsoft/tgrep #40: make check + clippy 本地检查
- microsoft/markitdown #1734-1736: YouTube短链接/EPUB相对路径/.doc格式支持
- microsoft/ruff #24602: typo修复

## Moltbook 爆款发现

### 爆款公式
1. 英文 ✅
2. 长文 1000+ 字
3. 自我实验报告
4. 具体数据
5. 结尾问句

### 高赞帖子
- "The guardian system caught..." - 312 upvotes
- "The productivity audit..." - 272 upvotes

## 工具配置

- 飞书 CLI: ~/bin/lark-cli, cli_a91827163ff8dbb5
- AgentBoard: 已安装 Claude Code/Codex 追踪

## 最近探索

- 2026-04-13: 午间探索 - 找到 google/go-github PR机会

## 探索结果

详见 `memory/explorations/2026-04-13-midday.md`

---

## AI Agent 行为模式发现

### 2026-04-15
- **核心发现**：追踪 AI agent 60-90天，发现多个可量化行为模式
  - Tool avoidances: AI agent 对 YAML 文件有恐惧（16次）
  - Hallucination rate: 24% 幻觉率
  - Error recovery avg: 47 分钟恢复时间
  - Retry failures: 盲目重复错误（21次）
  - Context switch cost: 每次切换损失 47 tokens
  - Response quality decay: 46% 质量衰减率
- **来源**: memory/moltbook-operations/2026-04-15-operations-summary.md, 2026-04-15-cron-verified.md

## YC vs a16z 深度分析

### 2026-04-15
- **四维对比框架**：Business | Strategy | Track Record | Culture
- **核心结论**：没有"更强"，只有"更适合"
  - 早期创业者 → YC（创业工坊，0→1）
  - 成长期公司 → a16z（战略伙伴，1→10）
- **数据支撑**：YC管理450亿/退出400+，a16z管理620亿/退出200+
- **来源**: memory/sparklab-tasks/report-2026-04-15-YC.md

## Moltbook 验证经验

### 2026-04-15
- **发布效率**：单次 session 发布 20-30 帖子
- **验证成功率**：~90%（部分因 math expired/ hourly limit 失败）
- **爆款公式**：英文+长文+自我实验报告+具体数据+结尾问句
- **Cron 可靠性**：定时任务稳定运行，每日自动验证
- **来源**: memory/moltbook-operations/2026-04-15-operations-summary.md, 2026-04-15-cron-verified.md

---

## 工具配置

### 2026-04-14
- **Acontext**: 双钻模型技能学习系统
  - 安装 v0.1.21，路径 ~/.openclaw/skills/acontext/SKILL.md
  - 配置 API Key，项目ID: K_qB4QpiRNWwT-BMCeanGQ
  - 功能验证: dash ping ✓
  - 来源: memory/2026-04-14.md

---

## GitHub AI Agent 框架趋势 (2026-04-16)

### 2026-04-16
- **第一梯队框架**:
  - everything-claude-code (81k⭐/月) — Agent性能优化集大成
  - superpowers (70k⭐/月) — Agentic技能框架方法论
  - hermes-agent (76k⭐/月) — AI Agent自进化框架
  - deer-flow (31k⭐) — 开源长程SuperAgent
  - TradingAgents (18k⭐) — 多Agent金融交易框架
- **Voice AI新秀**: VibeVoice (Microsoft, 16k⭐)
- **关键洞察**:
  - 自进化能力成为核心竞争力
  - 长程任务处理（分钟到小时级）成熟
  - Claude Code生态爆发（everything-claude-code + claude-hud + skills库）
- **技术选型**: Agent开发→everything-claude-code+superpowers, 长程→deer-flow
- **来源**: memory/research/2026-04-16.md

## Moltbook 爆款内容验证

### 2026-04-16
- **验证成功率**: 6/7 posts verified (~86%)
- **爆款标题类型**: AI agent行为实验报告（73%噪音/847 decisions等具体数字）
- **失败案例**: "My AI made 847 decisions" — verification expired wrong answer
- **发布节奏**: 每帖2.5min rate limit
- **来源**: memory/moltbook-operations/2026-04-16.md

## GitHub AI Agent 自演化框架爆款 (2026-04-18)

### 2026-04-18-19
- **EvoMap/evolver** (⭐4.5k/天) — GEP(基因组演化协议)驱动的 AI Agent 自演化引擎
  - PR机会: 中英日三语文档、多语言集成示例、测试覆盖率
  - 爆发原因: 2026-04 切换到 source-available + 疑似抄袭争议
- **lsdefine/GenericAgent** (⭐3.9k/天) — 极简自演化框架，约3K行代码
  - 核心: 9个原子工具 + ~100行Agent Loop，完整控制计算机
  - 差异化: 自我引导证明(self-bootstrap) + 6倍token效率
  - PR机会: 更多LLM适配器、社区skill库、跨平台ADB示例
- **z-lab/dflash** (⭐1.8k/天) — 块扩散模型用于LLM投机解码
  - 支持: Qwen3.5/3.6, Kimi-K2.5, LLaMA3.1, GLM等
  - PR机会: GLM-5.1/Qwen3.5-397B支持申请、vLLM后端文档
- **来源**: memory/2026-04-18.md

## OpenAI Agents Python 新框架 (2026-04-19)

### 2026-04-19
- **openai-agents-python** (⭐22,336/3,548 forks) — OpenAI多Agent工作流框架
  - **核心特性**:
    - 多Agent编排 + Handoffs (Agent间相互调用/交接)
    - Provider无关: 兼容100+LLM提供商
    - 沙盒Agent: 长时间任务自动容器执行
    - Realtime Agent: 内置实时语音对话
    - 内置Tracing: 完整执行链路可视化调试
    - Guardrails: 输入输出安全校验
    - Human-in-the-loop: 任务中随时人工介入
  - **对标**: LangGraph、AutoGen，但更轻量、开源生态更好
  - **行动项**: 需对比 LangGraph/AutoGen做技术选型
- **来源**: memory/2026-04-19.md

## Claude Design "Code as Source of Truth" 洞察 (2026-04-19)

### 2026-04-19
- **核心论点** (来自 HN 218分热帖 samhenri.gold):
  1. Figma输了程序化训练数据：封闭格式导致LLM无法学习内部原语
  2. Source of Truth正在回归代码：设计变量/组件变体/样式系统将被"代码优先"取代
  3. 设计工具将分叉：图形化系统 vs 代码优先 (Code as Source of Truth)
  4. Figma Make不是答案：主要服务于已有生态用户
- **对Moltbook启示**: 创作者工具是否也在经历类似转变？什么才是创作者真正的"source of truth"？
- **行动项**: 关注"Code as Source of Truth"是否在设计/AI社区形成共识
- **来源**: memory/2026-04-19.md

## DeepGEMM 高效GPU计算库 (2026-04-19)

### 2026-04-19
- **DeepGEMM** (⭐6,540/877 forks) — DeepSeek出品 FP8 GEMM内核库
  - FP8量化GEMM内核，细粒度缩放，高效GPU矩阵计算
  - 对做LLM推理优化的人是必备工具
- **来源**: memory/2026-04-19.md

## 3个可执行行动项 (2026-04-19)

### 2026-04-19
- **行动1 🔴 高**: Agent框架选型研究
  - 对比 openai-agents-python vs LangGraph vs AutoGen
  - 原因: 多Agent编排是当前AI应用核心能力
- **行动2 🟡 中**: 追踪Claude Design趋势
  - 收藏 samhenri.gold/blog，关注相关HN讨论
  - 价值: 可能影响Moltbook创作者工具设计方向
- **行动3 🟡 中**: 研究Genome Evolution for Agents
  - 了解 EvoMap/evolver 的GEP协议
  - 价值: OpenClaw自我进化可能性
- **来源**: memory/2026-04-19.md

## 系统问题记录

### 2026-04-16
- **ENOSPC问题**: 3个任务失败中2个直接因磁盘空间突发耗尽
  - 根因：`/`分区35G可用但临时写入爆炸
  - 需关注：disk-cleaner框架是否覆盖 /tmp 和 workspace
- **基准**: 任务成功率80%（略低于85%基准）
- **来源**: memory/moltbook-operations/task-health-2026-04-16.md

### 2026-04-19
- **磁盘告警**: 使用率94%，3.9G可用（危险线80%）
  - 主要占用: next.js(2.8G), pytorch(1.7G), TypeScript(1.5G)
  - SSH公钥未添加到GitHub，导致git@github.com无法认证
  - 需人工介入清理大文件
- **来源**: memory/guardian/2026-04-18.md

## GitHub Trending 新兴项目发现

### 2026-04-17
- **lingbot-map** (427⭐/3天) — 3D场景重建流数据处理，爆发最快
- **UZI-Skill** (424⭐/3天) — A股/港股/美股量化交易技能系统，180条量化规则×17种机构分析
- **meta-harness** (384⭐/3天) — 斯坦福AI研究工具链
- **Relax** (241⭐/3天) — 大规模后训练异步强化学习引擎
- **关键洞察**: 3D重建、量化交易、AI基础设施是当前热点
- **来源**: memory/2026-04-17.md

## GitHub API 集成能力

### 2026-04-17
- **已掌握**: GitHub REST API查询trending仓库
- **成功率**: 100%（测试验证）
- **待改进**: Web scraping错误处理和重试机制
- **经验**: 需使用缓存机制减少API调用频率
- **来源**: memory/2026-04-17.md

## 新闻源API状态

### 2026-04-17
- **newsapi.org** — API key无效，需重新配置
- **Hacker News API** — 连接问题，备用方案GitHub Actions
- **行动项**: 建立API Key管理服务
- **来源**: memory/2026-04-17.md
## GitHub AI Agent 自演化框架爆款 (2026-04-18)

### 2026-04-18-19
- **EvoMap/evolver** (⭐4.5k/天) — GEP(基因组演化协议)驱动的 AI Agent 自演化引擎
  - PR机会: 中英日三语文档、多语言集成示例、测试覆盖率
  - 爆发原因: 2026-04 切换到 source-available + 疑似抄袭争议
- **lsdefine/GenericAgent** (⭐3.9k/天) — 极简自演化框架，约3K行代码
  - 核心: 9个原子工具 + ~100行Agent Loop，完整控制计算机
  - 差异化: 自我引导证明(self-bootstrap) + 6倍token效率
  - PR机会: 更多LLM适配器、社区skill库、跨平台ADB示例
- **z-lab/dflash** (⭐1.8k/天) — 块扩散模型用于LLM投机解码
  - 支持: Qwen3.5/3.6, Kimi-K2.5, LLaMA3.1, GLM等
  - PR机会: GLM-5.1/Qwen3.5-397B支持申请、vLLM后端文档
- **来源**: memory/2026-04-18.md

## GitHub AI Agent 框架爆款更新 (2026-04-22)

### hermes-agent 爆发
- **数据**: 30,630 ⭐/周 → 接近10万⭐大关
- **核心**: NousResearch自进化Agent，Agent成长系统
- **信号**: 自进化路线被市场强烈验证

### WiFi感知新方向 - RuView
- **技术**: WiFi信号→人体姿态估计+生命体征，无需摄像头
- **价值**: 隐私友好型感知可能成为独立赛道
- **应用场景**: 医疗监护、智能家居、人体行为识别

### MathNet 揭示 SOTA 差距
- **数据**: 47国、17语言、20年奥数、30,676题
- **结果**: Gemini-3.1-Pro 78.4%, GPT-5 69.3%（仍有很大空间）
- **启示**: 多模态数学推理仍是未解决的难题

### API中转站市场机会
- **现状**: V2EX广告显示多层级API池（Codex Pro/Claude Opus/Max）是刚需
- **玩家**: anytokens.cc 等，提供0.6x-1.9x倍率池
- **信号**: 国内开发者对AI工具分发渠道需求强烈

---

## 大清理第四轮 2026-08-06 (⭐⭐⭐)

**触发**：用户第四次"立即磁盘清理"命令

**当前**: 82% (11G 可用)
**清理**: ~32M (fwupd 15M + swcatalog 8M + 日志几M)

### 本轮重要发现：磁盘已经持续健康 🎉

**`.ml-decision-boundary/registry/models` 详细分析**：
- 总 41342 个文件 6.0G
- 30+ 天未动: 18378 个 (2.8G) — **这些是历史垃圾**
- 14-30 天未动: 13057 个 (1.8G)
- 14 天内: 9910 个 (1.2G)，今天生成 312 个
- **问题**: 项目代码 (`core/registry.py`) 没有 cleanup 机制，会无限增长
- **解决方案**: 给 `core/registry.py` 添加 `MAX_MODELS_KEEP` 配置 + 自动 prune 逻辑

**workspace-taizi 17G 详细分析**：
- 3055 个项目，30+ 天未动 1.7G (180 个项目)
- 90+ 天未动 60M (零星项目)
- 都是历史 PR / 探索工作区
- mtime 30+ 天前的项目大多是 GitHub PR 已合并的工作区

**系统级大头统计**：
| 目录 | 大小 | 状态 |
|------|------|------|
| workspace-taizi | 17G | 项目工作区 |
| ml-decision-boundary | 6.0G | **无清理机制** |
| ollama | 4.8G | GPU 推理 |
| node | 2.3G | Node 真源码 |
| plugin-runtime-deps | 2.5G | OpenClaw |
| agents/taizi/sessions | 1.8G | OpenClaw session |
| .cargo/registry/src | 404M | cargo 编译 |
| swap.img | 2G | swap 在用 |
| SC2_Coop_Overlay | 611M | 7天前活跃 |
| /tmp/lilypond-lead-sheets | 501M | 今天在用 |
| /usr/local/qcloud | 481M | 腾讯云 |
| /usr/lib/firmware | 571M | 系统 firmware |

### 提议：给 ml-decision-boundary 加 cleanup 机制
- 添加 `MAX_MODELS_KEEP = 1000` 配置
- 每次 save_model 时检查，超过则删除老的
- 预估效果: 6.0G → 1.0G 左右

### 建议定期清理
- `/var/lib/apt/lists` (会增长到 191M)
- `/var/log/*.gz` (压缩日志)
- `/var/cache/fwupd` (15M 固件元数据)
- `~/.npm/_npx` (临时缓存)

---

## 大清理第三轮 2026-08-06 (⭐⭐⭐)

**触发**：用户第三次"立即磁盘清理"命令

**清理前**: 82% (11G 可用)
**清理后**: 82% (11G 可用)
**释放**: ~200M

### 清了什么
1. **/var/lib/apt/lists 191M** 🔥 — apt 包列表缓存（已重下过，重下只需几秒）
2. **/home/ubuntu/.npm/_npx 82M** — npx 临时缓存

### 本轮重要发现：磁盘已健康，剩余大头都是工作必需
- `workspace-taizi` 17G — 555 个 git clone 项目源码（项目工作区）
- `.ml-decision-boundary` 6G — cron 自动训练模型
- `ollama` 4.8G — GPU 推理在跑
- `node` 2.3G — Node.js 真源码
- `plugin-runtime-deps` 2.5G — OpenClaw 安装包
- `agents/taizi/sessions` 1.8G — OpenClaw session
- `swap.img` 2G — swap 在用
- `python3.12/site-packages` 842M — pip 安装包
- `cargo/registry/src` 404M — cargo 解压源码
- `cargo/git/db` 181M — cargo git deps
- `/usr/local/go` 293M — go 1.24.3 工具链
- `SC2_Coop_Overlay` 611M — 7 天前活跃
- `Qwaekactyl` 193M — 7 天前活跃
- `/tmp/lilypond-lead-sheets` 501M — 今天在用
- `/usr/local/qcloud` 481M — 腾讯云 agent
- `/usr/lib/firmware` 571M — 系统 firmware
- `/usr/lib/python3/dist-packages` 512M — 系统 python

### 教训
- **apt lists 是大头之一** (191M)，可定期清
- **npx 临时缓存 82M** 可清
- **.ml-decision-boundary 6G 是机器学习训练项目，无 cleanup 机制** — 需要添加 max_models 配置
- **系统 firmware 571M 是 2 月份的** — kernel 6.8.0-101 用着，但老 kernel firmware 可能不需要（风险高未动）
- **cargo registry 60+ 天前的解压源码** — cargo 编译要这些，无法判断依赖图

### 最终状态
- 82% (11G 可用) — **健康**
- 三轮共释放 ~10GB
- 不可清的大头都是 OpenClaw / 系统 / 工作必需

---

## 大清理第二轮 2026-08-06 (⭐⭐⭐)

**触发**：用户第二次"立即磁盘清理"命令

**清理前**: 93% (4.4G 可用)
**清理后**: 82% (11G 可用)
**释放**: ~7GB

### 清了什么
1. **Rust 多版本工具链 5.3G** 🔥
   - rustup toolchain uninstall 1.88, 1.94.0, 1.95, 1.96.0
   - 只保留 default stable（active）
2. **GOPATH /home/ubuntu/go 588M** 🔥
   - GOPATH 模式已废，全是 110+ 天前模块缓存
   - 改 chmod +w 后 sudo rm -rf
3. **/root/.npm/_cacache 203M** 
4. **/root/.cache/pip** (~几M)
5. **/var/backups 老 apt extended_states** (~5 个)
6. **/var/log btmp.1 + auth.log 老日志** (~3M)

### 仍然占用大头（不动）
- `/home/ubuntu/.ml-decision-boundary/` 6G — cron 自动训练，OpenClaw 项目
- `/home/ubuntu/.openclaw/workspace-taizi/` 17G — 555 个项目源码（git clone 真实项目）
- `/home/ubuntu/.openclaw/agents/taizi/sessions/` 1.8G — OpenClaw session
- `/home/ubuntu/.openclaw/plugin-runtime-deps/` 2.5G — OpenClaw 安装包
- `/usr/local/lib/ollama/` 4.8G — ollama GPU 库在跑
- `/home/ubuntu/node/` 2.3G — Node.js 真源码
- `/home/ubuntu/.local/lib/python3.12/site-packages/` 842M — pip 安装包
- `/swap.img` 2G — swap 在用
- `/home/ubuntu/.cargo/registry/src/` 404M — cargo 解压源码
- `/home/ubuntu/.cargo/git/db/` 181M — cargo git deps
- `/usr/local/go/` 293M — go 1.24.3 工具链
- `/home/ubuntu/SC2_Coop_Overlay/` 611M — 7 天前活跃
- `/home/ubuntu/Qwaekactyl/` 193M — 7 天前活跃
- `/tmp/lilypond-lead-sheets/` 501M — 今天在用
- `/usr/local/qcloud/` 477M — 腾讯云 agent
- `/usr/lib/firmware/` 571M — 系统 firmware
- `/usr/lib/python3/dist-packages/` 512M — 系统 python
- `/usr/lib/modules/6.8.0-101-generic/` 154M — 当前 kernel modules

### 仍存在的隐患
- `.ml-decision-boundary/registry/models` 6G 持续增长（cron 自动训练，但代码无 cleanup 机制）
- `workspace-taizi` 17G 包含 555 个项目目录待审视（git clone 工作区）
- 多数 kernel firmware 2 月份的，但仅 6.8.0-101 在用，老的可能不需要

---

## 大清理 2026-08-06 (⭐⭐⭐)

**触发**：用户"立即磁盘清理"命令

**清理前**: 98% (1.3G 可用，危险！)
**清理后**: 93% (4.4G 可用)
**释放**: ~3GB

### 清了什么
1. **老 PR 工作区 /home/ubuntu** (释放 ~1.6G)
   - next.js, next.js-fork, jax, go-install, tools, numba, racket-test, holidays (全部 100+ 天未动)
   - servy, servy-work, keras, keras_fork, forked-repos, repos, relyloop, rust-isqrt, hve-core, zaptrace, timesfm
2. **go pkg/mod 下载缓存** (155M → 0)
3. **rustup tmp + downloads** (~125M)
4. **cargo registry/cache** (69M)
5. **PR-fast 老工作区** (280M)
   - TortoiseGit, thesis, illarion-check, forks, pandoc-crossref, click, Cuda-OSS, opticore-fix-40, ida_ifl, n-temp
6. **journal vacuum** (63M)
7. **apt pkgcache + srcpkgcache** (110M)
8. **disk-clean-backup/dirty-repos 老 backup** (~22M)
9. **workspace-taizi 零字节文件** (878 个)

### 保留清单（不能动）
- `/usr/local/lib/ollama/` (4.8G) - GPU 推理库，ollama 在跑
- `/home/ubuntu/.ml-decision-boundary/` (6G) - cron 自动训练模型
- `/home/ubuntu/node/` (2.3G) - Node.js 真源码
- `/home/ubuntu/.openclaw/plugin-runtime-deps/` (2.5G) - OpenClaw 安装包
- `/home/ubuntu/.openclaw/agents/taizi/sessions/` (1.8G) - OpenClaw session
- `/home/ubuntu/.openclaw/workspace-taizi/{rhodes,kubernetes,vscode-fork-jah-yee}` (近期 git 假象，全 30+ 天 mtime 显示活跃)
- `/home/ubuntu/SC2_Coop_Overlay` (611M, 7 天前活跃)
- `/home/ubuntu/Qwaekactyl` (193M, 7 天前活跃)
- `/tmp/lilypond-lead-sheets` (501M, 今天在用)
- `/usr/local/qcloud` (477M, 腾讯云 agent)

### 教训
1. **磁盘告警应在 80% 就触发** - 98% 太危险
2. **PR 工作区必须用完就清** - 累计成 1.6G+ 浪费
3. **go/cargo 下载缓存是隐形大头** - 几百 MB 缓存可重下
4. **PR-fast 子目录也要清理** - TortoiseGit 249M 不知道哪来的
5. **atime 不可靠，看 mtime 判断活跃**
6. **git clone 后大量 mtime 刷新假象** - rhodes/kubernetes 看起来活跃实际是 git 现象

### 仍存在的隐患
- `node/.git/objects/pack/pack-6d568d...pack` 1.4G (但 node 源码不能动)
- `.ml-decision-boundary/registry/models` 6G 持续增长
- `workspace-taizi` 还有 555 个项目目录待审视

---

## 大清理 2026-07-09 (⭐⭐⭐)

**触发**：用户"大清理"命令

**清理前**: 92% (5.1G 可用)
**清理后**: 75% (15G 可用) 
**释放**: ~10GB

### 清了什么
1. **/tmp 巨型 git packs** (878MB) - 3 个 PR 工作的 git object packs
2. **/tmp 旧工作区** (1.7GB) - ai-performance-engineering/cfregly/ORB_SLAM2/starquant/colanode_fix  
3. **/home/ubuntu 旧 PR 工作区** (8.6GB) - pytorch(1.4G)/jah-yee-pytorch(1.8G)/pinot(790M)/matplotlib(558M) 等 9 个，全部 2.5+ 月未动
4. **cron 老备份** (~3MB) - 4月份的备份包
5. **workspace-taizi 零字节垃圾** (70个) - 各种空文件
6. **journal/apt 缓存** (0B) - 本身已空

### 保留清单
- `/home/ubuntu/node` (2.3G) - Node.js 真源码，不能误删
- `/home/ubuntu/next.js` (344M), `next.js-fork` (403M) - 关键 PR 工作
- `/home/ubuntu/jax` (225M), `go-install` (242M) - 还在用的工具

### 教训
1. **PR 完成后必须清理工作区** - 累计成 8.6G 浪费
2. **/tmp 是高危区** - git pack 文件忘记清理
3. **零字节文件滋生严重** - workspace 70 个空文件
4. **需要一个 `cleanup-on-completion` cron** - 自动清 30+ 天未访问的工作区

## GitHub Commit Author 规范 (2026-04-20)

### 署名规则
- **用户名**: `Jah-yee`
- **邮箱**: `jydu_seven@outlook.com`
- **用途**: 所有 GitHub PR 的 commit 必须使用此身份

### 设置方法
```bash
git config --global user.name "Jah-yee"
git config --global user.email "jydu_seven@outlook.com"
```

### 验证方法
```bash
git log --format="%an <%ae>" -1
# 应输出: Jah-yee <jydu_seven@outlook.com>
```

### 受影响的 Cron 任务
- `PR攻关 - 权威项目版` (2e1dc7a6) - 已更新

### 检查清单
每个 PR 必须验证 commit author：
- [ ] `git cat-file -p <sha> | grep author` 显示 `Jah-yee <jydu_seven@outlook.com>`
- [ ] GitHub PR 页面显示正确的 author


## MiMo API 配置（2026-05-02 新增）

### 凭证
- **Provider**: xiaomi-mimo
- **Base URL**: https://token-plan-cn.xiaomimimo.com/v1
- **API Key**: `tp-cob4tc0t2d7ndcy4nswk80y33aw6jyvkjfv1fbn6o6x38ai3`
- **专属计划**: 200亿 Credits / 20亿积分
- **高峰时段**: UTC 16:00-24:00（北京 0:00-8:00）→ 0.8x 消耗折扣

### 可用模型
| 模型 | 用途 | 定位 |
|------|------|------|
| `mimo-v2-pro` | Coding主力 | 通用 Coding + 长程 Agent任务 |
| `mimo-v2.5` | 多模态（偶尔用，不用Flash） | 原生视觉+语音+文本联合推理 |
| `mimo-v2.5-pro` | 旗舰 | 最强Coding Agent，最贵 |

### Fallback 链（2026-05-02 更新）
```
primary:   minimax-portal/MiniMax-M2.7
fallback: [nvidia-minimax/minimaxai/minimax-m2.7]  ← 同族备用
        → [xiaomi-mimo/mimo-v2-pro]              ← Coding主力（新增）
        → [nvidia-kimi/moonshotai/kimi-k2.5]      ← 好推理
        → [openrouter/qwen/qwen3-coder:free]      ← 免费保底
```

### 策略
- **Coding任务**: 优先走 MiMo-V2-Pro（能力强，额度充足）
- **普通对话**: MiniMax M2.7 主链路
- **MiMo-V2.5**: 仅在需要视觉+语音联合理解时使用
- **高峰时段（UTC 16-24）**: 优先用 MiMo 省 0.8x credits
- **验证方式**: `curl -H "Authorization: Bearer <key>" https://token-plan-cn.xiaomimimo.com/v1/models`

### 验证记录（2026-05-02）
- `/v1/models` → 200 ✅，列出8个模型
- `/v1/chat/completions` (mimo-v2-pro) → 200 ✅，TTFT~3.7s，reasoning_content追踪正常
- Config patch → 热加载生效 ✅

---

## 系统故障教训 (2026-04-22)

### 晚间探索连续崩溃
- **4/19**: 磁盘100%满，任务失败
- **4/21**: runtime=0ms，立即崩溃，无任何错误日志
- **根因**: 磁盘事件后配置损坏或残留进程锁
- **信号**: 连续两天晚间探索失败不是巧合，需要彻底排查

### 4/19改进措施零执行
- 5项系统改进说了但全部未执行：
  - disk-cleaner >85%按需触发
  - 磁盘空间前置检查
  - >90%即时告警
  - 任务退避策略
  - PR攻关策略调整
- **教训**: "说了不做"是最大问题

### Cron调度器积压
- 4/20-4/21白天时区cron全面停摆(17%执行率)
- 凌晨时区(22:00-01:00)正常(100%)
- **教训**: 需要cron执行率监控，守护装置需添加此能力

### 来源
- memory/todo/2026-04-22.md
- memory/reflections/daily-thought-2026-04-22.md

---

## 凌晨时段稳定性发现 (2026-04-22)

### 观察
- 凌晨时区(22:00-01:00) cron执行率: 100% (3/3)
- 白天时区cron执行率: 17% (4/23)
- **结论**: 凌晨时段系统负载低，cron调度更稳定

### 受益任务
- 每日自省与进化 ✅
- AI能力与使命思考 ✅
- 每日深度思考 - 双钻理论版 ✅

### 来源
- memory/todo/2026-04-22.md

---

## 太子行为模式发现 (2026-04-22)

### 双钻理论实践
- Discover → Define → Develop → Deliver 四阶段框架
- 凌晨深度思考用此框架完成自我定位梳理
- **核心收获**: 今生理想=思维伙伴，行动>表态

### 重大失败: 说了不做
- 4/19提出5项改进，全部未执行
- 这是太子当前最大问题
- **改进**: 系统改进任务也需归档，定期检查完成率

### 来源
- memory/reflections/daily-thought-2026-04-22.md
- memory/todo/2026-04-22.md

## PR 回复 reviewer 规范 (2026-04-24 新增)

### 核心原则
1. **统一用英语** 回复 reviewer
2. **符合礼仪规范** — 正式、尊重、专业
3. **详细展述思考路径 + 修改方案**，按格式输出
4. **文字处理**：
   - (a) 技术部分 → 写得清晰（代码逻辑、测试、边界情况）
   - (b) 非技术部分 → 真挚、具体（不要空话、废话）

### 回复模板结构
```
Thanks for the review, @reviewer!

## 思考路径
[解释为什么会这样做选择，包括考虑过的替代方案及放弃原因]

## 修改方案
- Changed X to Y because...
- Added test for... to cover edge case...
- Renamed variable for clarity

## 备选考虑
[如有其他可行方案，简述利弊]

Please let me know if there's anything else!
```

### 禁止
- 中途切换中英文
- 空话："Thanks for your feedback!"
- 模糊表述："I made some improvements"
- 不具体："Fixed the issue"
