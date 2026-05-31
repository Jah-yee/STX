# last30days Skill配置

## Skill信息
- **GitHub**: mvanhorn/last30days-skill
- **功能**: 深度研究引擎，覆盖Reddit、X、YouTube、HackerNews、Polymarket等10+来源
- **已克隆**: ~/.openclaw/workspace/skills/last30days

## 配置

创建配置文件：
```bash
mkdir -p ~/.config/last30days
cat > ~/.config/last30days/.env
INCLUDE_SOURCES=reddit,hackernews,polymarket
```

## 使用方法

```bash
# 快速研究
python3 scripts/last30days.py "AI coding" --emit=compact --quick

# 深度研究
python3 scripts/last30days.py "AI coding" --emit=compact --deep
```

## 场景配置

| 任务 | 使用Skill | 频率 |
|------|-----------|------|
| 深度调研 | last30days | 按需 |
| 趋势分析 | last30days | 每日/每周 |

## 限制/问题

- Reddit API需要认证，当前返回403
- X(Twitter)需要AUTH_TOKEN
- 可以解锁更多源

