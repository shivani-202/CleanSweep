import logging
from ydata_profiling import ProfileReport

def generate_profile_report(df, output_html="profile_report.html"):
    """
    Generates an EDA report using ydata-profiling (formerly pandas-profiling).
    """
    try:
        profile = ProfileReport(df, title="Data Cleaning Bot EDA Report", explorative=True)
        profile.to_file(output_file=output_html)
        logging.info(f"📊 ydata-profiling report saved to {output_html}")
    except Exception as e:
        logging.exception("❌ Failed to generate profiling report.")
        raise e
