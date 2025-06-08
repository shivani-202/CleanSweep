import sweetviz as sv
import os
import logging

def generate_eda_report(df, output_html="eda_report.html"):
    """
    Generates an interactive EDA report using SweetViz.
    """
    try:
        report = sv.analyze(df)
        report.show_html(output_html, open_browser=False)
        logging.info(f" EDA report saved to {output_html}")
    except Exception as e:
        logging.exception("Error")
        raise e
