#!/usr/bin/env python3
"""MiMo Travel Planner - AI trip planning."""
import os, argparse
from openai import OpenAI

client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url="https://api.xiaomimimo.com/v1")

def plan(dest, days=3, budget="medium"):
    r = client.chat.completions.create(model="mimo-v2.5-pro", messages=[
        {"role": "system", "content": f"{days}-day itinerary. Budget: {budget}. Schedule, food, tips, costs."},
        {"role": "user", "content": f"Plan {days} days in {dest}"}], max_tokens=3000)
    return r.choices[0].message.content

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("dest"); p.add_argument("--days", type=int, default=3); p.add_argument("--budget", default="medium")
    a = p.parse_args(); print(plan(a.dest, a.days, a.budget))
