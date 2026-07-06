---
name: tradingagents
description: "Use when running multi-agent LLM-powered financial trading analysis — analyze stocks/crypto with specialized AI analysts (fundamental, sentiment, news, technical) and get trading signals."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [trading, finance, multi-agent, stocks, analysis]
    related_skills: [github-pr-workflow, plan]
---

# TradingAgents: Multi-Agent LLM Trading Analysis for Hermes

## Overview

Wraps [TradingAgents](https://github.com/tauricresearch/tradingagents) — a multi-agent trading framework that deploys specialized LLM-powered agents (fundamental analysts, sentiment experts, news analysts, technical analysts → research team → trader → risk management → portfolio manager) to collaboratively evaluate market conditions and produce trading decisions.

The package is installed at `C:\Users\64567\Desktop\tradingagents`.

## When to Use

- Analyze a stock/crypto ticker with AI agents.
- Get buy/sell/hold signals with supporting reasoning from multiple analyst perspectives.
- Research a ticker before making a decision — get fundamental, sentiment, news, and technical analysis in one pipeline.

## Quick Start

### 1. Configure API Keys

Edit `.env` in the tradingagents directory:

```
cd /c/Users/64567/Desktop/tradingagents
```

Set at least one LLM provider key in `.env` (copy from `.env.example`):
- `OPENAI_API_KEY=sk-...`
- Or `DEEPSEEK_API_KEY=...` / `GOOGLE_API_KEY=...` / `ANTHROPIC_API_KEY=...`

### 2. Run Quick Analysis (Non-Interactive)

Use the Hermes agent interface below. The agent will:
1. Set up the TradingAgentsGraph with your chosen LLM provider
2. Run the full multi-agent pipeline
3. Return the final trading decision with all analyst reports

### 3. Interactive CLI

For the full interactive experience with Rich TUI display:

```
cd /c/Users/64567/Desktop/tradingagents
python -m cli.main
```

This walks you through: ticker → date → language → analysts → research depth → LLM provider → model selection.

## Hermes Usage

### Run Trading Analysis via Python Script

The skill includes a helper script `scripts/trade.py` that wraps the core API. Use it from Hermes:

```python
from hermes_tools import terminal, write_file

# Run analysis
result = terminal(
    command='python /c/Users/64567/Desktop/tradingagents/skill_scripts/trade.py --ticker AAPL --date 2025-12-15 --provider deepseek --deep-model deepseek-chat --quick-model deepseek-chat',
    timeout=300
)
print(result['output'])
```

Or with environment variables:

```python
from hermes_tools import terminal

result = terminal(
    command='TRADINGAGENTS_LLM_PROVIDER=deepseek TRADINGAGENTS_DEEP_THINK_LLM=deepseek-chat python /c/Users/64567/Desktop/tradingagents/skill_scripts/trade.py --ticker AAPL --date 2025-12-15',
    timeout=300
)
```

### Available Options

| Flag | Description | Default |
|------|-------------|---------|
| `--ticker` | Stock/crypto ticker (e.g., AAPL, 0700.HK, BTC-USD) | Required |
| `--date` | Analysis date (YYYY-MM-DD) | Today |
| `--provider` | LLM provider (openai, deepseek, anthropic, google, openrouter, etc.) | openai |
| `--deep-model` | Deep thinking model name | provider default |
| `--quick-model` | Quick thinking model name | provider default |
| `--language` | Output language | English |
| `--analysts` | Comma-separated analysts: market,news,social,fundamentals | all |
| `--debate-rounds` | Max debate rounds | 1 |
| `--risk-rounds` | Max risk discussion rounds | 1 |
| `--save` | Save report to file | False |
| `--vendor` / `-v` | Data vendor: `alpha_vantage` for A股, `yfinance` for global | default config |

## Workflow

### Basic Analysis

1. Ensure at least one LLM API key is set in `.env`.
2. Call the trade script with your ticker of interest.
3. The pipeline runs: Analysts → Research Debate → Trader → Risk Mgmt → Portfolio Manager.
4. Read the final trade decision (BUY/SELL/HOLD with confidence and reasoning).

### Reading the Output

The pipeline produces these report sections in order:

1. **Market Analysis** — Technical indicators, price patterns, support/resistance.
2. **Social Sentiment** — StockTwits and Reddit sentiment aggregation.
3. **News Analysis** — Global news and macro events affecting the ticker.
4. **Fundamentals Analysis** — Financial statements, ratios, cash flow.
5. **Research Team Decision** — Bull vs Bear debate, judged by Research Manager.
6. **Trading Team Plan** — Entry/exit price, position sizing, stop-loss.
7. **Risk Management** — Aggressive/Neutral/Conservative debate on the plan.
8. **Portfolio Management Decision** — FINAL signal (BUY/SELL/HOLD) with confidence level and reasoning.

## Configuration

### Environment Variables (`.env`)

All standard TradingAgents env vars work:

| Variable | Description |
|----------|-------------|
| `TRADINGAGENTS_LLM_PROVIDER` | LLM provider name |
| `TRADINGAGENTS_DEEP_THINK_LLM` | Model for deep reasoning (analysts, research) |
| `TRADINGAGENTS_QUICK_THINK_LLM` | Model for quick reasoning (risk mgmt, tools) |
| `TRADINGAGENTS_TEMPERATURE` | Sampling temperature (0.0-1.0) |
| `TRADINGAGENTS_OUTPUT_LANGUAGE` | Report language (e.g., "Chinese", "English") |
| `TRADINGAGENTS_MAX_DEBATE_ROUNDS` | Max bull/bear debate rounds |
| `TRADINGAGENTS_MAX_RISK_ROUNDS` | Max risk discussion rounds |

### Chinese LLM Providers

For users in China, recommended providers. See `references/china-ashares.md` for full A-share ticker mappings and sector coverage.
- **DeepSeek** (recommended): set `DEEPSEEK_API_KEY`, provider=`deepseek`
- **Qwen (Tongyi Qianwen)**: set `DASHSCOPE_API_KEY`, provider=`qwen`
  - International region: auto; China region: set `DASHSCOPE_CN_API_KEY`, provider picks `qwen_cn`
- **GLM (Zhipu)**: set `ZHIPU_API_KEY`, provider=`glm`
- **MiniMax**: set `MINIMAX_API_KEY`, provider=`minimax`

## Common Pitfalls

1. **Missing API key**: The first API call will fail. Always set at least one provider key in `.env` before running.
2. **FRED API key**: Macro data (FRED) requires `FRED_API_KEY` — free from https://fred.stlouisfed.org/docs/api/api_key.html. If not set, macro analysis is skipped.
3. **Rate limits**: LLM providers may throttle. Set `TRADINGAGENTS_LLM_MAX_RETRIES=6` to ride out bursty 429s.
4. **Ticker format**: Use Yahoo Finance format: `AAPL`, `0700.HK`, `BTC-USD`, `GC=F` for gold.
5. **Memory log persistence**: Past decisions are stored in `~/.tradingagents/memory/trading_memory.md` and loaded as context for future same-ticker runs.
6. **Long runs**: Full pipeline with all 4 analysts + debate + risk can take 2-10 minutes depending on LLM speed.
7. **Windows path issues**: Use `/c/Users/...` paths in bash (git-bash) which Hermes runs on.

### China-Specific Pitfalls

8. **yfinance blocked by GFW**: Yahoo Finance API times out when accessed from mainland China. Use VPN, or set `--vendor alpha_vantage` to enable the dual-chain fallback (yfinance → Alpha Vantage).
9. **Alpha Vantage free tier quota**: Only 5 calls/min, 25 calls/day. The full pipeline needs 4+ data calls and can exhaust the daily limit in one run. Reduce analysts to `market,news` only, or upgrade to AV premium.
10. **Web research fallback**: When both data APIs fail from China, use `web_search` + `web_extract` to gather sector intelligence and build reports manually. Slower but reliable. See `references/china-ashares.md` for A-share ticker mappings and sector data.
11. **HTML report output**: User prefers dark-themed HTML reports saved to the desktop (`C:\Users\64567\Desktop\`). After analysis, generate via `write_file` with responsive dark layout for sharing.

## Verification Checklist

- [ ] TradingAgents package installed (`python -c "import tradingagents"` succeeds)
- [ ] At least one LLM API key set in `.env`
- [ ] Ticker is a valid Yahoo Finance symbol
- [ ] Analysis produces a final_trade_decision with BUY/SELL/HOLD signal
- [ ] Reports saved to `~/.tradingagents/logs/reports/` (when `--save` is set)

## Files

- **Package**: `C:\Users\64567\Desktop\tradingagents\` (git clone + pip install -e ".[dev]")
- **Helper script**: `C:\Users\64567\Desktop\tradingagents\skill_scripts\trade.py`
- **Config**: `C:\Users\64567\Desktop\tradingagents\.env`
- **Results**: `~/.tradingagents/logs/`
- **Cache**: `~/.tradingagents/cache/`
- **Memory**: `~/.tradingagents/memory/trading_memory.md`
- **China A-Share Reference**: `references/china-ashares.md` — ticker mappings, sector coverage, DeepSeek config for Chinese users
