#!/usr/bin/env python3
"""
TradingAgents Hermes helper script.
Runs the full multi-agent trading pipeline from command line.

Usage:
    python trade.py --ticker AAPL --date 2025-12-15 --provider deepseek
    python trade.py --ticker 0700.HK --date 2025-12-15 --save
"""

import argparse
import json
import os
import sys
from datetime import datetime

# Add parent dir so the package resolves even when run from skill_scripts/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.graph.trading_graph import TradingAgentsGraph


def parse_args():
    parser = argparse.ArgumentParser(description="TradingAgents - Multi-Agent Trading Analysis")
    parser.add_argument("--ticker", "-t", required=True, help="Ticker symbol (e.g., AAPL, 0700.HK, BTC-USD)")
    parser.add_argument("--date", "-d", default=datetime.now().strftime("%Y-%m-%d"), help="Analysis date (YYYY-MM-DD)")
    parser.add_argument("--provider", "-p", default=None, help="LLM provider (openai, deepseek, anthropic, google, etc.)")
    parser.add_argument("--deep-model", default=None, help="Deep thinking model name")
    parser.add_argument("--quick-model", default=None, help="Quick thinking model name")
    parser.add_argument("--language", "-l", default="English", help="Output language")
    parser.add_argument("--analysts", default="market,news,social,fundamentals", help="Comma-separated analysts")
    parser.add_argument("--debate-rounds", type=int, default=1, help="Max debate rounds")
    parser.add_argument("--risk-rounds", type=int, default=1, help="Max risk discussion rounds")
    parser.add_argument("--save", action="store_true", help="Save report to file")
    parser.add_argument("--output", "-o", default=None, help="Output file path for JSON results")
    parser.add_argument("--asset-type", default="stock", choices=["stock", "crypto"], help="Asset type")
    parser.add_argument("--vendor", "-v", default=None,
                        choices=["yfinance", "alpha_vantage"],
                        help="Data vendor: 'alpha_vantage' for China A-shares, 'yfinance' for global stocks. Overrides default config.")
    return parser.parse_args()


def main():
    args = parse_args()

    # Build config - start with default and override
    config = DEFAULT_CONFIG.copy()
    config["output_language"] = args.language
    config["max_debate_rounds"] = args.debate_rounds
    config["max_risk_discuss_rounds"] = args.risk_rounds

    if args.provider:
        config["llm_provider"] = args.provider
    if args.deep_model:
        config["deep_think_llm"] = args.deep_model
    if args.quick_model:
        config["quick_think_llm"] = args.quick_model

    # Data vendor override (中国A股用alpha_vantage, 全球用yfinance)
    if args.vendor:
        for category in ("core_stock_apis", "technical_indicators", "fundamental_data", "news_data"):
            if category in config.get("data_vendors", {}):
                # Use as fallback chain: try yfinance first, fall back to alpha_vantage
                config["data_vendors"][category] = f"yfinance,{args.vendor}"
        # ALPHA_VANTAGE_API_KEY is auto-read from .env by the dataflows layer

    # Print configuration info
    print("=" * 70)
    print(f"  TradingAgents Analysis Pipeline")
    print("=" * 70)
    print(f"  Ticker:       {args.ticker}")
    print(f"  Date:         {args.date}")
    print(f"  Provider:     {config['llm_provider']}")
    print(f"  Deep model:   {config['deep_think_llm']}")
    print(f"  Quick model:  {config['quick_think_llm']}")
    print(f"  Analysts:     {args.analysts}")
    print(f"  Language:     {args.language}")
    vendor_display = args.vendor or config.get("data_vendors", {}).get("core_stock_apis", "default")
    print(f"  Data vendor:  {vendor_display}")
    print("=" * 70)
    print()

    # Parse selected analysts
    selected_analysts = tuple(a.strip() for a in args.analysts.split(","))

    # Detect asset type from ticker
    try:
        from tradingagents.cli.utils import detect_asset_type
        detected_asset_type = detect_asset_type(args.ticker).value
    except (ImportError, AttributeError):
        detected_asset_type = args.asset_type

    print(f"[INFO] Starting pipeline for {args.ticker} ({detected_asset_type})...")
    sys.stdout.flush()

    # Initialize and run
    try:
        ta = TradingAgentsGraph(
            selected_analysts=selected_analysts,
            debug=False,
            config=config,
        )

        print(f"[INFO] Pipeline started. Running analysts, research, trading, risk, portfolio...")
        sys.stdout.flush()

        final_state, decision = ta.propagate(args.ticker, args.date, asset_type=detected_asset_type)

        print()
        print("=" * 70)
        print("  FINAL TRADE DECISION")
        print("=" * 70)
        print(f"  {decision}")
        print("=" * 70)
        print()

        # Save report if requested
        if args.save:
            report_path = ta.save_reports(final_state, args.ticker)
            print(f"[INFO] Report saved to: {report_path}")

        # Output JSON if requested
        if args.output:
            output_data = {
                "ticker": args.ticker,
                "date": args.date,
                "decision": decision,
                "reports": {
                    "market_report": final_state.get("market_report", ""),
                    "sentiment_report": final_state.get("sentiment_report", ""),
                    "news_report": final_state.get("news_report", ""),
                    "fundamentals_report": final_state.get("fundamentals_report", ""),
                    "investment_plan": final_state.get("investment_plan", ""),
                    "final_trade_decision": final_state.get("final_trade_decision", ""),
                }
            }
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(output_data, f, ensure_ascii=False, indent=2)
            print(f"[INFO] JSON output saved to: {args.output}")

        # Print summary of reports
        print()
        print("=" * 70)
        print("  ANALYSIS SUMMARY")
        print("=" * 70)

        sections = [
            ("Market Analysis", final_state.get("market_report", "")),
            ("Sentiment Analysis", final_state.get("sentiment_report", "")),
            ("News Analysis", final_state.get("news_report", "")),
            ("Fundamentals Analysis", final_state.get("fundamentals_report", "")),
            ("Investment Plan", final_state.get("investment_plan", "")),
        ]

        for name, content in sections:
            if content:
                words = len(content.split())
                print(f"  ✓ {name}: {words} words")

        print()
        print("=" * 70)
        print("  DONE")
        print("=" * 70)

    except Exception as e:
        print(f"[ERROR] Pipeline failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
