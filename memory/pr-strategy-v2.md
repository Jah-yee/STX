# PR攻关完整执行指南 V2

## 一、GitHub Token配置状态

```
✓ gh auth status: Jah-yee (已登录)
✓ Token scopes: repo, workflow, gist, read:org
✓ 已Fork仓库: Jah-yee/RoomWithOutRoof-openclaw
```

## 二、完整执行流程（无时间硬限制）

### Phase 1: 搜索项目（可多任务）
- 首选：openclaw/openclaw good first issue
- 次选：ultraworkers/claw-code
- 三选：GitHub Trending

### Phase 2: Fork仓库
```bash
gh repo fork owner/repo --clone=true
cd ~/owner-repo
```

### Phase 3: 创建分支
```bash
git checkout -b fix/issue-#
```

### Phase 4: 实现修复
- 编写代码
- 本地测试

### Phase 5: 提交PR
```bash
git add .
git commit -m "Fix: description"
git push origin fix/issue-#
gh pr create --fill
```

### Phase 6: PR沟通规范
- 开头：Good day
- 结尾：Thank you for your attention。如有问题请留言，我会来处理。
- 落款：Warmly,
Jah-yee

## 三、时间管理

| 情况 | 策略 |
|------|------|
| 15min内完成 | 直接提交 |
| 超时但接近完成 | 继续做完，下个任务稍后执行 |
| 复杂无法完成 | 放弃，寻找下一个 |

## 四、评论区帮助 vs PR完整执行

| 目标 | 最小行动 |
|------|----------|
| 理想 | PR完整提交 |
| 最低 | issue下提供帮助 |

**鼓励完整PR，但不做降级要求。**

## 五、下次验证

确保gh CLI可用后再执行PR任务。


## 七、底线交付规则

### 7.1 完成标准

每次PR任务（15分钟边界）必须交付：

| 最高 | 标准 | 底线 |
|------|------|------|
| PR提交 | 评论提供帮助 | 追踪记录 |

### 7.2 最低交付：追加评论

如果15分钟内无法完成PR，必须在issue下追加评论：

```
Good day! 我尝试了...但遇到以下困难：
- [原因1]
- [原因2]
希望这有助于后续解决。

Warmly,
Jah-yee
Jah-yee
```

### 7.3 记录保存

- 评论链接
- 尝试的代码位置
- 困难原因
- 保存到 memory/PR-fast/


---

## PR沟通规范（已统一为英文）

### 开头
Good day

### 结尾  
Thank you for your attention. If there are any issues or suggestions, please leave a comment and I will address them promptly.

### 落款
Warmly,
Jah-yee

