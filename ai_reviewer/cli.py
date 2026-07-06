import argparse
import sys
from .input_handler import read_file
from .analyzer import analyze_code
from .prompt_builder import build_prompt
from .llm_client import get_ai_review
from .reporter import format_report

def main():
    # 1. Input Handling
    parser = argparse.ArgumentParser(description="AI-Powered Code Review CLI")
    parser.add_argument("filepath", help="Path to the code file you want to review")
    args = parser.parse_args()

    print(f"🔍 Reading file: {args.filepath}...")
    code_content = read_file(args.filepath)
    
    if not code_content:
        print("❌ Error: File is empty or could not be read.")
        sys.exit(1)

    # 2. Pre-processing & Static Analysis
    print("⚙️  Running static analysis...")
    analysis_data = analyze_code(code_content)

    # 3. Context Builder & Prompt Engineering
    print("📝 Assembling prompt...")
    prompt = build_prompt(code_content, analysis_data)

    # 4. AI Model Interaction
    print("🤖 Asking the AI for a review... (This might take a second)")
    raw_ai_response = get_ai_review(prompt)

    # 5. Response Analysis & Report Generation
    print("📊 Generating report...")
    final_report = format_report(raw_ai_response)

    # 6. CLI Output & Display
    print("\n" + "="*40)
    print("🚀 AI CODE REVIEW REPORT")
    print("="*40)
    print(final_report)
    print("="*40)

if __name__ == "__main__":
    main()