# China A-Share Market Reference

## Ticker Suffix Rules (Yahoo Finance)

Chinese stocks on Yahoo Finance use exchange suffixes:

| Exchange | Suffix | Example |
|----------|--------|---------|
| Shanghai Stock Exchange (SSE) | `.SS` | 688981.SS (中芯国际) |
| Shenzhen Stock Exchange (SZSE) | `.SZ` | 002475.SZ (立讯精密) |
| Hong Kong Stock Exchange | `.HK` | 0700.HK (腾讯控股) |

**Important**: A-share ticker codes on Yahoo Finance must include the exchange suffix. `688981` alone will NOT resolve.

## Sector → Ticker Mapping (Core Sectors)

### 半导体 Semiconductors
- 中芯国际 (SMIC) — 688981.SS — 晶圆代工龙头
- 北方华创 — 002371.SZ — 半导体设备
- 兆易创新 — 603986.SS — 存储芯片/MCU
- 韦尔股份 — 603501.SS — CIS图像传感器
- 紫光国微 — 002049.SZ — 特种芯片/FPGA

### 消费电子 Consumer Electronics
- 立讯精密 — 002475.SZ — 苹果供应链/连接器
- 歌尔股份 — 002241.SZ — VR/声学
- 蓝思科技 — 300433.SZ — 玻璃盖板
- 传音控股 — 688036.SS — 非洲手机市场

### CPO / 光模块 Co-packaged Optics
- 中际旭创 — 300308.SZ — 光模块龙头，2026Q1净利润+262%
- 新易盛 — 300502.SZ — 光模块
- 天孚通信 — 300394.SZ — 光器件
- 源杰科技 — 688498.SS — 光芯片
- 长光华芯 — 688048.SS — 激光芯片

### 算电协同 Computing-Electricity Synergy (2026新主线)
- 协鑫能科 — 002015.SZ — 算电协同绝对龙头，绿电+算力+储能
- 豫能控股 — 001896.SZ — 火电算力双驱，京津冀1GW算力
- 中恒电气 — 002364.SZ — 数据中心HVDC电源龙头
- 南网数字 — 301638.SZ — 首套"电碳算协同"系统
- 国电南瑞 — 600406.SH — 电网AI调度龙头，市占率60%+
- 金开新能 — 600821.SH — 源网荷储一体化
- 中国能建 — 601868.SH — 央企，新能源+算力方案
- 广电电气 — 601616.SH — 数据中心变压器

### 5G / 通信
- 中兴通讯 — 000063.SZ — 主设备商
- 信维通信 — 300136.SZ — 射频
- 中天科技 — 600522.SS — 光纤光缆
- 亨通光电 — 600487.SS — 光纤光缆

### 创新药 Innovative Drugs
- 恒瑞医药 — 600276.SS — 创新药龙头
- 百济神州 — 688235.SS — 肿瘤创新药
- 信达生物 — 1801.HK — 生物药
- 康希诺 — 688185.SS — 疫苗
- 药明康德 — 603259.SS — CXO龙头

## Recommended DeepSeek Config for Chinese Users

```ini
# .env
DEEPSEEK_API_KEY=sk-...
ALPHA_VANTAGE_API_KEY=xxx  # fallback when yfinance blocked

TRADINGAGENTS_LLM_PROVIDER=deepseek
TRADINGAGENTS_DEEP_THINK_LLM=deepseek-chat
TRADINGAGENTS_QUICK_THINK_LLM=deepseek-chat
TRADINGAGENTS_OUTPUT_LANGUAGE=Chinese
TRADINGAGENTS_TEMPERATURE=0.1
TRADINGAGENTS_LLM_MAX_RETRIES=3
```

- `deepseek-chat` = V3 model, fast and capable
- Temperature 0.1 for more deterministic analysis output

## Quick Analysis Command

```bash
cd /c/Users/64567/Desktop/tradingagents
python skill_scripts/trade.py \
  --ticker 300308.SZ \
  --date 2026-07-06 \
  --provider deepseek \
  --deep-model deepseek-chat \
  --quick-model deepseek-chat \
  --language Chinese \
  --analysts market,news,fundamentals \
  --vendor alpha_vantage \
  --save
```

**Note**: `--vendor alpha_vantage` sets a dual fallback chain `yfinance,alpha_vantage`. yfinance is tried first; if blocked/rate-limited from China, Alpha Vantage takes over.

## Known Data Source Limitations from China

### Blockers
| Source | Issue | Symptom |
|--------|-------|---------|
| yfinance | GFW blocks Yahoo Finance API | Connection timeout after 30s |
| Alpha Vantage (free) | 5 req/min, 25 req/day quota | "rate-limited" on 2nd+ call in same run |

### Workarounds (in priority order)
1. **VPN** — Connect before running; yfinance works normally
2. **Dual-vendor chain** — Already built into `--vendor alpha_vantage`; tries yfinance first, falls to AV
3. **Minimal analysts** — Reduce from 4 to 2 (`market,news`) to halve API calls per run
4. **Web research fallback** — When both APIs fail, use `web_search` + `web_extract` for sector-level intelligence and build report manually (slower but more reliable from China)
5. **Alpha Vantage premium** — $150/mo for 300 calls/min (only if heavy usage)

## Related ETFs (for fund recommendation)

| Fund | Code | Focus |
|------|------|-------|
| 电力ETF景顺 | 159158 | 算电协同+绿电直连 |
| 绿电ETF华夏 | 562550 | 绿色电力 |
| 电网ETF | 561380 | 电网设备全产业链 |

## Notes

- A-share market data on Yahoo Finance has ~15min delay for free tier
- For backtesting: pick a historical date, not today
- Social sentiment analyst (StockTwits/Reddit) has limited coverage on Chinese stocks — consider omitting `social` from analysts list
- Fundamentals data from yfinance for Chinese stocks may have gaps; Alpha Vantage can be a fallback
