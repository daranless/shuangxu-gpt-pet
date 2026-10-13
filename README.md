# 霜序 · Shuangxu GPT Pet

白发浅紫龙娘动画宠物：九类动作、十六个视线方向，以及无需安装的离线预览页面。

仓库保存最终精灵表、GIF / MP4 预览、原始动作素材、生成提示词和验证记录，方便查看、研究精灵动画流程，以及在支持相同格式的 Pets 工具中使用。

![霜序完整动作预览](outputs/shuangxu-all-states.gif)

## 快速预览

1. 点击仓库的 **Code → Download ZIP**，下载并解压；也可以使用下面的 Git 命令。
2. 用 Edge、Chrome 或其他现代浏览器打开根目录的 `index.html`。
3. 点击动作按钮切换动画，用“方向”选择视线角度，或点击“视线循环”。

```bash
git clone https://github.com/daranless/shuangxu-gpt-pet.git
```

离线预览无需 Python、Node.js、API Key 或联网。保持 `index.html` 与 `outputs/` 的相对位置，移动时一起移动整个目录。GitHub 中的 HTML 文件显示源码，下载后在浏览器打开才能交互预览。

## 主要文件

| 文件或目录 | 用途 |
| --- | --- |
| [`index.html`](index.html) | 离线播放器，支持动作、暂停、显示尺寸与视线切换 |
| [`outputs/shuangxu-spritesheet.png`](outputs/shuangxu-spritesheet.png) | 最终 v2 透明 PNG 精灵表 |
| [`outputs/shuangxu-all-states.gif`](outputs/shuangxu-all-states.gif) / [MP4](outputs/shuangxu-all-states.mp4) | 完整九类动作展示 |
| `outputs/shuangxu-<动作名>.gif` | 每种动作的单独预览 |
| [`outputs/shuangxu-idle-jump-idle.gif`](outputs/shuangxu-idle-jump-idle.gif) | 待机、跳跃、落地的衔接 |
| [`outputs/shuangxu-look-loop.gif`](outputs/shuangxu-look-loop.gif) | 十六方向视线循环 |
| [`outputs/shuangxu-contact-sheet.png`](outputs/shuangxu-contact-sheet.png) / [方向检查图](outputs/shuangxu-directions.png) | 全帧与视线检查图 |
| [`outputs/shuangxu-quality-report.json`](outputs/shuangxu-quality-report.json) | 制作质量结果，包含保留的警告 |
| `work/shuangxu/references/` | 角色参考、布局引导和方向锚点 |
| `work/shuangxu/decoded/`、`prompts/`、`frames/`、`final/` | 原始动作条、提示词、提取帧和组装成品 |
| `work/shuangxu/qa/` | 逐帧、配准、透明边缘、方向与独立目视复核记录 |
| `tools/work-pets/` | 制作时使用的 Pets 工具脚本及说明副本 |
| `archive/` | 文件清单、哈希、公开版本整理说明和检查记录 |
| [`outputs/shuangxu-production-files.zip.parts/`](outputs/shuangxu-production-files.zip.parts/) | 制作 ZIP 的四个分块；对应素材已完整展开在 `work/` |

`draft`、`rejected`、`v1`、`v2` 等名称的文件保留制作过程，日常使用优先选择最终成品。`tools/` 中的技能说明是制作参考，不是浏览器运行所需组件。

制作 ZIP 超过上传连接器的单次通信大小上限，因此保留为四个二进制分块。需要 ZIP 时，在下载的仓库根目录执行 `python tools/join_production_archive.py`；脚本只使用 Python 标准库，校验每个分块后生成 `outputs/shuangxu-production-files.zip`。动画预览和展开的源文件不需要这一步。

## 精灵表规格

| 项目 | 数值 |
| --- | --- |
| 格式 | RGBA 透明 PNG，v2 |
| 整图尺寸 | 1536 × 2288 px |
| 网格 | 8 列 × 11 行 |
| 单格尺寸 | 192 × 208 px |
| 有效帧 | 73 帧 |
| 空白格 | 15 格，保持透明 |

