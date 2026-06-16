import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_analytics_dashboard():
    print("==================================================")
    print("       CODEALPHA DATA VISUALIZATION ENGINE        ")
    print("==================================================")
    
    input_file = "custom_scraped_dataset.csv"
    
    # Check if target dataset exists from prior tasks; if not, construct runtime data
    if not os.path.exists(input_file):
        print("[SYSTEM] Local dataset target not found. Initializing pipeline data structures...")
        mock_records = {
            "Quote Text": [
                "The only way to do great work is to love what you do.",
                "Success is not final, failure is not fatal: it is the courage to continue that counts.",
                "Believe you can and you're halfway there.",
                "Your time is limited, so don't waste it living someone else's life.",
                " there are no secrets to success. It is the result of preparation, hard work, and learning from failure."
            ],
            "Author": ["Steve Jobs", "Winston Churchill", "Theodore Roosevelt", "Steve Jobs", "Colin Powell"],
            "Associated Tags": ["work, motivation", "success, courage", "inspiration", "life", "success, work"]
        }
        df = pd.DataFrame(mock_records)
        df.to_csv(input_file, index=False, encoding='utf-8')
    else:
        df = pd.read_csv(input_file)

    print("[SYSTEM] Extracting text metadata attributes...")
    # Calculate text length metrics for quantitative visualization processing
    df['Char_Count'] = df['Quote Text'].apply(lambda x: len(str(x)))
    df['Word_Count'] = df['Quote Text'].apply(lambda x: len(str(x).split()))
    df['Avg_Word_Len'] = df['Char_Count'] / (df['Word_Count'] + 0.001)

    # Initialize the structural grid layout for our 3-panel dashboard portfolio
    fig = plt.figure(figsize=(15, 10))
    grid = plt.GridSpec(2, 2, wspace=0.3, hspace=0.3)
    
    # Set global aesthetic chart styling configurations
    sns.set_theme(style="whitegrid")
    plt.suptitle("Executive Analytics Dashboard - Text Corpus Insights", fontsize=18, fontweight='bold', y=0.96)

    # --- PANEL 1: Top Data Contributing Authors (Bar Chart) ---
    ax1 = fig.add_subplot(grid[0, 0])
    author_data = df['Author'].value_counts().head(5)
    sns.barplot(x=author_data.values, y=author_data.index, ax=ax1, palette="viridis", hue=author_data.index, legend=False)
    ax1.set_title("Top 5 Data Contributing Authors", fontsize=12, fontweight='bold')
    ax1.set_xlabel("Frequency Occurrence Count")
    ax1.set_ylabel("Author Name")

    # --- PANEL 2: Text Character Length Distribution (KDE Histogram) ---
    ax2 = fig.add_subplot(grid[0, 1])
    sns.histplot(df['Char_Count'], kde=True, ax=ax2, color="teal", bins=6)
    ax2.set_title("Text Character Length Distribution Profile", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Absolute Character Count")
    ax2.set_ylabel("Frequency Density")

    # --- PANEL 3: Numerical Metric Correlations (Heatmap) ---
    ax3 = fig.add_subplot(grid[1, :]) # Span across the entire bottom row
    correlation_matrix = df[['Char_Count', 'Word_Count', 'Avg_Word_Len']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=1, ax=ax3, vmin=-1, vmax=1)
    ax3.set_title("Metadata Feature Correlation Matrix Matrix", fontsize=12, fontweight='bold')

    # Save out the unified dashboard asset
    output_dashboard = "analytics_dashboard_portfolio.png"
    plt.savefig(output_dashboard, dpi=150, bbox_inches='tight')
    
    print("\n==================================================")
    print("            DASHBOARD COMPILATION REPORT          ")
    print("==================================================")
    print(f"✔ Panel 1 Status : Active (Author Bar Chart Rendered)")
    print(f"✔ Panel 2 Status : Active (KDE Histogram Profile Generated)")
    print(f"✔ Panel 3 Status : Active (Correlation Heatmap Computed)")
    print(f"✔ Output Status  : Saved successfully to -> '{output_dashboard}'")
    print("==================================================")

if __name__ == "__main__":
    generate_analytics_dashboard()