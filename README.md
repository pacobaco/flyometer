# modelometer

**Measuring AI brilliance, one keyword at a time.**

modelometer is a Python tool to track, rate, and rank AI models based on keyword performance. It polls a curated list of AI models, evaluates responses, and generates comparative reports to help you see which model performs best for specific keywords.

## Features
- Poll multiple AI models (OpenAI, Anthropic, LLaMA, etc.)
- Evaluate responses for relevance, completeness, and quality
- Save results in JSON and CSV formats
- Historical tracking and comparison
- Easily extensible to add new models or metrics

## Installation
```bash
git clone https://github.com/yourusername/modelometer.git
cd modelometer
pip install -r requirements.txt
```

## Configuration
Set your API keys and desired models/keywords in `config.yaml`.