每行动作从左侧第一格开始，未使用的格子保持透明：

| 行号，从 0 开始 | 状态 | 帧数 | 含义 |
| --- | --- | --- | --- |
| 0 | `idle` | 6 | 安静待机、呼吸和眨眼 |
| 1 | `running-right` | 8 | 向屏幕右侧移动 |
| 2 | `running-left` | 8 | 向屏幕左侧移动 |
| 3 | `waving` | 4 | 双手招呼 |
| 4 | `jumping` | 5 | 蓄力、起跳、腾空和落地 |
| 5 | `failed` | 8 | 受挫反应 |
| 6 | `waiting` | 6 | 等待输入 |
| 7 | `running` | 6 | 专注工作 / 思考，双脚站定 |
| 8 | `review` | 6 | 查看和复核结果 |
| 9 | 视线方向 A | 8 | 0° 到 157.5°，每步 22.5° |
| 10 | 视线方向 B | 8 | 180° 到 337.5°，每步 22.5° |

角度以屏幕坐标为准：**0° 向上、90° 向右、180° 向下、270° 向左**，顺时针排列。正常待机提供正面的休息姿态。

![十六方向视线预览](outputs/shuangxu-look-loop.gif)

## 在支持 v2 的 Pets 流程中使用

将 `outputs/shuangxu-spritesheet.png` 交给支持上述网格的 Pets 创建流程，先验证文件，再按工具步骤创建和选用。下载仓库会得到素材和播放器；应用内宠物身份、创建和选用状态属于各自账号。

请确认目标工具接受 **1536 × 2288** 的十一行格式。需要九行格式的工具不能直接使用这份 v2 文件，不要通过拉伸整图适配。

状态 JSON 是制作阶段的历史快照，不能代表下载者的安装状态。项目目前提供精灵动画与播放器；GPT 对话服务、语音、Live2D 骨骼和 VRM 模型需要单独实现。

## 验证与制作记录

最终 PNG 在制作时通过结构验证、质量检查、Pets MCP 上传前验证和独立目视检查。四个基本视线方向通过独立检查；部分中间角度变化较轻，报告保留了相关歧义与连续性警告。

最终 PNG 的 SHA-256：

```text
618aa7acd7e6a35b530a77902471d7f1d6204e91434b7f790aaa3437e5fe6a7c
```

只看动画无需运行制作脚本。如需复查结构，使用 Python 3.10+ 并安装 Pillow，然后在仓库根目录执行：

```bash
python -m pip install Pillow
python tools/work-pets/skills/create-pet/scripts/validate_atlas.py outputs/shuangxu-spritesheet.png --require-v2 --chroma-key "#00FF00" --json-out archive/validation-local.json
```

`work/normalize_*.py` 会改写提取帧，不应反复执行来“启动宠物”。`work/render_final_previews.py` 重新渲染时还需要 `ffmpeg` 在 PATH 中可用。生成新图像需要另行准备图像生成工具，Pillow 只负责已有像素处理。

## 素材来源与公开版本

仓库保留创建时选择的 [Apache 2.0 许可证](LICENSE)。角色根据提供的白发龙娘参考图，通过 AI 图像生成制作。参考图保存在 `work/shuangxu/references/reference-01.png`，原作者和授权信息未附在归档中；使用参考图及衍生角色时，请确认对应权利。工具副本来自制作时的 Pets 插件，第三方素材和工具的权利仍以其原始来源为准。

公开版本保留动画、源图、提示词和技术记录，移除了聊天原文、个人会话标识和本机绝对路径，并重新生成制作 ZIP。图片未重新绘制，最终精灵表哈希保持一致。整理记录见 [`archive/publication-copy.json`](archive/publication-copy.json)。

更多操作说明见 [`README-使用说明.md`](README-使用说明.md)。
